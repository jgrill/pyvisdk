
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EnvironmentBrowser(BaseEntity):
    '''This managed object type provides access to the environment that a
    ComputeResource presents for creating and configuring a virtual machine.The
    environment consists of three main components:* The virtual machine
    configuration options. Each vim.vm.ConfigOption describes the execution
    environment for a virtual machine, the particular set of virtual hardware that
    is supported. A ComputeResource might support multiple sets. Access is provided
    through the configOptionDescriptor property and the QueryConfigOption
    operation. * The supported device targets. Each virtual device specified in the
    virtual machine needs to be hooked up to a "physical" counterpart. For
    networks, this means choosing a network name; for a virtual CD-rom this might
    be an ISO image, etc. The environment browser provides access to the device
    targets through the QueryConfigTarget operation. * Storage locations and files.
    A selection of locations where the virtual machine files can be stored, and the
    possibility to browse for existing virtual disks and ISO images. The datastore
    browser, provided by the datastoreBrowser property, provides access to the
    contents of one or more datastores. The items in a datastore are files that
    contain configuration, virtual disk, and the other data associated with a
    virtual machine. * The capabilities supported by the ComputeResource to which
    the virtual machine belongs.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.EnvironmentBrowser):
        super(EnvironmentBrowser, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def datastoreBrowser(self):
        '''DatastoreBrowser to browse datastores that are available on this entity.'''
        return self.update('datastoreBrowser')
    
    
    
    def QueryConfigOption(self, key, host):
        '''Query for a specific virtual machine configuration option (the ConfigOption).If
        the EnvironmentBrowser is from a ComputeResource or ClusterComputeResource, the
        key or host, or both arguments can be used to return the required config
        options. If a key is specified, then the ConfigOption corresponding to that key
        value is returned. If a host is specified, then the default ConfigOption for
        that host is returned. If key and host both are specified, the ConfigOption
        corresponding to the given key for that host is returned. If neither is
        specified, then the default ConfigOption for this environment browser is
        returned. Typically, the default contains the options for the most recent
        virtual hardware supported.If the EnvironmentBrowser is from a VirtualMachine
        neither a host nor a key should be specified.
        
        :param key: The key found in the VirtualMachineConfigOptionDescriptor, obtained by invoking the QueryConfigOptionDescriptor operation.
        
        :param host: The host whose ConfigOption is requested.
        
        '''
        return self.delegate("QueryConfigOption")(key, host)
    
    def QueryConfigOptionDescriptor(self):
        '''The list of ConfigOption keys available on this entity.
        
        '''
        return self.delegate("QueryConfigOptionDescriptor")()
    
    def QueryConfigTarget(self, host):
        '''Queries for information about a specific target, a "physical" device that can
        be used to back virtual devices. The ConfigTarget that is returned specifies
        the set of values that can be used in the device backings to connect the
        virtual machine to physical (or logical) host devices.If the EnvironmentBrowser
        is from a ComputeResource or ClusterComputeResource, the host argument can be
        used to return the ConfigTarget provided by a particular host in the compute
        resource or cluster. If host is specified and the EnvironmentBrowser is from a
        ComputeResource or ClusterComputeResource, then the union of all the devices is
        returned and the vim.vm.TargetInfo.configurationTag field indicates how widely
        the device is available across the compute resource or cluster.If the
        EnvironmentBrowser is from a VirtualMachine a host should not be specified.
        
        :param host: If specified, the host whose default BackingInfo is requested.
        
        '''
        return self.delegate("QueryConfigTarget")(host)
    
    def QueryTargetCapabilities(self, host):
        '''Queries for information on the capabilities supported by the ComputeResource
        associated with the EnvironmentBrowser.If the EnvironmentBrowser is from a
        ComputeResource or ClusterComputeResource, the host argument can be used to
        return the capabilities associated with a specific host in the compute resource
        or cluster. If the host argument is not specified and the EnvironmentBrowser is
        from a ComputeResource or ClusterComputeResource, then the intersection of the
        capabilities supported by all the hosts in the cluster is returned. If the
        EnvironmentBrowser is from a VirtualMachine, the compute resource associated
        with the virtual machine will be queried for its capabilities.If the
        EnvironmentBrowser is from a VirtualMachine a host should not be specified.
        
        :param host: If specified, the host whose capabilities are requested.
        
        '''
        return self.delegate("QueryTargetCapabilities")(host)