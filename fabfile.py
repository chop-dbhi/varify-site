from fabric.api import *

env.hosts = ['varify.chop.edu']

def deploy():
    with cd('/home/devuser/webapps/varify-site-static'):
        run('git pull')
        run('git submodule update --init')
        run('jekyll build')
