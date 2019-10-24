from builtins import KeyError

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

REGISTRY = {}


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
    print("registered users: {}".format(REGISTRY))
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
