========================
PyLadies Docker Workshop
========================

Welcome, PyLadies! 🐍 🌈

The purpose of this workshop is to provide an interactive introduction to `Docker`_.

This repository is comprised of two parts: a client_ skeleton and a server_. Your
task here is to complete the client and to containerize it.

Prerequisites
=============

- Docker
- Python 3.7
- Git

Server
======

There is a server running on a Raspberry Pi which is reading environmental metrics (such as
temperature, humidity), and sending metrics to registered clients.

Documentation for the server is found in the `server directory`_.

Client
======

There is a skeleton client which must be completed and dockerised. The client should register with
the server to receives metrics data. Upon termination, the client should deregister.

Documentation for the client is found in the `client directory`_.


.. _Docker: https://www.docker.com/
.. _client: ./client/README.rst
.. _server: ./server/README.rst
.. _server directory: ./server/README.rst
.. _client directory: ./client/README.rst
