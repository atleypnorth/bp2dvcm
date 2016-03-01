import datetime
from functools import wraps
from logging import getLogger

LOG = getLogger(__name__)


class RecordDetail(object):
    '''More stuff - trying to see how I could decorate a class or a method ...
    '''

    def __init__(self, name=None, exclude=None):
        LOG.info('__init__')
        self.name = name
        self.status = None
        self.start_time = datetime.datetime.now()
        self.stop_time = None
        self.number_of_records = None
        self.other_details = None
        if exclude is None:
            exclude = []
        self.exclude = exclude

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

    def _wrap_function(self, func):
        LOG.info('wrapping function %s', func)
        if self.name is None:
            self.name = func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            status = 0
            # Need to set this now when the function is called, not when the decorator is evaluated
            self.start_time = datetime.datetime.now()
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

    def _wrap_class_functions(self, klass):
        LOG.info('wrapping class %s', klass)
        for attr_name in dir(klass):
            LOG.info('attribute %s', attr_name)
            attr_value = getattr(klass, attr_name)
            if (not attr_name.startswith('_')) and callable(attr_value) and attr_name not in self.exclude:
                setattr(klass, attr_name, self._wrap_function(attr_value))
        return klass

    def __call__(self, something):
        LOG.info(something)
        if isinstance(something, type):
            return self._wrap_class_functions(something)
        if callable(something):
            return self._wrap_function(something)

