# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VAppOvfSectionInfo(vim, *args, **kwargs):
    '''The OvfSection encapsulates uninterpreted meta-data sections in an OVF
    descriptor. When an OVF package is imported, non-required / non-interpreted
    sections will be stored as OvfSection object. During the creation of an OVF
    package, these sections will be placed in the OVF descriptor.'''
    
    obj = vim.client.factory.create('ns0:VAppOvfSectionInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'atEnvelopeLevel', 'contents', 'key', 'namespace', 'type' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    