
==================================================================================================
VirtualDeviceConfigSpecFileOperation
==================================================================================================

.. describe:: VirtualDeviceConfigSpecFileOperation

    The type of operation being performed on the backing of a virtual device. Valid values are:
    
    
    .. py:data:: VirtualDeviceConfigSpecFileOperation.create
    
        Specifies the creation of the device backing; for example, the creation of a virtual disk or floppy image file.
        
    
    .. py:data:: VirtualDeviceConfigSpecFileOperation.destroy
    
        Specifies the destruction of a device backing.
        
    
    .. py:data:: VirtualDeviceConfigSpecFileOperation.replace
    
        Specifies the deletion of the existing backing for a virtual device and the creation of a new backing.
        
    