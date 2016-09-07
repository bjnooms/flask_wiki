from flask import Flask, render_template

from content_management import contentManagement
CMS = contentManagement()

app = Flask(__name__)

@app.route('/')
def homepage():
    return('This is the homepage.')

#@app.route('/wiki/')
#def wiki():
#    return render_template("wiki.html", CMS = CMS)

if __name__ == "__main__":
    app.run()
