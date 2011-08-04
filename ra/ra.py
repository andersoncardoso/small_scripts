#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import os
from pprint import pprint
from Tkinter import *
from tkFileDialog import askopenfilename

def load_data(filename):
    with open(filename) as f:
        #eliminate lines without data
        [ f.readline() for i in xrange(3)]
        
        #data parsing
        data = {'time':[], 'n':[],'sensor1':[], 'sensor2':[], 
                'sensor3':[], 'sensor4':[]}
        for line in f :
            l = line.split()
            t = float(l[0].replace(',', '.'))
            if  t >= 0:
                data['time'].append(t)
                data['n'].append(int(l[1]))
                for i in xrange(4):
                    data['sensor'+str(i+1)].append(int(l[i+2]))
                
        return data

def get_sensor_data(data, ind):
    return (data['sensor1'][ind],data['sensor2'][ind],data['sensor3'][ind],data['sensor4'][ind])

def analize_data(filename, data, texp, trec, num_exposicoes):
    with open(filename[:filename.find(".txt")]+"_output.txt", "w") as f:
        for i in xrange(num_exposicoes):
            l = [get_sensor_data(data, ind) for ind,t in enumerate(data['time']) \
                 if (t >= i*(trec+texp) and t < (i+1)*(trec+texp))]
            value = []
            for j in xrange(4):
                lista = [v[j] for v in l]
                max_val = max(lista)
                min_val = min(lista)
                value.append(float(max_val - min_val)/min_val)
            #print 'ciclo %2d -> '%(i+1), 
            for vl in value: f.write(str('%.3f  ' % vl).replace('.',','))
            f.write('\n')
            
    
def get_entry(filename):
    with open(filename,"r") as f:
        f.readline()
        s = f.readline()
        num_exp, texp, trec = [int(x) for x in s.split() if x.isdigit()]
    return texp,trec,num_exp
    
def main(filename):
    entrys= get_entry(filename)
    data = load_data(filename)
    analize_data(filename, data, *entrys)
        
if __name__ == '__main__':
    root = Tk()
    filename = askopenfilename(filetypes=[("all files","*"), ("text files", "*.txt")])
    main(filename)
    
