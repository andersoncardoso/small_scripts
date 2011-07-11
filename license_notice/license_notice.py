#! /usr/bin/env python
# -*- coding: utf-8

import os
import sys

__author__ = 'Anderson Pierre Cardoso <apierre.cardoso@gmail.com>'

class Licensing:
    
    def __init__(self, license_notice, root_folder):
        self.license_notice = license_notice
        self.root_folder = root_folder
        self.file_extension = '.java'
    
    def prepend_license(self, file_path):
        """
        prepends the license notice into a file
        """
        print 'adding license to file: %s'%file_path
        with open(file_path, 'r+') as f:
            old = f.read()
            f.seek(0)
            f.write(self.license_notice + old)

    def path_walker(self):
        for root,dirs,files in os.walk(self.root_folder):
            [self.prepend_license(os.path.join(root,f)) for f in files if f.endswith(self.file_extension)]
        print 'finished path walking =]'
                
    
if __name__=='__main__':
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print >> sys.stderr, '\nOps, pass a root folder and a (optional) notice text file'
        exit()

    root_folder = os.path.join(os.getcwd(), sys.argv[1])
    print 'root folder is %s'%(root_folder)

    license_file_name = sys.argv[2] if len(sys.argv) >2 else "gpl.notice"
    license_notice = open(license_file_name, "r").read()
    
    lic = Licensing(license_notice, root_folder)
    lic.path_walker()
    
