import os
import requests
from flask import Flask, request


app = Flask(__name__)


def _register_with_server(username: str, server_addr: str, port: int):
    requests.post(f"{server_addr}/register", json={"username": username, "port": port})


def _deregister(username: str, server_addr: str, port: int):
    requests.post(
        f"{server_addr}/deregister", json={"username": username, "port": port}
    )


@app.route("/", methods=["POST"])
def listener():
    payload = request.get_json(silent=True)
    print(payload)
    return f"Received!"


def main():
    server = os.environ.get("SERVER", "http://127.0.0.1:5000")
    name = os.environ.get("USERNAME", "Mysterious PyLady")
    port = os.environ.get("PORT", 65432)
    try:
        _register_with_server(username=name, server_addr=server, port=port)
        app.run(host="0.0.0.0", port=port)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error: {e}")
    finally:
        _deregister(username=name, server_addr=server, port=port)


if __name__ == "__main__":
    main()
