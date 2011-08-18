# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterComputeResourceSummary(vim, *args, **kwargs):
    '''The ClusterComputeResourceSummary data object encapsulates runtime properties
    of a ClusterComputeResource.'''
    
    obj = vim.client.factory.create('ns0:ClusterComputeResourceSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 9:
        raise IndexError('Expected at least 10 arguments got: %d' % len(args))
        
    signature = [ 'effectiveCpu', 'effectiveMemory', 'numCpuCores', 'numCpuThreads',
        'numEffectiveHosts', 'numHosts', 'overallStatus', 'totalCpu', 'totalMemory' ]
    inherited = [ 'admissionControlInfo', 'currentBalance', 'currentEVCModeKey',
        'currentFailoverLevel', 'numVmotions', 'targetBalance' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    