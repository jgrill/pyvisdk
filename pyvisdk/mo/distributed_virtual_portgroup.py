
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.network import Network

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualPortgroup(Network):
    '''The interface to the distributed virtual portgroup objects. This type
    represents both a group of ports that share the common network setting and a
    Network entity in the datacenter.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.DistributedVirtualPortgroup):
        super(DistributedVirtualPortgroup, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def config(self):
        '''The configuration of the portgroup.'''
        return self.update('config')
    @property
    def key(self):
        '''The generated UUID of the portgroup.'''
        return self.update('key')
    @property
    def portKeys(self):
        '''The port keys of those ports in the portgroup.'''
        return self.update('portKeys')
    
    
    
    def ReconfigureDVPortgroup_Task(self):
        '''The DistributedVirtualPortgroups to be reconfigured* DVPortgroup.PolicyOp if
        changing the policy of the portgroup. * DVPortgroup.ScopeOp if changing the
        scope of the portgroup. * DVPortgroup.Modify for anything else.
        
        '''
        return self.delegate("ReconfigureDVPortgroup_Task")()