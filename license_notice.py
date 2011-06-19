#! /usr/bin/env python
# -*- coding: utf-8

import os
import sys

__author__ = 'Anderson Pierre Cardoso <apierre.cardoso@gmail.com>'

file_extension = '.java'
license_notice = """
/*******************************************************************************
 * Copyright 2011 Zappiens.br
 * Este arquivo é parte do programa Zappiens.br - Portal Web de
 * Distribuição de Vídeo
 *
 * Este programa é um software livre; você pode redistribui-lo e/ou
 * modifica-lo dentro dos termos da Licença Pública Geral GNU como
 * publicada pela Fundação do Software Livre (FSF); na versão 2 da Licença,
 * ou (na sua opinião) qualquer versão posterior.
 *
 * Este programa é distribuido na esperança que possa ser  util, mas
 * SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
 * MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a Licença Pública Geral GNU para
 * maiores detalhes.
 * Você deve ter recebido uma cópia da Licença Pública Geral GNU, sob o
 * título "LICENCA.txt", junto com este programa, se não, escreva para a
 * Fundação do Software Livre(FSF) Inc., 51 Franklin St, Fifth Floor,
 * Boston, MA  02110-1301  USA
 ******************************************************************************/

"""

def prepend_license(file_path):
    """
    prepends the license notice into a file
    """
    print 'adding license to file: %s'%file_path
    with open(file_path, 'r+') as f:
        old = f.read()
        f.seek(0)
        f.write(license_notice + old)

def path_walker(raiz):
    for root,dirs,files in os.walk(raiz):
        [prepend_license(os.path.join(root,f)) for f in files if f.endswith(file_extension)]
    print 'finished path walking =]'
                
    
if __name__=='__main__':
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print >> sys.stderr, '\nOps, pass a valid root folder (of your project) as argument'
        exit()

    raiz = os.path.join(os.getcwd(), sys.argv[1])
    print 'root folder is %s'%(raiz)

    path_walker(raiz)
    
