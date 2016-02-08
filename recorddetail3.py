import datetime
from contextlib import contextmanager
import logging

LOG = logging.getLogger(__name__)


class RecordDetail(object):

    def __init__(self, name):
        self.name = name
        self.status = None
        self.start_time = datetime.datetime.now()
        self.stop_time = None
        self.number_of_records = None
        self.other_details = None

    def save(self,):
        # Do stuff to write to database
        LOG.info('saving %s ', self)

    def __str__(self):
        return ('name: %s start: %s stop : %s' % (self.name, self.start_time, self.stop_time))

    def stop(self, status):
        LOG.info('stopping')
        self.status = status
        self.stop_time = datetime.datetime.now()
        self.save()


@contextmanager
def record_detail(name):
    detail = RecordDetail(name)
    detail.save()
    yield detail
    detail.stop(0)
