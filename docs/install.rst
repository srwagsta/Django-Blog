Install
=========

Install Docker Daemon for `mac`_ or `windows`_.

Start the Docker Daemon using the Docker application.

Pull the Docker images of the django container and postgres container using::
    $ docker pull srwagsta/infost691_django_blog:crits_blog_local_django
    $ docker pull srwagsta/infost691_django_blog:crits_blog_production_postgres

Build the container using::
    $ docker-compose -f local.yml build

Start the container using::
    $ docker-compose -f local.yml up

At this point the application can be reached at 0.0.0.0:8000

For local testing and development please build and run the included local.yml docker configuration file

Any management commands run through the Docker instance::

    $ docker-compose -f local.yml run --rm django python manage.py migrate

.. _`mac`: https://docs.docker.com/docker-for-mac/install/
.. _`windows`: https://docs.docker.com/docker-for-windows/install/

Testing user credentials:
^^^^^^^^^^^^^^^^^^^^^^^^

========     ===========
username     password
--------     -----------
ktrainor     PythonAnywhere
ewatson      GraduatingSoon
swagstaff    MilwaukeeMadness
adminUser    SOISsecret
========     ===========
