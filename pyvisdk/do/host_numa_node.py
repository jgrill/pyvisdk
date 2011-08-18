# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNumaNode(vim, *args, **kwargs):
    '''Information about a single NUMA node.NOTE: This data object is not modeled
    correctly if the NUMA node contains multiple disjoint memory ranges. If there
    are multiple memory ranges, the client will see one memory ranges from this
    NumaNode object, and the memory range may or may not belong to this NUMA node.'''
    
    obj = vim.client.factory.create('ns0:HostNumaNode')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'cpuID', 'memoryRangeBegin', 'memoryRangeLength', 'typeId' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    