from flask import Flask, render_template, request, url_for, flash, redirect, session, make_response

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    # print(sensors_tuple[0].sensorLocation)

    # return 'Hello world'
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(host='192.168.42.209')
    app.run()