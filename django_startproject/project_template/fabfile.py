from fabric.api import env, local, run, require

env.disable_known_hosts = True # always fails for me without this
env.hosts = ['myproject.mydevhost']
env.root = '/opt/webapps/myproject'
env.proj_root = env.root + '/src/myproject'
env.pip_file = env.proj_root + '/requirements.pip'


def deploy():
    """Update source, update pip requirements, syncdb, restart server"""
    update()
    update_reqs()
    syncdb()
    restart()


def switch(branch):
    """Switch the repo branch which the server is using"""
    ve_run('cd %s; git checkout %s' % (env.proj_root, branch))
    restart()


def version():
    """Show last commit to repo on server"""
    print sshagent_run('cd %s; git log -1' % env.proj_root)


def restart():
    """Restart Apache process"""
    run('touch %s/etc/apache/django.wsgi' % env.root)


def update_reqs():
    """Update pip requirements"""
    ve_run('yes w | pip install -r %s' % env.pip_file)


def update():
    """Updates project source"""
    print sshagent_run('cd %s; git pull' % env.proj_root)


def syncdb():
    """Run syncdb (along with any pending south migrations)"""
    ve_run('manage.py syncdb --migrate')


def ve_run(cmd):
    """
    Helper function.
    Runs a command using the virtualenv environment
    """
    require('root')
    return sshagent_run('source %s/bin/activate; %s' % (env.root, cmd))


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
