from flask import *

app = Flask(__name__)	

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/submit_link')
def submit_link():
    return render_template("submit.html")

@app.route('/add_link')
def add_link():
    # do stuff
    return "Link submitted successfully"

if __name__ == '__main__':
    app.debug=True
    app.run()
