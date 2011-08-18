# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DiskChangeInfo(vim, *args, **kwargs):
    '''Data structure to describe areas in a disk associated with this VM that have
    been modified since a well-defined point in the past. Returned by
    QueryChangedDiskAreas. This data structure describes a subset of the disk
    identified by startOffset and length. All areas that have been modified within
    this interval are listed under changedArea.'''
    
    obj = vim.client.factory.create('ns0:DiskChangeInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'changedArea', 'length', 'startOffset' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    