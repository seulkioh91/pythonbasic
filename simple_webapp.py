from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'

@app.route('/page1')
def page1() -> str:
    return 'This is page1.'

@app.route('/page2')
def page2() -> str:
    return 'This is page2.'

@app.route('/page3')
def page3() -> str:
    return 'This is page3.'

if __name__ == '__main__':
    app.run()