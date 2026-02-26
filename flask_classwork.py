from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/training/<string:prof>')
def index(prof):
    return render_template('base.html', prof=prof)

@app.route('/')
@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_temp.html', title=list, list=list)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
