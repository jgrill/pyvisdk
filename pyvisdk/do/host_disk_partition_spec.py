
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskPartitionSpec(vim, *args, **kwargs):
    '''This data object type describes the disk partition table specification used to
    configure the partitions on a disk. This data object represents the fundamental
    data needed to specify a partition table.'''
    
    obj = vim.client.factory.create('ns0:HostDiskPartitionSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    required = [  ]
    optional = [ 'chs', 'partition', 'totalSectors', 'dynamicProperty', 'dynamicType' ]
    
    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    