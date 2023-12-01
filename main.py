import datetime
import io
import json
import pprint

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/data/test")
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_data = {
      "dates": [
        datetime.datetime(2018, 1, 1, 10, 0, 0).strftime("%Y-%m-%d"),
        datetime.datetime(2018, 1, 2, 10, 30, 0).strftime("%Y-%m-%d"),
        datetime.datetime(2018, 1, 3, 11, 0, 0).strftime("%Y-%m-%d"),
      ]}

    return dummy_data


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
