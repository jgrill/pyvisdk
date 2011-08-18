# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFirewallRule(vim, *args, **kwargs):
    '''This data object type describes a port (or range of ports), identified by port
    number(s), direction and protocol. It is used as a convenient way for users to
    express what ports they want to permit through the firewall.'''
    
    obj = vim.client.factory.create('ns0:HostFirewallRule')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'direction' ]
    inherited = [ 'endPort', 'port', 'protocol' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    