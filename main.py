#!/usr/bin/env python3
import json
import threading
import importlib
import webbrowser
from core.libs.bottle import Bottle, template, static_file

with open("config.json") as fconfig:
    config = json.load(fconfig)

app     = Bottle()
methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]

@app.route("/css/<filename:re:.+\.css$>", method="GET")
def css_server(filename):
    return static_file(filename, root="views/css")

@app.route("/js/<filename:re:.+\.js$>", method="GET")
def js_server(filename):
    return static_file(filename, root="views/js")

@app.route("/img/<filename:re:.+\.(png|gif|jpe?g)$>", method="GET")
def img_server(filename):
    return static_file(filename, root="views/img")

@app.route("/", method=methods)
@app.route("/<controller>", method=methods)
@app.route("/<controller>/<args:path>", method=methods)
def get_handler(controller="init", args=""):
    ctrl = controller.lower()
    args = args.split("/")
    try:
        controller = importlib.import_module("controllers.{}".format(ctrl))
    except ImportError:
        return template("error", ctrl=ctrl)
    try:
        controller = getattr(controller, ctrl.title())
    except AttributeError:
        raise ValueError("There is no \"{}\" controller class."\
                        .format(ctrl.title()))
    return controller().run(*args)

def run():
    app.run(**config["bottle"])

if __name__ == "__main__":
    host = config["bottle"]["host"]
    port = config["bottle"]["port"]
    url  = "http://{host}:{port}/".format(host=host, port=port)
    threading.Thread(target=run).start()
    webbrowser.open(url)