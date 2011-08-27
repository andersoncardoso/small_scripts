#! /usr/bin/env python

import markdown
import sys, os

__author__ = 'Anderson Pierre Cardoso'
__license__ = 'MIT'

def parse_markdown(f, root):
    """
    This function parses a  markdown file.
    Args: 
        f = file name
        root = root folder for the given file
    """
    out = os.path.join(root, f[:f.rindex('.')] + '.html')
    inp = os.path.join(root, f)
    print 'parsing %s' % (f)
    markdown.markdownFromFile(input=inp, output=out)

def path_walker(raiz):
    """
    Walks the path tree from a given root folder,
    and parses every file that ends with .markdwon or .md
    """
    for root,dirs,files in os.walk(raiz):
        [parse_markdown(f, root) for f in files if '.md' in f or '.markdown' in f]
    print('finished path walking =]')
                
    
if __name__=='__main__':
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print >> sys.stderr, '\nOps, pass a valid root folder (of your project) as argument'
        exit()

    raiz = os.path.join(os.getcwd(), sys.argv[1])
    print('root folder is %s' % (raiz))

    path_walker(raiz)
