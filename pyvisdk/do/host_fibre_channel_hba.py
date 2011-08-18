# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFibreChannelHba(vim, *args, **kwargs):
    '''This data object type describes the Fibre Channel host bus adapter.'''
    
    obj = vim.client.factory.create('ns0:HostFibreChannelHba')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))
        
    signature = [ 'bus', 'device', 'nodeWorldWideName', 'portType', 'portWorldWideName', 'speed' ]
    inherited = [ 'driver', 'key', 'model', 'pci', 'status' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    