# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DvsPortJoinPortgroupEvent(vim, *args, **kwargs):
    '''A port was moved into the distributed virtual portgroup.'''
    
    obj = vim.client.factory.create('ns0:DvsPortJoinPortgroupEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'chainId', 'portgroupKey', 'portgroupName', 'portKey' ]
    inherited = [ 'changeTag', 'computeResource', 'createdTime', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'key', 'net', 'userName', 'vm' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    