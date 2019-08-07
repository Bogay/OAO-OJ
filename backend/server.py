import os
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

TMP_DIR = 'tmp'
TEST_DIR = 'testdata'

def readAll(name):
    with open(name, 'r') as f:
        ret = f.read()
    return ret


@app.route('/', methods=['POST'])
def submit():
    script = request.values['script'].strip()
    inData = request.values.get('input-data', readAll(f'{TEST_DIR}/test.in'))
    outData = request.values.get('output-data', readAll(f'{TEST_DIR}/test.out')).strip()

    if any(c in script for c in ['\n', '\r', ';']):
        return jsonify({'result': 'LLE'})

    with open(f'{TMP_DIR}/a.py', 'w') as f:
        f.write(script)
    with open(f'{TMP_DIR}/a.in', 'w') as f:
        f.write(inData)

    os.system(f'cd {TMP_DIR} && python3 a.py < a.in > a.out')

    return jsonify({'result': ['WA', 'AC'][readAll(f'{TMP_DIR}/a.out').rstrip() == outData]})


if __name__ == '__main__':
    app.run()
