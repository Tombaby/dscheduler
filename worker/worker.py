#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from multiprocessing import Process

class JobWorker(object):

    def __init__(self, name=None, worker=None, args=None):
        self.name = name
        self.worker = worker
        self.args = args
        self.process = Process(target=self.worker, name=self.name, args=(self.args,))
        self.process.daemon = True


    def run(self, async=False):
        self.process.start()
        if async:
            self.process.join()


    def status(self):
        if self.process.is_alive():
            print 'working'
            return True
        else:
            print 'done'
            return False
