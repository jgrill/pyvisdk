# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostProxySwitch(vim, *args, **kwargs):
    '''The HostProxySwitch is a software entity which represents the component of a
    DistributedVirtualSwitch on a particular host.'''
    
    obj = vim.client.factory.create('ns0:HostProxySwitch')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'dvsName', 'dvsUuid', 'key' ]
    inherited = [ 'mtu', 'numPorts', 'numPortsAvailable', 'pnic', 'spec', 'uplinkPort' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    