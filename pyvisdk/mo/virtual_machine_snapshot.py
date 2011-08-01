
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
    
    

    def RemoveSnapshot_Task(self, removeChildren):
        '''Removes this snapshot and deletes any associated storage.

        :param removeChildren: Flag to specify removal of the entire snapshot subtree.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RemoveSnapshot_Task")(removeChildren)
        

    def RenameSnapshot(self):
        '''Rename this snapshot with either a new name or a new description or both. At least
        one of these must be specified when calling the rename method.
        '''
        
        return self.delegate("RenameSnapshot")()
        

    def RevertToSnapshot_Task(self):
        '''Change the execution state of the virtual machine to the state of this snapshot.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RevertToSnapshot_Task")()
        