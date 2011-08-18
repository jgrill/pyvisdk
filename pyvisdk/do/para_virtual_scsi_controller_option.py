# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ParaVirtualSCSIControllerOption(vim, *args, **kwargs):
    '''ParaVirtualSCSIControllerOption is the data object that contains the options
    for a a paravirtualized SCSI controller.'''
    
    obj = vim.client.factory.create('ns0:ParaVirtualSCSIControllerOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 8:
        raise IndexError('Expected at least 9 arguments got: %d' % len(args))
        
    signature = [ 'devices', 'defaultSharedIndex', 'hotAddRemove', 'numSCSICdroms',
        'numSCSIDisks', 'numSCSIPassthrough', 'scsiCtlrUnitNumber', 'sharing' ]
    inherited = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'deprecated', 'hotRemoveSupported',
        'licensingLimit', 'plugAndPlay', 'type', 'supportedDevice' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    