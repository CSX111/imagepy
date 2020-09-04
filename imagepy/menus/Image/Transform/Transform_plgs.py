# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 01:14:50 2016
@author: yxl
"""
import numpy as np
import scipy.ndimage as nimg
from sciapp.action import Filter, Simple
from imagepy.ipyalg.transform

class Rotate(Filter):
    title = 'Rotate'
    note = ['all', 'auto_msk', 'auto_snap','preview']
    para = {'ang':0}
    view = [(float, 'ang', (0,360), 1, 'angle', 'degree')]
        
    def run(self, ips, snap, img, para = None):
        if para == None: para = self.para
        a = para['ang']/180.0*np.pi
        o = np.array(ips.shape)*0.5
        if ips.roi!=None:
            box = ips.roi.box
            o = np.array([box[1]+box[3],box[0]+box[2]])*0.5
        trans = np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
        offset = o-trans.dot(o)
        nimg.affine_transform(snap, trans, output=img, offset=offset)
        
class Scale(Filter):
    title = 'Scale'
    note = ['all', 'auto_msk', 'auto_snap','preview']
    para = {'zoom':1}
    view = [(float, 'zoom', (0.1,10), 1, 'fact', '')]

    def run(self, ips, snap, img, para = None):
        if para == None: para = self.para
        k = 1/para['zoom']
        o = np.array(ips.shape)*0.5
        if ips.roi!=None:
            box = ips.roi.box
            o = np.array([box[1]+box[3],box[0]+box[2]])*0.5
        trans = np.array([[k,0],[0,k]])
        offset = o-trans.dot(o)
        nimg.affine_transform(snap, trans, output=img, offset=offset)
'''
class LinearPolar(Simple):
    title = 'Linear To Polar'
    note = ['all']    
    para = {'slice':False, 'order':1}

    view = [(list, 'con', ['4-Connect','8-Connect'], str, 'Structure', 'connect'),
            (bool, 'slice', 'slice')]
        
    def run(self, ips, imgs, para = None):
        if not para['slice']:  imgs = [ips.img]
        labels = []
        for i in range(len(imgs)):
            labels.append(lab)
        self.app.show_img(labels, ips.title+'-label') 
'''
plgs = [Rotate, Scale]