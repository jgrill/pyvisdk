# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskDimensionsLba(vim, *args, **kwargs):
    '''This data object type describes the logical block addressing system that uses
    block numbers and block sizes to refer to a block. This scheme is employed by
    SCSI. If a SCSI disk is not involved, then blockSize is 512 bytes.'''
    
    obj = vim.client.factory.create('ns0:HostDiskDimensionsLba')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'block', 'blockSize' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    