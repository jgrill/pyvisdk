
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachine(ManagedEntity):
    '''VirtualMachine is the managed object type for manipulating virtual machines,
        including templates that can be deployed (repeatedly) as new virtual
        machines. This type provides methods for configuring and controlling a
        virtual machine.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.VirtualMachine):
        # MUST define these
        super(VirtualMachine, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def StandbyGuest(self):
        '''Issues a command to the guest operating system asking it to prepare for a suspend
        operation. Returns immediately and does not wait for the guest operating
        system to complete the operation.
        '''
        
        return self.delegate("StandbyGuest")()
        

    def MarkAsVirtualMachine(self):
        '''Clears the 'isTemplate' flag and reassociates the virtual machine with a resource
        pool and host.
        '''
        
        return self.delegate("MarkAsVirtualMachine")()
        

    def QueryFaultToleranceCompatibility(self):
        '''This API can be invoked to determine whether a virtual machine is compatible for
        Fault Tolerance. The API only checks for VM-specific factors that impact
        compatibility for Fault Tolerance. Other requirements for Fault Tolerance
        such as host processor compatibility, logging nic configuration and
        licensing are not covered by this API. The query returns a list of faults,
        each fault corresponding to a specific incompatibility. If a given virtual
        machine is compatible for Fault Tolerance, then the fault list returned
        will be empty.

        :rtype: MethodFault[] 

        '''
        
        return self.delegate("QueryFaultToleranceCompatibility")()
        

    def RelocateVM_Task(self, spec):
        '''Relocates a virtual machine's virtual disks to a specific location; optionally
        moves the virtual machine to a different host as well.Additionally
        requires the Resource.HotMigrate privilege if the virtual machine is
        powered on (for Storage VMotion), and Datastore.AllocateSpace on any
        datastore the virtual machine or its disks are relocated to.If the "pool"
        field of the RelocateSpec is set, additionally requires the
        Resource.AssignVMToPool privilege held on the specified pool.

        :param spec: The specification of where to relocate the virtual machine.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RelocateVM_Task")(spec)
        

    def RebootGuest(self):
        '''Issues a command to the guest operating system asking it to perform a reboot.
        Returns immediately and does not wait for the guest operating system to
        complete the operation.
        '''
        
        return self.delegate("RebootGuest")()
        

    def PowerOffVM_Task(self):
        '''Powers off this virtual machine. If this virtual machine is a fault tolerant
        primary virtual machine, this will result in the secondary virtual
        machine(s) getting powered off as well.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("PowerOffVM_Task")()
        

    def CustomizeVM_Task(self, spec):
        '''Customizes a virtual machine's guest operating system.

        :param spec: The customization specification object.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CustomizeVM_Task")(spec)
        

    def StopReplaying_Task(self):
        '''Stops a replay session on this virtual machine.This is an experimental interface
        that is not intended for use in production code.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("StopReplaying_Task")()
        

    def CreateSecondaryVM_Task(self):
        '''Creates a secondary virtual machine to be part of this fault tolerant group.If a
        host is specified, the secondary virtual machine will be created on it.
        Otherwise, a host will be selected by the system.If the primary virtual
        machine (i.e., this virtual machine) is powered on when the secondary is
        created, an attempt will be made to power on the secondary on a system
        selected host. If the cluster is a DRS cluster, DRS will be invoked to
        obtain a placement for the new secondary virtual machine. If the DRS
        recommendation (see ClusterRecommendation) is automatic, it will be
        automatically executed. Otherwise, the recommendation will be returned to
        the caller of this method and the secondary will remain powered off until
        the recommendation is approved using ApplyRecommendation. Failure to power
        on the secondary virtual machine will not fail the creation of the
        secondary.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateSecondaryVM_Task")()
        

    def UpgradeVM_Task(self):
        '''Upgrades this virtual machine's virtual hardware to the latest revision that is
        supported by the virtual machine's current host.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("UpgradeVM_Task")()
        

    def SuspendVM_Task(self):
        '''Suspends execution in this virtual machine.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("SuspendVM_Task")()
        

    def RefreshStorageInfo(self):
        '''Explicitly refreshes the storage information of this virtual machine, updating
        properties storage, layoutEx and storage.
        '''
        
        return self.delegate("RefreshStorageInfo")()
        

    def ExtractOvfEnvironment(self):
        '''Returns the OVF environment for a virtual machine. If the virtual machine has no
        vApp configuration, an empty string is returned. Also, sensitive
        information is omitted, so this method is not guaranteed to return the
        complete OVF environment.

        :rtype: xsd:string 

        '''
        
        return self.delegate("ExtractOvfEnvironment")()
        

    def ShutdownGuest(self):
        '''Issues a command to the guest operating system asking it to perform a clean
        shutdown of all services. Returns immediately and does not wait for the
        guest operating system to complete the operation.
        '''
        
        return self.delegate("ShutdownGuest")()
        

    def UpgradeTools_Task(self):
        '''Begins the tools upgrade process. To monitor the status of the tools install,
        clients should check the tools status, toolsVersionStatus and
        toolsRunningStatus.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("UpgradeTools_Task")()
        

    def MakePrimaryVM_Task(self):
        '''Makes the specified secondary virtual machine from this fault tolerant group as
        the primary virtual machine.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("MakePrimaryVM_Task")()
        

    def CheckCustomizationSpec(self, spec):
        '''Checks the customization specification against the virtual machine configuration.
        For example, this is used on a source virtual machine before a clone
        operation to catch customization failure before the disk copy. This checks
        the specification's internal consistency as well as for compatibility with
        this virtual machine's configuration.

        :param spec: The customization specification to check.

        '''
        
        return self.delegate("CheckCustomizationSpec")(spec)
        

    def QueryUnownedFiles(self):
        '''For all files that belong to the vm, check that the file owner is set to the
        current datastore principal user, as set by
        HostDatastoreSystem.ConfigureDatastorePrincipal

        :rtype: xsd:string[] 

        '''
        
        return self.delegate("QueryUnownedFiles")()
        

    def QueryChangedDiskAreas(self, deviceKey, startOffset, changeId):
        '''Get a list of areas of a virtual disk belonging to this VM that have been modified
        since a well-defined point in the past. The beginning of the change
        interval is identified by "changeId", while the end of the change interval
        is implied by the snapshot ID passed in.Note that the result of this
        function may contain "false positives" (i.e: flag areas of the disk as
        modified that are not). However, it is guaranteed that no changes will be
        missed.

        :param deviceKey: Identifies the virtual disk for which to compute changes.

        :param startOffset: Start Offset in bytes at which to start computing changes. Typically, callers will make multiple calls to this function, starting with startOffset 0 and then examine the "length" property in the returned DiskChangeInfo structure, repeatedly calling queryChangedDiskAreas until a map forthe entire virtual disk has been obtained.

        :param changeId: Identifyer referring to a point in the past that should be used as the point in time at which to begin including changes to the disk in the result. A typical use case would be a backup application obtaining a changeId from a virtual disk's backing info when performing a backup. When a subsequent incremental backup is to be performed, this change Id can be used to obtain a list of changed areas on disk.


        :rtype: DiskChangeInfo 

        '''
        
        return self.delegate("QueryChangedDiskAreas")(deviceKey,startOffset,changeId)
        

    def CloneVM_Task(self, name, spec):
        '''Creates a clone of this virtual machine. If the virtual machine is used as a
        template, this method corresponds to the deploy command.Any % (percent)
        character used in this name parameter must be escaped, unless it is used
        to start an escape sequence. Clients may also escape any other characters
        in this name parameter.The privilege required on the source virtual
        machine depends on the source and destination types:

        :param name: The name of the new virtual machine.

        :param spec: Specifies how to clone the virtual machine.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CloneVM_Task")(name,spec)
        

    def RemoveAllSnapshots_Task(self):
        '''Remove all the snapshots associated with this virtual machine. If the virtual
        machine does not have any snapshots, then this operation simply returns
        successfully.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RemoveAllSnapshots_Task")()
        

    def TurnOffFaultToleranceForVM_Task(self):
        '''Removes all secondary virtual machines associated with the fault tolerant group
        and turns off protection for this virtual machine. This operation can only
        be invoked from the primary virtual machine in the group.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("TurnOffFaultToleranceForVM_Task")()
        

    def TerminateFaultTolerantVM_Task(self):
        '''Terminates the specified secondary virtual machine in a fault tolerant group. This
        can be used to test fault tolerance on a given virtual machine, and should
        be used with care.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("TerminateFaultTolerantVM_Task")()
        

    def ReconfigVM_Task(self, spec):
        '''Reconfigures this virtual machine. All the changes in the given configuration are
        applied to the virtual machine as an atomic operation.Reconfiguring the
        virtual machine may require any of the following privileges depending on
        what is being changed:

        :param spec: The new configuration values.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ReconfigVM_Task")(spec)
        

    def StartReplaying_Task(self):
        '''Starts a replay session on this virtual machine. As a side effect, this operation
        updates the current snapshot of the virtual machine.This is an
        experimental interface that is not intended for use in production code.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("StartReplaying_Task")()
        

    def AcquireMksTicket(self):
        '''Deprecated. As of vSphere API 4.1, use AcquireTicket instead. Creates and returns
        a one-time credential used in establishing a remote mouse-keyboard-screen
        connection to this virtual machine. The correct function of this method
        depends on being able to retrieve TCP binding information about the server
        end of the client connection that is requesting the ticket. If such
        information is not available, the NotSupported fault is thrown. This
        method is appropriate for SOAP and authenticated connections, which are
        both TCP-based connections.

        :rtype: VirtualMachineMksTicket 

        '''
        
        return self.delegate("AcquireMksTicket")()
        

    def StartRecording_Task(self, name):
        '''Initiates a recording session on this virtual machine. As a side effect, this
        operation creates a snapshot on the virtual machine, which in turn becomes
        the current snapshot.This is an experimental interface that is not
        intended for use in production code.

        :param name: The name for the snapshot associated with this recording. The name need not be unique for this virtual machine.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("StartRecording_Task")(name)
        

    def UnmountToolsInstaller(self):
        '''Unmounts VMware Tools installer CD.
        '''
        
        return self.delegate("UnmountToolsInstaller")()
        

    def MountToolsInstaller(self):
        '''Mounts the VMware Tools CD installer as a CD-ROM for the guest operating system.
        To monitor the status of the tools install, clients should check the tools
        status, toolsVersionStatus and toolsRunningStatus
        '''
        
        return self.delegate("MountToolsInstaller")()
        

    def SetDisplayTopology(self, displays):
        '''Sets the console window's display topology as specified.

        :param displays: The topology for each monitor that the virtual machine's display must span.

        '''
        
        return self.delegate("SetDisplayTopology")(displays)
        

    def PromoteDisks_Task(self, unlink):
        '''Promotes disks on this virtual machine that have delta disk backings.A delta disk
        backing is a way to preserve a virtual disk backing at some point in time.
        A delta disk backing is a file backing which in turn points to the
        original virtual disk backing (the parent). After a delta disk backing is
        added, all writes go to the delta disk backing. All reads first try the
        delta disk backing and then try the parent backing if needed.Promoting
        does two things

        :param unlink: If true, then these disks will be unlinked before consolidation.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("PromoteDisks_Task")(unlink)
        

    def CreateScreenshot_Task(self):
        '''Create a screen shot of a virtual machine.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateScreenshot_Task")()
        

    def reloadVirtualMachineFromPath_Task(self, configurationPath):
        '''Reloads the configuration for this virtual machine from a given datastore path.
        This is equivalent to unregistering and registering the virtual machine
        from a different path. The virtual machine's hardware configuration,
        snapshots, guestinfo variables etc. will be replaced based on the new
        configuration file. Other information associated with the virtual machine
        object, such as events and permissions, will be preserved.This method is
        only supported on vCenter Server. It can be invoked on inaccessible or
        orphaned virtual machines, but it cannot be invoked on powered on,
        connected virtual machines.Note: If the referenced configuration path does
        not refer to a valid virtual machine, configuration information for the
        virtual machine object may be lost.

        :param configurationPath: 


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("reloadVirtualMachineFromPath_Task")(configurationPath)
        

    def EnableSecondaryVM_Task(self):
        '''Enables the specified secondary virtual machine in this fault tolerant group.This
        operation is used to enable a secondary virtual machine that was
        previously disabled by the DisableSecondaryVM_Task call. The specified
        secondary will be automatically started whenever the primary is powered
        on.If the primary virtual machine (i.e., this virtual machine) is powered
        on when the secondary is enabled, an attempt will be made to power on the
        secondary. If a host was specified in the method call, this host will be
        used. If a host is not specified, one will be selected by the system. In
        the latter case, if the cluster is a DRS cluster, DRS will be invoked to
        obtain a placement for the new secondary virtual machine. If the DRS
        recommendation (see ClusterRecommendation) is automatic, it will be
        executed. Otherwise, the recommendation will be returned to the caller of
        this method and the secondary will remain powered off until the
        recommendation is approved using ApplyRecommendation.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("EnableSecondaryVM_Task")()
        

    def AnswerVM(self, questionId, answerChoice):
        '''Responds to a question that is blocking this virtual machine.

        :param questionId: The value from QuestionInfo.id that identifies the question to answer.

        :param answerChoice: The contents of the QuestionInfo.choice.value array element that identifies the desired answer.

        '''
        
        return self.delegate("AnswerVM")(questionId,answerChoice)
        

    def ExportVm(self):
        '''Obtains an export lease on this virtual machine. The export lease contains a list
        of URLs for the virtual disks for this virtual machine, as well as a
        ticket giving access to the URLs.See HttpNfcLease for information on how
        to use the lease.

        :rtype: ManagedObjectReference to a HttpNfcLease 

        '''
        
        return self.delegate("ExportVm")()
        

    def DisableSecondaryVM_Task(self):
        '''Disables the specified secondary virtual machine in this fault tolerant group. The
        specified secondary will not be automatically started on a subsequent
        power-on of the primary virtual machine. This operation could leave the
        primary virtual machine in a non-fault tolerant state.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("DisableSecondaryVM_Task")()
        

    def StopRecording_Task(self):
        '''Stops a currently active recording session on this virtual machine.This is an
        experimental interface that is not intended for use in production code.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("StopRecording_Task")()
        

    def DefragmentAllDisks(self):
        '''Defragment all virtual disks attached to this virtual machine.
        '''
        
        return self.delegate("DefragmentAllDisks")()
        

    def MarkAsTemplate(self):
        '''Marks a VirtualMachine object as being used as a template. Note: A VirtualMachine
        marked as a template cannot be powered on.
        '''
        
        return self.delegate("MarkAsTemplate")()
        

    def AcquireTicket(self, ticketType):
        '''Creates and returns a one-time credential used in establishing a specific
        connection to this virtual machine, for example, a ticket type of mks can
        be used to establish a remote mouse-keyboard-screen connection.A client
        using this ticketing mechanism must have network connectivity to the ESX
        server where the virtual machine is running, and the ESX server must be
        reachable to the management client from the address made available to the
        client via the ticket.Acquiring a virtual machine ticket requires
        different privileges depending on the types of ticket:

        :param ticketType: The type of service to acquire, the set of possible values is described in VirtualMachineTicketType.


        :rtype: VirtualMachineTicket 

        '''
        
        return self.delegate("AcquireTicket")(ticketType)
        

    def UnregisterVM(self):
        '''Removes this virtual machine from the inventory without removing any of the
        virtual machine's files on disk. All high-level information stored with
        the management server (ESX Server or VirtualCenter) is removed, including
        information such as statistics, resource pool association, permissions,
        and alarms.Use the Folder.RegisterVM method to recreate a VirtualMachine
        object from the set of virtual machine files by passing in the path to the
        configuration file. However, the VirtualMachine managed object that
        results typically has different objects ID and may inherit a different set
        of permissions.
        '''
        
        return self.delegate("UnregisterVM")()
        

    def PowerOnVM_Task(self):
        '''Powers on this virtual machine. If the virtual machine is suspended, this method
        resumes execution from the suspend point.When powering on a virtual
        machine in a cluster, the system might implicitly or due to the host
        argument, do an implicit relocation of the virtual machine to another
        host. Hence, errors related to this relocation can be thrown. If the
        cluster is a DRS cluster, DRS will be invoked if the virtual machine can
        be automatically placed by DRS (see DrsBehavior). Because this method does
        not return a DRS ClusterRecommendation, no vmotion nor host power
        operations will be done as part of a DRS-facilitated power on. To have DRS
        consider such operations use PowerOnMultiVM_Task.If this virtual machine
        is a fault tolerant primary virtual machine, its secondary virtual
        machines will be started on system-selected hosts. If the virtual machines
        are in a VMware DRS enabled cluster, then DRS will be invoked to obtain
        placements for the secondaries but no vmotion nor host power operations
        will be considered for these power ons.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("PowerOnVM_Task")()
        

    def ResetGuestInformation(self):
        '''Clears cached guest information. Guest information can be cleared only if the
        virtual machine is powered off.This method can be useful if stale
        information is cached, preventing an IP address or MAC address from being
        reused.
        '''
        
        return self.delegate("ResetGuestInformation")()
        

    def ResetVM_Task(self):
        '''Resets power on this virtual machine. If the current state is poweredOn, then this
        method first performs powerOff(hard). Once the power state is poweredOff,
        then this method performs powerOn(option).Although this method functions
        as a powerOff followed by a powerOn, the two operations are atomic with
        respect to other clients, meaning that other power operations cannot be
        performed until the reset method completes.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ResetVM_Task")()
        

    def RevertToCurrentSnapshot_Task(self):
        '''Reverts the virtual machine to the current snapshot. This is equivalent to doing
        snapshot.currentSnapshot.revert.If no snapshot exists, then the operation
        does nothing, and the virtual machine state remains unchanged.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RevertToCurrentSnapshot_Task")()
        

    def SetScreenResolution(self, width, height):
        '''Sets the console window's resolution as specified.

        :param width: The screen width that should be set.

        :param height: The screen height that should be set.

        '''
        
        return self.delegate("SetScreenResolution")(width,height)
        

    def MigrateVM_Task(self, priority):
        '''Migrates a virtual machine's execution to a specific resource pool or
        host.Requires Resource.HotMigrate privilege if the virtual machine is
        powered on or Resource.ColdMigrate privilege if the virtual machine is
        powered off or suspended.

        :param priority: The task priority (@see vim.VirtualMachine.MovePriority).


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("MigrateVM_Task")(priority)
        

    def CreateSnapshot_Task(self, quiesce, name):
        '''Creates a new snapshot of this virtual machine. As a side effect, this updates the
        current snapshot.Snapshots are not supported for Fault Tolerance primary
        and secondary virtual machines.Any % (percent) character used in this name
        parameter must be escaped, unless it is used to start an escape sequence.
        Clients may also escape any other characters in this name parameter.

        :param quiesce: If TRUE and the virtual machine is powered on when the snapshot is taken, VMware Tools is used to quiesce the file system in the virtual machine. This assures that a disk snapshot represents a consistent state of the guest file systems. If the virtual machine is powered off or VMware Tools are not available, the quiesce flag is ignored.

        :param name: The name for this snapshot. The name need not be unique for this virtual machine.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateSnapshot_Task")(quiesce,name)
        