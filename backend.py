from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    fib(3)
    return render_template('index.html',result=fib(3))

def fib(num):
    return num

if __name__ == '__main__':
    app.run(debug=True)