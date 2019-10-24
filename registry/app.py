import random
import requests
import logging

from builtins import KeyError
from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

REGISTRY = {}

logging.basicConfig(level=logging.INFO)


def send_telemetry_data():
    """ Post telemetry data to registered users """

    telemetry = _generate_telemetry_data()
    for registered_ip, meta in REGISTRY.items():
        url = "http://{}:{}".format(registered_ip, meta["port"])
        try:
            requests.post(url, json=telemetry)
        except requests.exceptions.RequestException as request_exception:
            logging.warning(
                "Error posting to {} at {}, caused by {}".format(
                    meta["user"], url, request_exception
                )
            )


def _generate_telemetry_data():
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
def register():
    ip_address = request.remote_addr
    payload = request.get_json(silent=True)

    REGISTRY[ip_address] = {"user": payload["username"], "port": payload["port"]}
    logging.info("registered user {} at: {}".format(payload["username"], ip_address))
    return "Registering {} with IP Address {} and port {}".format(
        payload["username"], ip_address, payload["port"]
    )


@app.route("/deregister", methods=["GET", "POST"])
def deregister():
    try:
        REGISTRY.pop(request.remote_addr)
        return "Deregistered {}".format(request.remote_addr)
    except KeyError as keyerror:
        return "{} has no registered containers.".format(request.remote_addr), 404


if __name__ == "__main__":

    app.run(host="0.0.0.0")
