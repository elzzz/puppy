#!/usr/bin/env python

from agent import connect_agent
import sys
sys.dont_write_bytecode = True

try:
    connect_agent()
except:
    print('Closed connection')
