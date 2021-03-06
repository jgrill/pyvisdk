
==================================================================================================
HostIpConfigIpV6AddressConfigType
==================================================================================================

.. describe:: HostIpConfigIpV6AddressConfigType

    This specifies how the ipv6 address is configured for the interface. We follow rfc4293 in defining the values for the configType.
    
    
    .. py:data:: HostIpConfigIpV6AddressConfigType.dhcp
    
        The address is configured through dhcp.
        
    
    .. py:data:: HostIpConfigIpV6AddressConfigType.linklayer
    
        The address is obtained through stateless autoconfiguration.
        
    
    .. py:data:: HostIpConfigIpV6AddressConfigType.manual
    
        The address is configured manually.
        
    
    .. py:data:: HostIpConfigIpV6AddressConfigType.other
    
        Any other type of address configuration other than the below mentioned ones will fall under this category. For e.g., automatic address configuration for the link local address falls under this type.
        
    
    .. py:data:: HostIpConfigIpV6AddressConfigType.random
    
        The address is chosen by the system at random e.g., an IPv4 address within 169.254/16, or an RFC 3041 privacy address.
        
    