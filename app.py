from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/about')
def home2():
    return render_template('about.html')



if __name__ == '__name__':
    app.run(debug = True)

    # $env:FLASK_ENV = "development"
