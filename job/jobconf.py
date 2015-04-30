#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

def getJobConf():
    return [
        {'jobName':'Test Job1', 'module':'job.job1', 'entryMethod':'start', 'packagePath':None, 'arguments':'---job1---'},
        {'jobName':'Test Job2', 'module':'job.job2', 'entryMethod':'start', 'packagePath':None, 'arguments':'---job2---'}
    ]