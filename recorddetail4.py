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

    def __init__(self, name):
        self.name = name
        self.status = None
        self.start_time = datetime.datetime.now()
        self.stop_time = None
        self.number_of_records = None
        self.other_details = None
        LOG.info('__init__')

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

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Need to set this now when the function is called, not when the decorator is evaluated
            self.start_time = datetime.datetime.now()
            result = func(*args, **kwargs)
            self.stop(0)
            return result
        return wrapper
