
==================================================================================================
VirtualMachineToolsStatus
==================================================================================================

.. describe:: VirtualMachineToolsStatus

    Current status of VMware Tools running in the guest operating system.
    
    
    .. py:data:: VirtualMachineToolsStatus.toolsNotInstalled
    
        VMware Tools has never been installed or has not run in the virtual machine.
        
    
    .. py:data:: VirtualMachineToolsStatus.toolsNotRunning
    
        VMware Tools is not running.
        
    
    .. py:data:: VirtualMachineToolsStatus.toolsOk
    
        VMware Tools is running and the version is current.
        
    
    .. py:data:: VirtualMachineToolsStatus.toolsOld
    
        VMware Tools is running, but the version is not current.
        
    