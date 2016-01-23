"""
HeadURL:  $HeadURL$
Last changed by:  $Author$
Last changed on:  $Date$

(c)  2015 BlackRock.  All rights reserved.
"""
__version__ = '$Revision$'

import datetime
from logging import getLogger
from functools import wraps

LOG = getLogger(__name__)


class RecordDetail(object):

    def __init__(self, name=None):
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
        return ('name: %s start: %s stop : %s status : %d' % (self.name, self.start_time,
                                                              self.stop_time, self.status))

    def stop(self, status):
        LOG.info('stopping')
        self.status = status
        self.stop_time = datetime.datetime.now()
        self.save()

    def __call__(self, func):
        if self.name is None:
            self.name = func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            status = 0
            try:
                args += (self,)
                result = func(*args, **kwargs)
            except Exception:
                status = -1
                raise
            finally:
                self.stop(status)
            return result
        return wrapper
