import logging
from time import sleep
from recorddetail_tng import RecordDetail

# need the logging setup before we use the decorator otherwise we cant see what happens
logging.basicConfig(level=logging.INFO)


LOG = logging.getLogger(__name__)


@RecordDetail(exclude=['run'])
class MyProcess():

    def __init__(self,):
        self.numbers = list(range(0, 10))

    def step_one(self, detail):
        LOG.info('Doing step one')
        self.numbers = [n + 2 for n in self.numbers]

    def step_two(self, detail):
        LOG.info('Doing step two')
        detail.name = 'fooo baaa'
        self.numbers = [n * 2 for n in self.numbers]
        sleep(1)

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
    process = MyProcess()
    process.run()
