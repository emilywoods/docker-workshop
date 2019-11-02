import os
import requests
from flask import Flask, request


app = Flask(__name__)


def _get_env_variables():
    """Step 2

    Replace `???` with the **name** of environment variables which will be
    provided to the client. Typically system environment variables are all uppercase,
    e.g. ``USERNAME``.

    If these variables are not set, defaults have been provided for each.
    """

    server = os.environ.get(???, "http://127.0.0.1:5000")
    name = os.environ.get(???, "It's me - anonymous PyLady")
    port = os.environ.get(???, 65432)
    return name, port, server


def _register_with_server(username: str, server_addr: str, port: int):
    """Step 3

    Make a POST request to the `/register` endpoint of the server,
    and provide a json body with fields "username" and "port".

    The server address contains the protocol and port e.g. http://127.0.0.1:5000
    so these don't need to be added.
    """
    pass


def _deregister(username: str, server_addr: str, port: int):
    """Step 4

    Make a POST request to the `/deregister` endpoint of the server,
    and provide a json body with fields "username" and "port".
    """
    pass

@app.route("/", methods=["POST"])
def client():
    """
    The client runs on the specified port while the server POSTS
    metrics data to it. The metrics data is printed to the console.
    """

    payload = request.get_json(silent=True)
    print(payload)
    return f"Received!"


def main():
    name, port, server = _get_env_variables()
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
