__author__ = 'Test-YLL'

from flask import Flask, render_template
app = Flask(__name__)

'''
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# 动态路由
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)




if __name__ == '__main__':
    app.run(debug=True)