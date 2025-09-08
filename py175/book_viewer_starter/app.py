from flask import Flask, render_template, g, redirect, request

app = Flask(__name__)

@app.before_request
def load_contents():
    with open("book_viewer/data/toc.txt", "r") as file:
        g.contents = file.readlines()

def in_paragraphs(text):
    return text.split("\n\n")

    # formatted_paragraphs = [
    #     {paragraph} for paragraph in paragraphs if paragraph
    # ]
    # return ''.join(formatted_paragraphs)

app.jinja_env.filters['in_paragraphs'] = in_paragraphs

def highlight(text, query):
    return text.replace(query, f'<strong>{query}</strong>')

app.jinja_env.filters['highlight'] = highlight

@app.route("/")
def index():
    return render_template('home.html', contents=g.contents)

@app.route("/chapters/<page_num>")
def chapter(page_num):
    if page_num.isdigit() and int(page_num) in range(1, len(g.contents)):
        chapter_name = g.contents[int(page_num) - 1]
        chapter_title = f"Chapter {page_num}: {chapter_name}"

        with open(f"book_viewer/data/chp{page_num}.txt", "r") as file:
            chapter = file.read()

        return render_template('chapter.html',
                           chapter_title=chapter_title,
                           contents=g.contents,
                           chapter=chapter)
    
    return redirect('/')

# capture the value of the input field from search.html
# save that value to a variable `query`
#   render the search.html with nothing else if no query
# if query, search each chapter for the query value
#   return a list of chapters that contain the value
#   display list on search page

def chapters_matching(query):
    if not query:
        return []

    results = []
    for index, name in enumerate(g.contents, start=1):
        with open(f"book_viewer/data/chp{index}.txt", "r") as file:
            chapter_content = file.read()

        matches = {}
        for para_index, paragraph in enumerate(chapter_content.split("\n\n")):
            if query.lower() in paragraph.lower():
                matches[para_index] = paragraph
        if matches:
            results.append({'number': index, 'name': name, 'paragraphs': matches})

    return results

@app.route("/search")
def search():
    # results needs to be a list of paragraphs instead of chapters
    # looks like I want both the chapter titles and the actual paragraphs to
    #   be returned by the search

    # the paragraphs listed need to link correctly, so anchor to paragraph id
    #   which means I salso need paragraph ids (do in `in_paragraphs`?)
    #   I think that's done correctly
    query = request.args.get('query', '')
    results = chapters_matching(query) if query else []

    return render_template('search.html', query=query, results=results)

@app.errorhandler(404)
def page_not_found(_error):
#    return render_template('404.html'), 404
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5003)