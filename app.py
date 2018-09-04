import os
import requests
from bottle import route, post, run, abort, static_file, redirect, request

current_path = os.path.dirname(os.path.realpath(__file__))
static_path = os.path.join(current_path, 'static')

@route("/")
def hello_world():
    return static_file('bbva.html', root=static_path)

run(server='gunicorn', host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
