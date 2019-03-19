# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

app = Flask(__name__)
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route("/")
def PyJoo():
    print('Func_called - main')
    return "PyJoo"    

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'   

if __name__ == '__main__':
    print('Func_called - main')
    app.run(host="0.0.0.0", port=5000, debug = True)
else:
    print('Func_called - imported')