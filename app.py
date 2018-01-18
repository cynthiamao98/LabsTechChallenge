from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/sm4396')
def subpage():
    return render_template('sm4396.html')


if __name__ == '__main__':
    app.run()
