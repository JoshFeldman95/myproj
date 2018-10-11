#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:49:17 2018

@author: joshfeldman
"""
import numpy as np

class Complex(object):
    """A complex number
    
    Attributes:
        real (float): the real part
        complex (float): the complex part
    
    """
    
    def __init__(self, r , c):
        """Form a complex number
        args:
            r (float): the real part
            c (float): the complex moart
        """
        self.real = r
        self.complex = c
    
    def conjugate(self):
        """returns the complex conjugate"""
        return Complex(self.real, -self.complex)
    
    def magnitude(self):
        """returns the magnitude"""
        return np.sqrt(self.real**2+self.complex**2)
    
    def angle(self):
        """returns the angle/argument"""
        if self.real > 0:
            if self.complex > 0:
                return np.arctan(self.complex/self.real)
            if self.complex < 0:
                return np.arctan(self.complex/self.real) + 2*np.pi
            if self.complex == 0:
                return 0
        if self.real < 0:
            if self.complex > 0:
                return np.arctan(self.complex/self.real) + np.pi
            if self.complex < 0:
                return np.arctan(self.complex/self.real) + np.pi
            if self.complex == 0:
                return np.pi
        if self.real == 0:
            if self.complex > 0:
                return np.pi/2
            if self.complex < 0:
                return 3*np.pi/2
            if self.complex == 0:
                return None
    
    def __add__(self, other):
        try:
            return Complex(self.real + other.real, self.complex + other.complex)
        except AttributeError:
            return Complex(self.real + other.real, self.complex)
    
    def __radd__(self, other):
        try:
            return Complex(self.real + other.real, self.complex + other.complex)
        except AttributeError:
            return Complex(self.real + other.real, self.complex)
    
    def __repr__(self):
        return "{} + {}i".format(self.real, self.complex)
    
    def __eq__(self, other):
        real_part_match = self.real == other.real
        complex_part_match = self.complex == other.complex
        return real_part_match and complex_part_match