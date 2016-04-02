import datetime
from contextlib import contextmanager
from logging import getLogger

LOG = getLogger(__name__)


class RecordDetail(object):

    def __init__(self, name):
        self.name = name
        self.status = None
        self.start_time = datetime.datetime.now()
        self.stop_time = None
        self.number_of_records = None
        self.other_details = None
        LOG.info('___INIT__')

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

    def __enter__(self,):
        LOG.info('__ENTER__')
        self.save()
        # Return value is used if you with ... as VAR
        return self

    def __exit__(self, etype, evalue, etrace):
        self.stop(0)
        # rethrow any exception (set to True to swallow it ...)
        return False


@contextmanager
def record_detail(name):
    detail = RecordDetail(name)
    detail.save()
    yield detail
    detail.stop(0)













