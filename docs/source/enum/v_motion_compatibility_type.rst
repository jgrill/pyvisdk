
==================================================================================================
VMotionCompatibilityType
==================================================================================================

.. describe:: VMotionCompatibilityType

    Types of a host's compatibility with a designated virtual machine that is a candidate for VMotion. Used with queryVMotionCompatibility both as inputs (to designate which compatibility types to test for) and as outputs (to specify which compatibility types apply for each host).
    
    
    .. py:data:: VMotionCompatibilityType.cpu
    
        The host's CPU features are compatible with the the virtual machine's requirements.
        
    
    .. py:data:: VMotionCompatibilityType.software
    
        The software platform on the host supports VMotion and is compatible with the virtual machine.
        
    