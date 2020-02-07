from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')



if __name__ == '__name__':
    app.run(debug = True)

    # $env:FLASK_ENV = "development"
