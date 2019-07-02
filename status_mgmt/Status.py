#!/usr/bin/env python3
import json
import os, sys
from pprint import pprint, pformat
from copy import deepcopy
import collections
#  Date/Time imports
from datetime import date, timedelta
import datetime as dz
from dateutil import tz
import time as tm
import glob
"""
Purpose:  General status management class so the information can 
be passed around safely between routines and used within education Colaboratory scripts

This is written as a MutableMapping so that it acts like a dictionary with additional
features for tracking the number of times cells are run, naming cells, etc.

As with most of these type capabilities to output status, there will be a minor language
to have reasonable 
"""
class Status(collections.MutableMapping):
    """The class for managing the status information

    This application requires a good bit of input because I prefer not
    deriving information from the current location of a computer.

    """
    def __init__(self):
        #check for required fields
        self.cells = dict()
        self.run_order = []
        self.run_number = 0
    #
    def __kill_processing__(self,msg):
        print("STOP PROCESSING: {}".format(msg))
        sys.exit(1)
    # 
    # def state(self):
    #     cfg = deepcopy(self.conf)
    #     return cfg
    # #  Overloads so that it acts kinda like a dictionary
    def __getitem__(self,key) -> str:
        try:
            w_key = self.__valid_key__(key)
            try:
                return self.cells[w_key]
            except:
                return None
        except Exception as e:
            print(e)
            pass
    def update(self,key):
        assert isinstance(key,int)
        self[key] = key

    def __setitem__(self,key,value):
        try:
            w_key = self.__valid_key__(key)
            if w_key not in self.cells:
                self.cells[w_key] = value
            self.run_order.append({w_key:self.run_number})
            self.run_number += 1

        except ValueError as e:
            raise ValueError(e)

    def __delitem__(self,key:str):
        del self.cells[key]
    def __len__(self):
        return len(self.cells)
    def __iter__(self):
        return iter(self.cells)
    def __repr__(self):
        return pformat(self.cells())
    def __valid_key__(self,key):
        return str(key).lower().strip()
    def iter_run_order(self):
        return iter(self.run_order)
    def format_run_order(self):
        return pformat(self.run_order)
    