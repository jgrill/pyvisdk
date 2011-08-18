# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DiagnosticManagerLogHeader(vim, *args, **kwargs):
    '''A header that is returned with a set of log entries. This header describes
    where entries are located in the log file. Log files typically grow
    dynamically, so indexes based on line numbers may become inaccurate.'''
    
    obj = vim.client.factory.create('ns0:DiagnosticManagerLogHeader')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'lineEnd', 'lineStart' ]
    inherited = [ 'lineText' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    