import random
import requests
import logging

from builtins import KeyError
from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask, request, jsonify, render_template
from flask_expects_json import expects_json

log = logging.getLogger("werkzeug")
log.setLevel(logging.WARN)

app = Flask(__name__)

REGISTRY = {}

logging.basicConfig(level=logging.INFO)


PAYLOAD_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["port", "username"],
    "properties": {
        "port": {
            "$id": "#/properties/port",
            "type": "integer",
            "title": "The port of the registered container",
            "examples": [42049],
        },
        "username": {
            "$id": "#/properties/username",
            "type": "string",
            "title": "The username that the registered container belongs to",
            "examples": ["Emily", "Mika", "Super Cool Pylady"],
            "pattern": "^(.*)$",
        },
    },
}


def send_telemetry_data():
    """ Send telemetry data to registered users

    Iterates over the registered users, and POSTs telemetry data to them.

    This is run as a job by the ``BackroundScheduler`` on a specified interval.
    """

    telemetry = _generate_telemetry_data()
    for username in REGISTRY:
        for container in REGISTRY[username]["containers"]:
            url = f"http://{container}"
            try:
                requests.post(url, json=telemetry, timeout=1)
                REGISTRY[username]["containers"][container]["success"] += 1
            except requests.exceptions.RequestException as request_exception:
                logging.warning(
                    "Error posting to {} at {}, caused by {}".format(
                        username, url, request_exception
                    )
                )
                REGISTRY[username]["containers"][container]["error"] += 1


def _generate_telemetry_data():
    """ Generate randomised telemetry data """

    return {
        "humidity": float(random.randrange(60, 85)),
        "temperature": float(random.randrange(16.0, 25.0)),
        "luminosity": random.randrange(0, 1025),
    }


scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(send_telemetry_data, "interval", seconds=10, id="send_telemetry_data")
scheduler.start()


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/containers")
def containers():
    return jsonify(REGISTRY)


@app.route("/register", methods=["POST"])
@expects_json(PAYLOAD_SCHEMA)
def register():
    """Register a container

    Accepts a POST request with a JSON body containing:
    {
      "username": "Pylady A",
      "port": 65432
    }

    Adds this user's username, IP and port to the Registry.
    """
    ip_address = request.remote_addr
    payload = request.get_json(silent=True)

    key = f"{ip_address}:{payload['port']}"

    if payload["username"] not in REGISTRY:
        REGISTRY[payload["username"]] = {
            "containers": {key: {"success": 0, "error": 0}}
        }
    else:
        REGISTRY[payload["username"]]["containers"][key] = {"success": 0, "error": 0}

    logging.info("registered user {} at: {}".format(payload["username"], key))
    return "Registering {} with IP Address {} and port {}".format(
        payload["username"], ip_address, payload["port"]
    )


@app.route("/deregister", methods=["POST"])
@expects_json(PAYLOAD_SCHEMA)
def deregister():
    """Deregister a container

    Accepts a POST request with a JSON body containing:
    {
      "username": "Pylady A",
      "port": 65432
    }

    Removes the IP and port from the user's registerd containers. If it is the last
    registered container, it removes the user as well.
    """

    ip_address = request.remote_addr
    payload = request.get_json(silent=True)
    username = payload["username"]
    port = payload["port"]

    key = f"{ip_address}:{port}"

    try:
        REGISTRY[username]["containers"].pop(key)
        if len(REGISTRY[username]["containers"].keys()) == 0:
            REGISTRY.pop(username)
        return "Deregistered {}".format(key)
    except KeyError as keyerror:
        return "{} has no registered containers.".format(request.remote_addr), 404


if __name__ == "__main__":

    app.run(host="0.0.0.0")
