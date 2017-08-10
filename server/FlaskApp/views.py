#!flask/bin/python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.errorhandler(404)
def page_not_found(error):
    return 'This page doesn\'t exist', 404

if __name__ == '__main__':
    app.run(debug=True)
