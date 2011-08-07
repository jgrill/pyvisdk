
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineSnapshot(ExtensibleManagedObject):
    '''The Snapshot managed object type specifies the interface to individual snapshots
        of a virtual machine. Although these are managed objects, they are
        subordinate to their virtual machine.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.VirtualMachineSnapshot):
        # MUST define these
        super(VirtualMachineSnapshot, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def childSnapshot(self):
        '''All snapshots for which this snapshot is the parent.
        '''
        return self.update('childSnapshot')

    @property
    def config(self):
        '''Information about the configuration of this virtual machine when this snapshot was
        taken.
        '''
        return self.update('config')


    def RemoveSnapshot_Task(self, host, suppressPowerOn):
        '''Removes this snapshot and deletes any associated storage.

        :param host: to a HostSystem(optional) Choice of host for the virtual machine, in case this
        operation causes the virtual machine to power on.

        :param suppressPowerOn: (optional) If set to true, the virtual machine will not be powered on regardless
        of the power state when the snapshot was created. Default to false.vSphere
        API 4.0


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RemoveSnapshot_Task")(host,suppressPowerOn)
        

    def RenameSnapshot(self, host, suppressPowerOn):
        '''Rename this snapshot with either a new name or a new description or both. At least
        one of these must be specified when calling the rename method.

        :param host: to a HostSystem(optional) Choice of host for the virtual machine, in case this
        operation causes the virtual machine to power on.

        :param suppressPowerOn: (optional) If set to true, the virtual machine will not be powered on regardless
        of the power state when the snapshot was created. Default to false.vSphere
        API 4.0


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RenameSnapshot")(host,suppressPowerOn)
        

    def RevertToSnapshot_Task(self, host, suppressPowerOn):
        '''Change the execution state of the virtual machine to the state of this snapshot.

        :param host: to a HostSystem(optional) Choice of host for the virtual machine, in case this
        operation causes the virtual machine to power on.

        :param suppressPowerOn: (optional) If set to true, the virtual machine will not be powered on regardless
        of the power state when the snapshot was created. Default to false.vSphere
        API 4.0


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RevertToSnapshot_Task")(host,suppressPowerOn)
        
