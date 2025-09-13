'''
Requirements
1. When a user loads the home page, they should be redirected to a page that
 lists all of the users' names. Load the users from the
 users.yaml file.
2. Each of the users' names should be a link to a page for that user.
3. On each user's page, display their email address.
 Also, display their interests, with a comma appearing between each interest.
4. At the bottom of each user's page, list links to all of the
 other users pages. Do not include the user whose page it is in this list.
5. Add a layout to the application. At the bottom of every page, display
 a message like this: "There are 3 users with a total of 9 interests."
6. Update the message printed out in #5 to determine the number of users
 and interests based on the content of the YAML file.
 Use a view helper method, total_interests, to determine the total number
 of interests across all users.
7. Add a new user to the users.yaml file. Verify that the site updates accordingly.
'''

from flask import Flask, redirect, render_template, g, request
import yaml

app = Flask(__name__)

with open('users.yaml', 'r') as file:
    user_data = yaml.safe_load(file)
    names = [name for name in user_data.keys()]

def num_users():
    return len(names)

def num_interests():
    interests = 0
    for user in user_data.values():
        interests += len(user['interests'])
    return interests

app.jinja_env.globals.update(num_users=num_users)
app.jinja_env.globals.update(num_interests=num_interests)

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return redirect('/users')
    
@app.route('/users')
def users():
    return render_template('users.html', content=names)

@app.route('/profile/name=<user_name>')
def profile(user_name):
    if user_name not in names:
        return render_template('404.html')

    other_users = [name for name in names if name != user_name]
    user_info = user_data.get(user_name)

    return render_template('profile.html', 
                           user_info=user_info, 
                           other_users=other_users)

@app.errorhandler(404)
def page_not_found(_error):
    return render_template('404.html'), 404

@app.route('/print_test')
def print_test(var_you_want_printed):
    # to directly see what a given variable holds, for troubleshooting
    # return print_test(arg) in the applicable function
    # then navigate to this route
    return var_you_want_printed


if __name__ == '__main__':
    app.run(debug=True, port=5000)
