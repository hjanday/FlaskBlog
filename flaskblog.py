#imports
from flask import Flask, render_template, url_for
app = Flask(__name__)




#define some sample data
#sample blog post
posts=[
    {
        'author': 'Harp',
        'title': '1st Post',
        'content': 'deez nuts',
        'post_date': '12/31/2020'
    },
    {
        'author': 'Joe',
        'title': 'My Post',
        'content': 'nuts',
        'post_date': '01/01/2021'
    }
]

#routes are just the links like FAQ, about and so on
@app.route("/")
@app.route("/home")
#each route has its method which can render a template which is an html file
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')



#debug lets you auto update changes
if __name__ == '__main__':
    app.run(debug=True)