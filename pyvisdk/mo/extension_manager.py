
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtensionManager(BaseEntity):
    '''This managed object type provides directory and basic management services for
    all registered extensions.Clients use the ExtensionManager, available in
    ServiceInstance, to access extension objects.While several authentication
    methods are available for extension servers to use (see SessionManager), only
    one authentication method is valid for an extension at any given time.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ExtensionManager):
        super(ExtensionManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def extensionList(self):
        '''The list of currently registered extensions.'''
        return self.update('extensionList')
    
    
    
    def FindExtension(self, extensionKey):
        '''Returns extension with the given key, if any.
        
        :param extensionKey: Key to search for.
        
        '''
        return self.delegate("FindExtension")(extensionKey)
    
    def GetPublicKey(self):
        '''Deprecated. As of VI 4.0, use trusted certificates and
        LoginExtensionBySubjectName or SetExtensionCertificate and
        LoginExtensionByCertificate. Returns VirtualCenter Server public key.
        
        '''
        return self.delegate("GetPublicKey")()
    
    def RegisterExtension(self, extension):
        '''Registers extension.
        
        :param extension: Extension description to register.
        
        '''
        return self.delegate("RegisterExtension")(extension)
    
    def SetExtensionCertificate(self, extensionKey, certificatePem):
        '''Update the stored authentication certificate for a specified extension. Updates
        the registration of the specified extension with the thumbprint of the X.509
        client certificate provided over SSL handshake, or by the
        "certificatePem"argument. The thumbprint will be used to authenticate the
        extension during invocations of LoginExtensionByCertificate.NOTE: No
        verification is performed on the received certificate, such as expiry or
        revocation.This method will unset any public key or subject name associated
        with the extension.
        
        :param extensionKey: Key of extension to update.
        
        :param certificatePem: PEM encoded certificate. If not specified, the certificate passed over SSL handshake is used.
        
        '''
        return self.delegate("SetExtensionCertificate")(extensionKey, certificatePem)
    
    def SetPublicKey(self, extensionKey, publicKey):
        '''Deprecated. As of VI 4.0, use trusted certificates and
        LoginExtensionBySubjectName or SetExtensionCertificate and
        LoginExtensionByCertificate. Sets extension's public key.
        
        :param extensionKey: Key of extension to update.
        
        :param publicKey: Public key of extension, encoded in PEM (privacy-enhanced mail) format.
        
        '''
        return self.delegate("SetPublicKey")(extensionKey, publicKey)
    
    def UnregisterExtension(self, extensionKey):
        '''Unregisters the specified extension if it exists.
        
        :param extensionKey: Unique name of extension to unregister.
        
        '''
        return self.delegate("UnregisterExtension")(extensionKey)
    
    def UpdateExtension(self, extension):
        '''If the key specified in the extension exists, the existing record is updated.If
        the "subjectName" property of the Extension object has a value, and it is
        different from the existing value, this method will unset any public key or
        certificate associated with the extension.
        
        :param extension: Updated extension description.
        
        '''
        return self.delegate("UpdateExtension")(extension)