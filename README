============
StartProject
============

StartProject installs a script which allows the easy creation of a standard
Django project layout based on Lincoln Loop standards.


Script usage
============

After installing StartProject, simply run the following command (from within
the directory in where the new project directory should be created)::

	django-startproject.py project_name

The script will prompt for values to replace boilerplate variables with. These
variables allow for both the file contents and path names to be customized to
this specific project.


Using a custom project template
===============================

If you would prefer to use a custom project template than the one included in
this application, create your custom project template directory and call the
command script like this::

    django-startproject.py --template-dir=/your/custom/template project_name


Specifying boilerplate variables
--------------------------------

Two optional files in the root of the project template directory are used to
determine the boilerplate variables:

``.startproject_boilerplate``
	Each line should contain the boilerplate variable (and optionally, a
	description of the variable, separated from the variable by white space).

``.startproject_defaults``
	Each line should contain a variable and the default value, separated by
	whitespace. If the default value contains ``PROJECT``, it is replaced with
	the project name.

See the files included in the project_template directory of StartProject for
an example.
