from flask import Flask, render_template, g

app = Flask(__name__)

@app.before_request
def load_contents():
    with open("book_viewer/data/toc.txt", "r") as file:
        g.contents = file.readlines()

def in_paragraphs(text):
    paragraphs = text.split("\n\n")
    formatted_paragraphs = [
        f'<p>{paragraph}</p>' for paragraph in paragraphs if paragraph
    ]
    return ''.join(formatted_paragraphs)

app.jinja_env.filters['in_paragraphs'] = in_paragraphs

@app.route("/")
def index():
    return render_template('home.html', contents=g.contents)

@app.route("/chapters/<page_num>")
def chapter(page_num):

    chapter_name = g.contents[int(page_num) - 1]
    chapter_title = f"Chapter {page_num}: {chapter_name}"

    with open(f"book_viewer/data/chp{page_num}.txt", "r") as file:
        chapter = file.read()

    return render_template('chapter.html',
                           chapter_title=chapter_title,
                           contents=g.contents,
                           chapter=chapter)

@app.route("/show/<name>")
def show(name):
    return name

@app.route("/quack")
def quack():
    return render_template('home.html', contents=['Quack! Quack! Quack!'])

if __name__ == "__main__":
    app.run(debug=True, port=5003)