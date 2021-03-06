
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.resource_pool import ResourcePool

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualApp(ResourcePool):
    '''Represents a multi-tiered software solution. A vApp is a collection of virtual
    machines (and potentially other vApp containers) that are operated and
    monitored as a unit. From a manage perspective, a multi-tiered vApp acts a lot
    like a virtual machine object. It has power operations, networks, datastores,
    and its resource usage can be configured.From a technical perspective, a vApp
    container is a specialized resource pool that has been extended with the
    following capabilities:Destroying a vAppWhen a vApp is destroyed, all of its
    virtual machines are destroyed, as well as any child vApps.The VApp.Delete
    privilege must be held on the vApp as well as the parent folder of the vApp.
    Also, the VApp.Delete privilege must be held on any child vApps that would be
    destroyed by the operation.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.VirtualApp):
        super(VirtualApp, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def childLink(self):
        '''List of linked children'''
        return self.update('childLink')
    @property
    def datastore(self):
        '''A collection of references to the subset of datastore objects used by this
        vApp.'''
        return self.update('datastore')
    @property
    def network(self):
        '''A collection of references to the subset of network objects that is used by
        this virtual machine.'''
        return self.update('network')
    @property
    def parentFolder(self):
        '''A reference to the parent folder in the VM and Template folder hierarchy. This
        can be null if the vApp is not associated with a VM & Template folder. A child
        vApp can never be associated with a folder, but it is also not a requirement
        that a root vApp is linked into the VM and Template view.'''
        return self.update('parentFolder')
    @property
    def parentVApp(self):
        '''Reference to the parent vApp.'''
        return self.update('parentVApp')
    @property
    def vAppConfig(self):
        '''Configuration of this package.'''
        return self.update('vAppConfig')
    
    
    
    def CloneVApp_Task(self, name, target, spec):
        '''Creates a clone of this vApp.Any % (percent) character used in this name
        parameter must be escaped, unless it is used to start an escape sequence.
        Clients may also escape any other characters in this name parameter.When
        invoking this method, the following privilege checks occur:* The privilege
        VApp.Clone is required on this vApp. * If the target is a resource pool, the
        privilege Resource.AssignVAppToPool is required on it. * If the target is a
        vApp, the privileges VApp.Clone and VApp.AssignVApp are required on
        it.Additional privileges are required by the clone spec provided. See
        VAppCloneSpec for details.
        
        :param name: The name of the new vApp.
        
        :param target: The parent entity of the new vApp. Must be of type ResourcePool or VirtualApp.
        
        :param spec: Specifies how to clone the vApp.
        
        '''
        return self.delegate("CloneVApp_Task")(name, target, spec)
    
    def ExportVApp(self):
        '''Obtains an export lease on this vApp. The export lease contains a list of URLs
        for the disks of the virtual machines in this vApp, as well as a ticket that
        gives access to these URLs.See HttpNfcLease for information on how to use the
        lease.
        
        '''
        return self.delegate("ExportVApp")()
    
    def PowerOffVApp_Task(self, force):
        '''Stops this vApp.The virtual machines (or child vApps) will be stopped in the
        order specified in the vApp configuration, if force is false. If force is set
        to true, all virtual machines are powered-off (in no specific order and
        possibly in parallel) regardless of the vApp auto-start configuration.While a
        vApp is stopping, all power operations performed on sub entities are disabled
        through the VIM API. They will throw TaskInProgress.
        
        :param force: If force is false, the shutdown order in the vApp is executed. If force is true, all virtual machines are powered-off (regardless of shutdown order).
        
        '''
        return self.delegate("PowerOffVApp_Task")(force)
    
    def PowerOnVApp_Task(self):
        '''Starts this vApp.The virtual machines (or sub vApps) will be started in the
        order specified in the vApp configuration. If the vApp is suspended (@see
        vim.VirtualApp.Summary.suspended), all suspended virtual machines will be
        powered-on based on the defined start-up order.While a vApp is starting, all
        power operations performed on sub entities are disabled through the VIM API.
        They will throw TaskInProgress.In case of a failure to power-on a virtual
        machine, the exception from the virtual machine power on is returned, and the
        power-on sequence will be terminated. In case of a failure, virtual machines
        that are already started will remain powered-on.
        
        '''
        return self.delegate("PowerOnVApp_Task")()
    
    def SuspendVApp_Task(self):
        '''Suspends this vApp.Suspends all powered-on virtual machines in a vApp,
        including virtual machines in child vApps. The virtual machines are suspended
        in the same order as used for a power-off operation (reverse power-on
        sequence).While a vApp is being suspended, all power operations performed on
        sub entities are disabled through the VIM API. They will throw TaskInProgress.
        
        '''
        return self.delegate("SuspendVApp_Task")()
    
    def unregisterVApp_Task(self):
        '''Removes this vApp from the inventory without removing any of the virtual
        machine's files on disk. All high-level information stored with the management
        server (ESX Server or VirtualCenter) is removed, including information such as
        vApp configuration, statistics, permissions, and alarms.
        
        '''
        return self.delegate("unregisterVApp_Task")()
    
    def UpdateLinkedChildren(self, addChangeSet, removeSet):
        '''Reconfigure the set of linked children.A VirtualMachine and vApp can be added
        as a linked child as long as it is not a direct child of another vApp. In case
        it is a linked child, the existing link is removed and replaced with the new
        link specified in this call.An InvalidArgument fault is thrown if a link target
        is a direct child of another vApp, or if the addition of the link will result
        in a vApp with a cycle. For example, a vApp cannot be linked to itself.The
        removeSet must refer to managed entities that are currently linked children.
        Otherwise, an InvalidArgument exception is thrown.For each entity being linked,
        the operation is subject to the following privilege checks:* If the object
        being linked is a vApp, VApp.Move must be held on the vApp being linked and its
        former parent vApp (if any). The privilege VApp.AssignVApp must be held on this
        vApp. * If the object being linked is a VirtualMachine, VApp.AssignVM is
        required on both the target vApp, the VirtualMachine, and its former parent
        vApp (if any).Privilege checks for each entity in the removeSet are similar to
        the entities in the addChangeSet, except that there is no target vApp.This
        operation is only transactional with respect to each individual link change.
        The changes are processed sequentially and committed one at a time. The
        addChangeSet is processed first, followed by the removeSet. If a failure is
        detected, then the method terminates with an exception.
        
        :param addChangeSet: a set of LinkInfo objects that either add a new link or modify an exisiting link.
        
        :param removeSet: a set of entities that should no longer link to this vApp.
        
        '''
        return self.delegate("UpdateLinkedChildren")(addChangeSet, removeSet)
    
    def UpdateVAppConfig(self, spec):
        '''Updates the vApp configuration.Updates in different areas require different
        privileges. See VAppConfigSpec for a full description.
        
        :param spec: contains the updates to the current configuration. Any set element, is changed. All values in the spec that is left unset, will not be modified.
        
        '''
        return self.delegate("UpdateVAppConfig")(spec)