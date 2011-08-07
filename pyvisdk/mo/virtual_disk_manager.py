
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskManager(BaseEntity):
    '''NOTE: This managed object type and all of its methods are experimental and subject
        to change in future releases.This managed object type provides a way to
        manage and manipulate virtual disks on datastores. The source and the
        destination names are in the form of a URL or a datastore path.A URL has
        the formwhere* is or . * specifies the hostname or IP address of the
        VirtualCenter or ESX server and optionally the port. * is the inventory
        path to the Datacenter containing the Datastore. * is the name of the
        Datastore. * is a slash-delimited path from the root of the datastore.A
        datastore path has the formwhere* is the datastore name. * is a slash-
        delimited path from the root of the datastore.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.VirtualDiskManager):
        # MUST define these
        super(VirtualDiskManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def CopyVirtualDisk_Task(self, name, datacenter):
        '''Copy a virtual disk, performing conversions as specified in the spec.If source (or
        destination) name is specified as a URL, then the corresponding datacenter
        parameter may be omitted.Requires Datastore.FileManagement privilege on
        both source and destination datastores.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CopyVirtualDisk_Task")(name,datacenter)
        

    def CreateVirtualDisk_Task(self, name, datacenter):
        '''Create a virtual disk.The datacenter parameter may be omitted if a URL is used to
        name the disk.Requires Datastore.FileManagement privilege on the datastore
        where the virtual disk is created.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateVirtualDisk_Task")(name,datacenter)
        

    def DefragmentVirtualDisk_Task(self, name, datacenter):
        '''Defragment a sparse virtual disk. This is defragmentation of the virtual disk
        file(s) in the host operating system, not defragmentation of the guest
        operating system filesystem inside the virtual disk.The datacenter
        parameter may be omitted if a URL is used to name the disk.Requires
        Datastore.FileManagement privilege on the datastore where the virtual disk
        resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("DefragmentVirtualDisk_Task")(name,datacenter)
        

    def DeleteVirtualDisk_Task(self, name, datacenter):
        '''Delete a virtual disk. All files relating to the disk will be deleted.The
        datacenter parameter may be omitted if a URL is used to name the
        disk.Requires Datastore.FileManagement privilege on the datastore where
        the virtual disk is removed.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("DeleteVirtualDisk_Task")(name,datacenter)
        

    def EagerZeroVirtualDisk_Task(self, name, datacenter):
        '''Explicitly zero out unaccessed parts zeroedthick disk. Effectively a no-op if the
        disk is already eagerZeroedThick. Unlike zeroFillVirtualDisk, which wipes
        the entire disk, this operation only affects previously unaccessed parts
        of the disk.The datacenter parameter may be omitted if a URL is used to
        name the disk.Requires Datastore.FileManagement privilege on the datastore
        where the virtual disk resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("EagerZeroVirtualDisk_Task")(name,datacenter)
        

    def ExtendVirtualDisk_Task(self, name, datacenter):
        '''Expand the capacity of a virtual disk to the new capacity. If the eagerZero flag
        is not specified, - the extended disk region of a zerothick disk will be
        zeroedthick - the extended disk region of a eagerzerothick disk will be
        eagerzeroedthick - a thin-provisioned disk will always be extended as a
        thin-provisioned disk. If the eagerZero flag TRUE, the extended region of
        the disk will always be eagerly zeroed. If the eagerZero flag FALSE, the
        extended region of a zeroedthick or eagerzeroedthick the disk will not be
        eagerly zeroed. This condition has no effect on a thin source disk.The
        datacenter parameter may be omitted if a URL is used to name the
        disk.Requires Datastore.FileManagement privilege on the datastore where
        the virtual disk resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ExtendVirtualDisk_Task")(name,datacenter)
        

    def InflateVirtualDisk_Task(self, name, datacenter):
        '''Inflate a sparse or thin-provisioned virtual disk up to the full size. Additional
        space allocated to the disk as a result of this operation will be filled
        with zeroes.The datacenter parameter may be omitted if a URL is used to
        name the disk.Requires Datastore.FileManagement privilege on the datastore
        where the virtual disk resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("InflateVirtualDisk_Task")(name,datacenter)
        

    def MoveVirtualDisk_Task(self, name, datacenter):
        '''Move a virtual disk and all related files from the source location specified by
        sourceName and sourceDatacenter to the destination location specified by
        destName and destDatacenter.

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("MoveVirtualDisk_Task")(name,datacenter)
        

    def QueryVirtualDiskFragmentation(self, name, datacenter):
        '''Return the percentage of fragmentation of the sparse virtual disk. This is the
        fragmentation of virtual disk file(s) in the host operating system, not
        the fragmentation of the guest operating systemS filesystem inside the
        virtual disk.The datacenter parameter may be omitted if a URL is used to
        name the disk.Requires Datastore.FileManagement privilege on the datastore
        where the virtual disk resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("QueryVirtualDiskFragmentation")(name,datacenter)
        

    def QueryVirtualDiskGeometry(self, name, datacenter):
        '''Get the disk geometry information for the virtual disk.The datacenter parameter
        may be omitted if a URL is used to name the disk.Requires
        Datastore.FileManagement privilege on the datastore where the virtual disk
        resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("QueryVirtualDiskGeometry")(name,datacenter)
        

    def QueryVirtualDiskUuid(self, name, datacenter):
        '''Get the virtual disk SCSI inquiry page 0x83 data.The datacenter parameter may be
        omitted if a URL is used to name the disk.Requires
        Datastore.FileManagement privilege on the datastore where the virtual disk
        resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("QueryVirtualDiskUuid")(name,datacenter)
        

    def SetVirtualDiskUuid(self, name, datacenter):
        '''Set the virtual disk SCSI inquiry page 0x83 data.The datacenter parameter may be
        omitted if a URL is used to name the disk.Requires
        Datastore.FileManagement privilege on the datastore where the virtual disk
        resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("SetVirtualDiskUuid")(name,datacenter)
        

    def ShrinkVirtualDisk_Task(self, name, datacenter):
        '''Shrink a sparse virtual disk.The datacenter parameter may be omitted if a URL is
        used to name the disk.The optional parameter copy specifies whether to
        shrink the disk in copy-shrink mode or in-place mode. In copy-shrink mode,
        additional space is required, but will result in a shrunk disk that is
        also defragmented. In-place shrink does not require additional space, but
        will increase fragmentation. The default behavior is to perform copy-
        shrink if the parameter is not specified.

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ShrinkVirtualDisk_Task")(name,datacenter)
        

    def ZeroFillVirtualDisk_Task(self, name, datacenter):
        '''Overwrite all blocks of the virtual disk with zeros. All data will be lost.The
        datacenter parameter may be omitted if a URL is used to name the
        disk.Requires Datastore.FileManagement privilege on the datastore where
        the virtual disk resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual
        disk whose blocks should be overwritten with zeroes.

        :param datacenter: to a DatacenterIfis a datastore path, the datacenter for that datastore path. Not
        needed when invoked directly on ESX. If not specified on a call to
        VirtualCenter,must be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ZeroFillVirtualDisk_Task")(name,datacenter)
        
