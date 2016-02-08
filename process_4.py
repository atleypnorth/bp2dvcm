"""
HeadURL:  $HeadURL$
Last changed by:  $Author$
Last changed on:  $Date$

(c)  2015 BlackRock.  All rights reserved.

Description:

description
"""
__version__ = '$Revision$'


if __name__ == '__main__':
    pass
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
from recorddetail4 import RecordDetail

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)


class MyProcess():

    def __init__(self,):
        self.numbers = list(range(0, 10))

    @RecordDetail('one')
    def step_one(self):
        LOG.info('Doing step one')
        self.numbers = [n + 2 for n in self.numbers]

    @RecordDetail('two')
    def step_two(self):
        LOG.info('Doing step two')
        self.numbers = [n * 2 for n in self.numbers]
        sleep(1)

    @RecordDetail('three')
    def step_three(self):
        LOG.info('Doing step three')
        self.numbers = [(n - 2) / 2 for n in self.numbers]

    def run(self):
        self.step_one()
        LOG.info(self.numbers)
        self.step_two()
        LOG.info(self.numbers)
        self.step_three()
        LOG.info(self.numbers)

if __name__ == '__main__':
    process = MyProcess()
    process.run()
