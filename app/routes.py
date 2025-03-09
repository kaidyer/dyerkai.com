from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    resume = [
        "SWE @ Company 1",
        "SWE Intern @ Company 2"
    ]
    return render_template('index.html', resume=resume)