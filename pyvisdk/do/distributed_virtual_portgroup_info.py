# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualPortgroupInfo(vim, *args, **kwargs):
    '''This class describes a DistributedVirtualPortgroup that a device backing can be
    attached to.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualPortgroupInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))
        
    signature = [ 'portgroup', 'portgroupKey', 'portgroupName', 'portgroupType', 'switchName',
        'switchUuid', 'uplinkPortgroup' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    