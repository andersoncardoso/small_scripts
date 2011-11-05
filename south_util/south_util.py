#! /usr/bin/env python
# -*- coding: utf-8 _-*-

import sys
import subprocess
import time

APP_LIST = ['your','apps','go', 'here'] 

SETTINGS = '--settings=development'

ERR_MSG="""
Please pass one of these options as argument: 
build         : builds initial migration from scratch (should run only once)
initial       : recreates db, syncs it and migrates all data
new_app       : for new apps
normal        : normal workflow migration (default)
one_app <app> : schema migration for only one app

"""

def remove_db():
    print(u'removing old db')
    # This is usefull only on our project structure (using a sqlite for dev)
    # change for your specific db/structure
    subprocess.Pope(['rm', '../db/dev.db'])

def syncdb():  
    print(u'syncing db')
    subprocess.call(['./manage.py',  'syncdb', '--noinput',\
                    SETTINGS])
                    
def app_schemamigration(app, initial=False):
    print(u'[{}] schemamigration'.format(app))
    subprocess.call(
        ['./manage.py','schemamigration',app,
         '--initial' if initial else '--auto', SETTINGS]) 
    
def schemamigration(*args):
    [app_schemamigration(app) for app in APP_LIST]

def schemamigration_initial(*args):
    [app_schemamigration(app, initial=True) for app in APP_LIST]

def app_migrate(app, fake=False):
    print(u'[{}] migrate'.format(app))
    subprocess.call(
        ['./manage.py','migrate',app,'--fake' if fake else '',SETTINGS]) 

def migrate(*args):
    [app_migrate(app) for app in APP_LIST]

def migrate_fake(*args):
    [app_migrate(app,fake=True) for app in APP_LIST]

def run_cmd(opt):
    try:
        routines = {
            'build' : [remove_db, syncdb, schemamigration_initial, migrate_fake],
            'initial': [remove_db, syncdb, migrate],
            'new_app' : [schemamigration_initial, migrate],
            'normal': [schemamigration, migrate],
            'one_app': [app_schemamigration, app_migrate],
        }
        arg = sys.argv[2] if opt == 'one_app' else None
        [cmd(arg) for cmd in routines[opt]]
    except Exception as err:
        print(u'Ops, invalid option : {} \n{}'.format(opt, err))
        print(ERR_MSG)
    
def main():
    opt = sys.argv[1] if len(sys.argv) > 1 else 'normal'
    if '--help' in sys.argv:
        print(ERR_MSG)
        sys.exit(1)
    run_cmd(opt)

if __name__ == '__main__':
    main()
