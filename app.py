from flask import Flask, render_template, url_for
from forms import SignupForm, SignInForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c4ebd5c19784795cce458b28cf63e20a' #Used Secrets module in python to generate a secret key to protect against some potential attacks. 

posts = [
    {
        'name': 'Peter',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date': 'September 29, 2021'
    }
]

@app.route("/")
@app.route("/home")
def main_page():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title='About')

@app.route("/recent_movies")
def recent_movies_page():
    return render_template('recent_movies.html', title='Recent Movies')

@app.route("/genres")
def genres_page():
    return render_template('genres.html', title='Genres')

@app.route("/sign_in")
def sign_in_page():
    form = SignInForm()
    return render_template('sign_in.html', title='Sign in', form=form)

@app.route("/sign_up")
def sign_up_page():
    form = SignupForm()
    return render_template('sign_up.html', title='Sign up', form=form)

@app.route("/movie_picker")
def movie_picker_page():
    return render_template('movie_picker.html', title='Movie Picker')