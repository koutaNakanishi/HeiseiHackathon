from flask import Flask, render_template, request

import ddtable_process
import event_process

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/dd-table', methods=["GET"])
def dd_table():
    yymm = request.args.get('yymm')
    return ddtable_process.get_ddtable_json(yymm)


@app.route("/event", methods=["GET"])
def event():
    yymm = request.args.get('yymm')
    return event_process.get_event_json(yymm)


if __name__ == "__main__":
    app.run(debug=True)
