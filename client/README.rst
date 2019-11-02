======
Client
======

The purpose of this service to register with the server and receive metrics data from it.
Upon termination the client should deregister.

Workshop
========

This project requires Python 3.7 or greater.
All of the python dependencies are included in the ``setup.py`` file and no additional
dependencies should be required.

Complete the client
-------------------

1. Install the application and its dependencies with::

    $ make install

2. Allow the client to accept environment variables.

3. Enable the client to register with the server. The server endpoints and how to use them
   are documented in the `server README`_.

4. Enable the client to de-register with the server.

Complete the Dockerfile
-----------------------

5. Choose a base image

6. Add your project files

7. Install project with pip

8. Configure the ``ENTRYPOINT`` to run the project with environment variables

Run your container
------------------

9. Build the container with a tag::

   $ docker build -t <YOUR-IMAGE-TAG>

10. Run the container::

   $ docker run <PORT>:<PORT> --env SERVER=<SERVER ADDRESS> --env USERNAME=<YOUR USERNAME> --env PORT=<PORT> <YOUR-IMAGE-TAG>

   Note: the environment variable names will be the same as set in step 1. above.

11. Stop the container::

  $ docker stop <YOUR-IMAGE-TAG>

Useful docker commands
======================

List the running docker processes::

  $ docker ps

Connect to running docker container::

  $ docker exec -it <CONTAINER-ID> sh

View the logs of a container::

  $ docker logs <CONTAINER-ID>

.. _server README: ../registry/README.rst
