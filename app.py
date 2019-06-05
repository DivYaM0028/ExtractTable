from flask import Flask , render_template
from page import Pages

app = Flask(__name__)

Pages=Pages()

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/table')
def pages():
    return render_template('page.html', pages=Pages)


if __name__ == '__main__':
    app.run(debug=True)