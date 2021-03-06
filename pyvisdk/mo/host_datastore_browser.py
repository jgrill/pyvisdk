
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDatastoreBrowser(BaseEntity):
    '''The DatastoreBrowser managed object type provides access to the contents of one
    or more datastores. The items in a datastore are files that contain
    configuration, virtual disk, and the other data associated with a virtual
    machine.Although datastores may often be implemented using a traditional file
    system, a full interface to a file system is not provided here. Instead,
    specialized access for virtual machine files is provided. A datastore
    implementation may completely hide the file directory structure.The intent is
    to provide functionality analogous to a file chooser in a user interface.Files
    on datastores do not have independent permissions through this API. Instead,
    the permissions for all the files on a datastore derive from the datastore
    object itself. It is not possible to change individual file permissions as the
    user browsing the datastore may not necessarily be a recognized user from the
    point of view of the host changing the permission. This occurs if the user
    browsing the datastore is doing so through the VirtualCenter management
    server.The DatastoreBrowser provides many ways to customize a search for files.
    A search can be customized by specifying the types of files to be searched,
    search criteria specific to a file type, and the amount of detail about each
    file. The most basic queries only use file details and are efficient with
    limited side effects. For these queries, file metadata details can be
    optionally retrieved, but the files themselves are opened and their contents
    examined. As a result, these files are not necessarily validated.More
    complicated queries can be formed by specifying the specific types of files to
    be searched, the parameters to filter for each type, and the desired level of
    detail about each file. This method of searching for files is convenient
    because it allows additional data about the virtual machine component to be
    retrieved. In addition, certain validation checks can be performed on matched
    files as an inherent part of the details collection process. However, gathering
    extra details or the use of type specific filters can sometimes only be
    implemented by examining the contents of a file. As a result, the use of these
    conveniences comes with the cost of additional latency in the request and
    possible side effects on the system as a whole.See FileInfo'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostDatastoreBrowser):
        super(HostDatastoreBrowser, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def datastore(self):
        '''Set of datastores that can be searched on this DatastoreBrowser.'''
        return self.update('datastore')
    @property
    def supportedType(self):
        '''The list of supported file types. The supported file types are represented as
        items in this list. For each supported file type, there is an object in the
        list whose dynamic type is one of the types derived from the FileQuery data
        object type. In general, the properties in this query type are not set.'''
        return self.update('supportedType')
    
    
    
    def DeleteFile(self):
        '''Deprecated. As of VI API 2.5, use DeleteDatastoreFile_Task. Deletes the
        specified files from the datastore. If a valid virtual disk file is specified,
        then all the components of the virtual disk are deleted.
        
        '''
        return self.delegate("DeleteFile")()
    
    def SearchDatastore_Task(self):
        '''Returns the information for the files that match the given search criteria as a
        SearchResults object. Searches only the folder specified by the datastore path.
        The Datastore.Browse privilege must be held on the datastore identified by the
        datastore path.
        
        '''
        return self.delegate("SearchDatastore_Task")()
    
    def SearchDatastoreSubFolders_Task(self):
        '''Returns the information for the files that match the given search criteria as a
        SearchResults[] object. Searches the folder specified by the datastore path and
        all subfolders. The Datastore.Browse privilege must be held on the datastore
        identified by the datastore path.
        
        '''
        return self.delegate("SearchDatastoreSubFolders_Task")()