# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfCounterInfo(vim, *args, **kwargs):
    '''This data object type contains metadata for a performance counter. See
    PerformanceManager for definitions of available counters.'''
    
    obj = vim.client.factory.create('ns0:PerfCounterInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'associatedCounterId', 'groupInfo', 'key', 'level', 'nameInfo',
        'perDeviceLevel', 'rollupType', 'statsType', 'unitInfo' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    