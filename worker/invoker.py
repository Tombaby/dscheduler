#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

import importlib
from worker import JobWorker
import time

if __name__ == '__main__':
    m = importlib.import_module("job.jobconf")
    jobconfs = m.getJobConf()
    workers = {}
    for jobconf in jobconfs:
        m = importlib.import_module(jobconf['module'])
        workers[jobconf['jobName']]=JobWorker(name=jobconf['jobName'],worker=getattr(m, jobconf['entryMethod']), args=jobconf['arguments'])

    for k, p in workers.items():
        p.run()

    running = True;
    while running:
        running = False
        time.sleep(5)
        print 'runing'
        for k, p in workers.items():
            if p.status():
                running = True

