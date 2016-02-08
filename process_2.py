"""
HeadURL:  $HeadURL$
Last changed by:  $Author$
Last changed on:  $Date$

(c)  2015 BlackRock.  All rights reserved.

Description:

description
"""
__version__ = '$Revision$'

import logging
from time import sleep
from recorddetail import RecordDetail

LOG = logging.getLogger(__name__)


class MyProcess():

    def __init__(self,):
        self.numbers = list(range(0, 10))

    def step_one(self):
        detail = RecordDetail('one')
        LOG.info('Doing step one')
        self.numbers = [n + 2 for n in self.numbers]
        detail.stop(0)

    def step_two(self):
        detail = RecordDetail('two')
        LOG.info('Doing step two')
        self.numbers = [n * 2 for n in self.numbers]
        sleep(1)
        detail.stop(0)

    def step_three(self):
        detail = RecordDetail('three')
        LOG.info('Doing step three')
        self.numbers = [(n - 2) / 2 for n in self.numbers]
        detail.stop(0)

    def run(self):
        self.step_one()
        LOG.info(self.numbers)
        self.step_two()
        LOG.info(self.numbers)
        self.step_three()
        LOG.info(self.numbers)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    process = MyProcess()
    process.run()
