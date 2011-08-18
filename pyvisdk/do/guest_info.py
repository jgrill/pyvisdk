# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def GuestInfo(vim, *args, **kwargs):
    '''Information about the guest operating system.Most of this information is
    collected by VMware Tools. In general, be sure you have VMware Tools installed
    and that the virtual machine is running when you access this information.'''
    
    obj = vim.client.factory.create('ns0:GuestInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'appHeartbeatStatus', 'disk', 'guestFamily', 'guestFullName', 'guestId',
        'guestState', 'hostName', 'ipAddress', 'ipStack', 'net', 'screen',
        'toolsRunningStatus', 'toolsStatus', 'toolsVersion', 'toolsVersionStatus' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    