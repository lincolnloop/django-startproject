import os
import re
import shutil
import stat


def copy_template(src, dest, replace=None):
    """
    Copy all files in the source path to the destination path.
    
    To replace boilerplate strings in the source data, pass a dictionary to the
    ``replace`` argument where each key is the boilerplate string and the
    corresponding value is the string which should replace it.
    
    """
    for path, dirs, files in os.walk(src):
        relative_path = path[len(src):].lstrip('/')
        os.mkdir(os.path.join(dest, relative_path))
        for i, subdir in enumerate(dirs):
            if subdir.startswith('.'):
                del dirs[i]
        for f in files:
            if f.startswith('.startproject') or f.endswith('.pyc'):
                continue
            src_file_path = os.path.join(path, f)
            dest_file_path = os.path.join(dest, relative_path, f)
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


def get_boilerplate(path):
    """
    Look for a ``.startproject_boilerplate`` file the given path and parse it.
    
    Return a 2-tuple list of the boilerplate variables and optional
    descriptions.
    
    If no file was found (or no lines contained boilerplate variables), return
    an empty list.
    
    """
    boilerplate = []
    boilerplate_path = os.path.join(path, '.startproject_boilerplate')
    if os.path.isfile(boilerplate_path):
        boilerplate_file = open(boilerplate_path, 'r')
        for line in boilerplate_file:
            match = re.match(r'\s*(\w+)\s*(.*)$', line)
            if match:
                boilerplate.append(match.groups())
    return boilerplate
