
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNasVolumeConfig(vim, *args, **kwargs):
    '''This describes the NAS Volume configuration containing the configurable
    properties on a NAS Volume'''
    
    obj = vim.client.factory.create('ns0:HostNasVolumeConfig')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    required = [  ]
    optional = [ 'changeOperation', 'spec', 'dynamicProperty', 'dynamicType' ]
    
    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    