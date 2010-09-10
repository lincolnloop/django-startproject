==================
Installation
==================

Pre-Requisites
===============

* `setuptools <http://pypi.python.org/pypi/setuptools>`_
* `virtualenv <http://pypi.python.org/pypi/virtualenv>`_

To install all of these system dependencies on a Debian-based system, run::

	sudo apt-get install python-setuptools
	sudo easy_install virtualenv

System Dependencies
===================

* Python Imaging Library

To install all of these system dependencies on a Debian-based system, run::

	sudo apt-get install python-imaging


Creating the Virtual Environment
================================

First, create a clean base environment using virtualenv::

    virtualenv myproject
    cd myproject
    source bin/activate
    easy_install pip


Installing the Project
======================

If you have the project source checked out already, place it in a ``myproject``
directory inside the virtual environment source (``src``) directory. 
Otherwise, checkout the source now::

    pip install -e git+ssh://git@myrepohost/myproject.git#egg=myproject

Next, install the requirements and the project source::

    pip install -r src/myproject/requirements.pip


Configuring a Local Environment
===============================

If you're just checking the project out locally, you can copy some example
configuration files to get started quickly::

    cp conf/local/example/* conf/local
    manage.py syncdb


Building Documentation
======================

Documentation is available in ``docs`` and can be built into a number of 
formats using `Sphinx <http://pypi.python.org/pypi/Sphinx>`_. To get started::

    pip install Sphinx
    cd docs
    make html

This creates the documentation in HTML format at ``docs/_build/html``.
