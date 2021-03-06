import os

from flask import Flask, request, send_from_directory

import ddtable_process
import event_process

app = Flask(__name__)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/dd-table', methods=["GET"])
def dd_table():
    yymm = request.args.get('yymm')
    return ddtable_process.get_ddtable_json(yymm)


@app.route("/event", methods=["GET"])
def event():
    yymm = request.args.get('yymm')
    return event_process.get_event_json(yymm)


@app.route('/favicon.ico', methods=["GET"])
def favicon():
    favicon_name = "favicon.gif"
    favicon_pass = os.path.join(app.root_path, 'static', 'images')
    return send_from_directory(favicon_pass, favicon_name, mimetype='image/gif')


if __name__ == "__main__":
    app.run(debug=True)
