Crits Blog
==========

A simple blog for future integration to the crits and coffee website.
Refer to the bottom section for local testing environment setup.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
Built by: `Stephen Wagstaff`_

.. _`Stephen Wagstaff`: https://critsandcoffee.com/

:License: Apache Software License 2.0


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sass CSS compilation is done through a simple management command run through the Docker instance::

    $ docker-compose -f local.yml run --rm django python manage.py compilescss

More information can be found on `django-sass-processor on gitHub`_.

.. _`django-sass-processor on gitHub`: https://github.com/jrief/django-sass-processor



Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

Deployed via an Ubuntu based Docker container. A 'default' and 'editors' user groups must be created for proper deployment.
The default users will have restrictive permissions and the editors will have all blog related permissions. This will change
the view behaviors within the blog app unless the user is the author.


Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html


Local Testing and Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install Docker Daemon for `mac`_ or `windows`_.
Start the Docker Daemon using the Docker application.
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
