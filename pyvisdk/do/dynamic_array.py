# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DynamicArray(vim, *args, **kwargs):
    '''DynamicArray is a data object type that represents an array of dynamically-
    typed objects. A client should only see a DynamicArray object when the element
    type is unknown (meaning the type is newer than the client). Otherwise, a
    client would see the type as T[] where T is known.'''
    
    obj = vim.client.factory.create('ns0:DynamicArray')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'dynamicType', 'val' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    