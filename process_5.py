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
from recorddetail5 import RecordDetail

LOG = logging.getLogger(__name__)


class MyProcess():

    def __init__(self,):
        self.numbers = list(range(0, 10))

    @RecordDetail()
    def step_one(self, detail):
        LOG.info('Doing step one')
        self.numbers = [n + 2 for n in self.numbers]

    @RecordDetail()
    def step_two(self, detail):
        LOG.info('Doing step two')
        detail.name = 'fooo baaa'
        self.numbers = [n * 2 for n in self.numbers]
        sleep(1)

    @RecordDetail('three')
    def step_three(self, detail):
        LOG.info('Doing step three')
        self.numbers = [n / (n - 4) for n in self.numbers]

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
