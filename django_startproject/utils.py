import os
import re
import shutil
import stat
from random import choice


def copy_template(src, dest, replace=None):
    """
    Copy all files in the source path to the destination path.
    
    To replace boilerplate strings in the source data, pass a dictionary to the
    ``replace`` argument where each key is the boilerplate string and the
    corresponding value is the string which should replace it.
    
    The destination file paths are also parsed through the boilerplate
    replacements, so directories and file names may also be modified.
    
    """
    for path, dirs, files in os.walk(src):
        relative_path = path[len(src):].lstrip(os.sep)
        # Replace boilerplate strings in destination directory.
        for old_val, new_val in replace.items():
            relative_path = relative_path.replace(old_val, new_val)
        os.mkdir(os.path.join(dest, relative_path))
        for i, subdir in enumerate(dirs):
            if subdir.startswith('.'):
                del dirs[i]
        for filename in files:
            if (filename.startswith('.startproject') or
                filename.endswith('.pyc')):
                continue
            src_file_path = os.path.join(path, filename)
            # Replace boilerplate strings in destination filename.
            for old_val, new_val in replace.items():
                filename = filename.replace(old_val, new_val)
            dest_file_path = os.path.join(dest, relative_path, filename)
            copy_template_file(src_file_path, dest_file_path, replace)


def copy_template_file(src, dest, replace=None):
    """
    Copy a source file to a new destination file.
    
    To replace boilerplate strings in the source data, pass a dictionary to the
    ``replace`` argument where each key is the boilerplate string and the
    corresponding value is the string which should replace it.
    
    """
    replace = replace or {}
    # Read the data from the source file.
    src_file = open(src, 'r')
    data = src_file.read()
    src_file.close()
    # Replace boilerplate strings.
    for old_val, new_val in replace.items():
        data = data.replace(old_val, new_val)

    # Generate SECRET_KEY for settings file
    secret_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    data = re.sub(r"(?<=SECRET_KEY = ')'", secret_key + "'", data)

    # Write the data to the destination file.
    dest_file = open(dest, 'w')
    dest_file.write(data)
    dest_file.close()
    # Copy permissions from source file.
    shutil.copymode(src, dest)
    # Make new file writable.
    if os.access(dest, os.W_OK):
        st = os.stat(dest)
        new_permissions = stat.S_IMODE(st.st_mode) | stat.S_IWUSR
        os.chmod(dest, new_permissions)


def get_boilerplate(path, project_name):
    """
    Look for a ``.startproject_boilerplate`` file the given path and parse it.
    
    Return a list of 3-part tuples, each containing a boilerplate variable,
    optional description and default value.
    
    If no file was found (or no lines contained boilerplate variables), return
    an empty list.
    
    """
    defaults = {}
    defaults_path = os.path.join(path, '.startproject_defaults')
    if os.path.isfile(defaults_path):
        defaults_file = open(defaults_path, 'r')
        for line in defaults_file:
            match = re.match(r'\s*(\w+)\s*(.*)$', line)
            if match:
                var, default = match.groups()
                defaults[var] = default
    boilerplate = []
    boilerplate_path = os.path.join(path, '.startproject_boilerplate')
    if os.path.isfile(boilerplate_path):
        boilerplate_file = open(boilerplate_path, 'r')
        for line in boilerplate_file:
            match = re.match(r'\s*(\w+)\s*(.*)$', line)
            if match:
                var, description = match.groups()
                default = defaults.get(var)
                boilerplate.append((var, description, default))
    return boilerplate
