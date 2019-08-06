import os
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def readAll(name):
    with open(name, 'r') as f:
        ret = f.read()
    return ret


@app.route('/', methods=['GET'])
def index():
    return readAll('index.md')


@app.route('/', methods=['POST'])
def submit():
    script = request.values['script'].strip()
    inData = request.values.get('inputData', readAll('test.in'))
    outData = request.values.get('outputData', readAll('test.out')).strip()

    if any(c in script for c in ['\n', '\r', ';']):
        return jsonify({'result': 'LLE'})

    with open('a.py', 'w') as f:
        f.write(script)
    with open('a.in', 'w') as f:
        f.write(inData)
    os.system(f'python3 a.py < a.in > a.out')

    return jsonify({'result': ['WA', 'AC'][readAll('a.out').rstrip() == outData]})


if __name__ == '__main__':
    app.run()
