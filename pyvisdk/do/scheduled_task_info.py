# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ScheduledTaskInfo(vim, *args, **kwargs):
    '''The scheduled task details.'''
    
    obj = vim.client.factory.create('ns0:ScheduledTaskInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'action', 'description', 'enabled', 'name' ]
    inherited = [ 'notification', 'scheduler', 'activeTask', 'entity', 'error',
        'lastModifiedTime', 'lastModifiedUser', 'nextRunTime', 'prevRunTime',
        'progress', 'result', 'scheduledTask', 'state', 'taskObject' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    