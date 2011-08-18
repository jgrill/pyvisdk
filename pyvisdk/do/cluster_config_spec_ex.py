# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterConfigSpecEx(vim, *args, **kwargs):
    '''The ClusterConfigSpecEx data object provides a set of update specifications for
    complete cluster configuration. You can configure a cluster when you create a
    new cluster (the CreateClusterEx method) or when you reconfigure an existing
    cluster (the ReconfigureComputeResource_Task method).All fields are optional.
    If you set the parameter to when you call ReconfigureComputeResource_Task, an
    unset property has no effect on the existing property value in the cluster
    configuration on the Server. If you set the parameter to when you reconfigure a
    cluster, the cluster configuration is reverted to the default values, then the
    new configuration values are applied.Use the properties defined for this object
    to configure the following services:When it chooses a failover host, HA selects
    a host that is compatible with the virtual machine and that can support
    resource allocation for that virtual machine so that service level guarantees
    remain intact. HA does not consider hosts that are in maintenance mode, standby
    mode, or which are disconnected from the vCenter Server. When a host powers on
    or becomes available again, HA is reenabled on that host, so it becomes
    available for failover again. VMware recommends that you configure hosts and
    virtual machines so that all virtual machines can run on all hosts in the
    cluster. This will maximize the chances of restarting a VM after a failure.HA
    also restarts a virtual machine after a guest operating system failure. In this
    case, the virtual machine health monitoring service detects the guest failure,
    and HA restarts the virtual machine on the same host. The service monitors
    heartbeats from the VmTools service and optionally heartbeats that are
    generated by a third-party application monitor. See
    ClusterVmToolsMonitoringSettings and ClusterDasConfigInfo.vmMonitoring.To
    enable HA for a cluster, set the ClusterDasConfigInfo.enabled property to and
    the ClusterDasConfigInfo.hostMonitoring property to enabled. (The vSphere API
    uses the substring "das" in object, property, and method names for HA. )To
    enable DRS for a cluster, set the ClusterDrsConfigInfo.enabled property to .To
    enable DPM for a cluster, set the ClusterDpmConfigInfo.enabled property to .The
    HA, DRS, and DPM services are integrated with the FT (Fault Tolerance) and EVC
    (Enhanced vMotion Compatibility) services. Use the CreateSecondaryVM_Task
    method to establish fault tolerance for a virtual machine. Use the vSphere
    Client to configure EVC. The HA, DRS, DPM, FT, and EVC services interact under
    the following circumstances.When admission control is disabled, failover
    resource constraints are not passed on to DRS and DPM. The constraints are not
    enforced.If EVC is disabled, vCenter automatically creates overrides to disable
    DRS for FT primary/secondary pairs in the cluster. vCenter will still use DRS
    to place a secondary virtual machine when it powers on. Attempts to remove the
    overrides or to enable DRS operations will fail.High Availability was
    previously called Distributed Availability Services.'''
    
    obj = vim.client.factory.create('ns0:ClusterConfigSpecEx')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'vmSwapPlacement', 'dasConfig', 'dasVmConfigSpec', 'dpmConfig',
        'dpmHostConfigSpec', 'drsConfig', 'drsVmConfigSpec', 'groupSpec', 'rulesSpec' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    