#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:11:05 2018

@author: joshfeldman
"""
from myproj import module as mod

def test_conjugate():
    assert mod.Complex(1,2).conjugate() ==mod.Complex(1,-2)