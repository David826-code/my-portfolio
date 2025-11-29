from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

year = datetime.now().year

@app.route('/')
def home():
    return render_template('home.html', year=year, title='home')

@app.route('/about')
def about():
    return render_template('about.html', year=year, title='about')

@app.route('/skills')
def skills():
    return render_template('skills.html', year=year, title='skills')

@app.route('/projects')
def projects():
    return render_template('projects.html', year=year, title='projects')

@app.route('/contact')
def contact():
    return render_template('contact.html', year=year, title='contact')

if __name__ == '__main__':
    app.run(debug=True)
