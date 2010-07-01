from fabric.api import *

env.disable_known_hosts = True # always fails for me without this
env.hosts = ['myproject.mydevhost']
env.root = '/opt/webapps/myproject'
env.proj_root = env.root + '/src/myproject'
env.pip_file = env.proj_root + '/requirements.pip'

def update():
    """Update source, update pip requirements, syncdb, restart server"""
    update_proj()
    update_reqs()
    migrate()
    syncdb()
    restart()

def push():
    """
    Update source and restart

    This is similar to `update` but it does not update all the requirements
    and does not execute migrations. Perfect for minor changes.
    """
    local('git push') # TODO: use an explicit branch here?
    update_proj()
    restart()

def version():
    """Show last commit to repo on server"""
    sshagent_run('cd %s; git log -1' % env.proj_root)

def restart():
    """Restart Apache process"""
    run('touch %s/etc/apache/django.wsgi' % env.root)

def update_reqs():
    """Update pip requirements"""
    ve_run('yes w | pip install -E %s -r %s' % (env.root, env.pip_file))

def update_proj():
    """Updates project source"""
    sshagent_run('cd %s; git pull' % env.proj_root)

def syncdb():
    """Run syncdb"""
    output = ve_run('manage.py syncdb')
    if 'There are unapplied evolutions for ' in output:
         evolve()

def evolve():
    ve_run('manage.py evolve --execute --noinput')

def migrate():
    """Execute south migrations"""
    ve_run('manage.py migrate')

def ve_run(cmd):
    """
    Helper function.
    Runs a command using the virtualenv environment
    """
    require('root')
    return run('source %s/bin/activate; %s' % (env.root, cmd))

def sshagent_run(cmd):
    """
    Helper function.
    Runs a command with SSH agent forwarding enabled.
    
    Note:: Fabric (and paramiko) can't forward your SSH agent. 
    This helper uses your system's ssh to do so.
    """

    for h in env.hosts:
        try:
            host, port = h.split(':')
            local('ssh -p %s -A %s "%s"' % (port, host, cmd))
        except ValueError:
            local('ssh -A %s "%s"' % (h, cmd))
