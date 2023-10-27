from flask import Flask, render_template
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index2.html')
    return render_template('index2.css')


@app.route('/run-python')
def run_python():
    result = subprocess.getoutput(' Dr. Diagnosis.py')
    return result


if __name__ == '__main__':
    app.run()
