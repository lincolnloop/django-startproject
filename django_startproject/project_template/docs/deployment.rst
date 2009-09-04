Deployment
==========

Staging/Development
-------------------

`Fabric <http://pypi.python.org/pypi/Fabric>`_ is used to allow developers to
easily push changes to a previously setup development/staging environment.
To get started, run the following command from within your virtual environment::

    pip install -e git://fabfile.org/fabric.git@0.9b1#egg=fabric
    fab --fabfile src/myproject/fabfile.py -l

This will install Fabric and provide a list of available commands.
    