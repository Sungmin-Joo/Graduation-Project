
from flask import Flask, render_template, request, jsonify
import os

def Find_dir(root):
    return os.listdir(root)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return render_template('post.html')

@app.route('/download/food')
def download_food():
    arr = Find_dir("./update/word/food")
    data = {}
    for i in arr:
        f = open("./update/word/food/" + i,'r')
        lines = f.readlines()
        data[i] = lines
        f.close()

    return jsonify(data)

@app.route('/download/place')
def download_place():
    arr = Find_dir("./update/word/place")
    data = {}
    for i in arr:
        f = open("./update/word/place/" + i,'r')
        lines = f.readlines()
        data[i] = lines
        f.close()

    return jsonify(data)

@app.route('/download/vehicle')
def download_vehicle():
    arr = Find_dir("./update/word/vehicle")
    data = {}
    for i in arr:
        f = open("./update/word/vehicle/" + i,'r')
        lines = f.readlines()
        data[i] = lines
        f.close()

    return jsonify(data)

@app.route('/download/version')
def check_version():
    arr = Find_dir("./update/word/version")
    data = {}
    for i in arr:
        f = open("./update/word/version/" + i,'r')
        lines = f.readlines()
        data[i.replace('.txt','')] = lines
        f.close()

    return jsonify(data)

@app.route('/post', methods=['POST'])
def post():
    value = request.form['test']
    return value


@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    print('Func_called - main')
    app.run(host="0.0.0.0", port=30000, debug = True)

else:
    print('Func_called - imported')
