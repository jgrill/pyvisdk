#!/usr/bin/env python
from pyvisdk import consts
import pyvisdk.core
from pyvisdk.vm import VirtualMachine
import logging

"""
Assumptions:  Must connect to the vSphere vCenter
              Must be version 4.0 or greater

"""
log = logging.getLogger(__name__)

class Vim(pyvisdk.core.VimBase):
    def __init__(self, server, connect=True, verbose=3):
        super(Vim, self).__init__(server, connect, verbose)
        
    def login(self, username, password):
        self.username = username
        self.password = password
        
        if self.verbose > 5:
            self.displayAbout()

        self.client.service.Login(self.managers['sessionManager'], self.username, self.password)
        if self.verbose > 2:
            log.info("Successfully logged into %s" % self.url)

    def logout(self):
        self.client.service.Logout(self.managers['sessionManager'])

    def displayAbout(self):
        print dir(self.service_content.about)
        print "=" * 40
        print "Connected to %s" % self.server
        print "  %s" % self.service_content.about.fullName
        print "  OS: %s" % self.service_content.about.osType
        print "  License: %s %s" % (
                self.service_content.about.licenseProductName, self.service_content.about.licenseProductVersion)
        print "=" * 40

    def getApiType(self):
        return self.service_content.about.apiType

    def getVirtualMachine(self, name):
        return VirtualMachine(self, name)
        
    def getAllVirtualMachineRefs(self, attrs=["name", "runtime.powerState"]):
        pSpec = self.PropertySpec(consts.VirtualMachine, pathSet=attrs)
        refs = self.getContentsRecursively(root=self.root, props=pSpec, recurse=True)
        return refs
    
    def getAllVirtualMachines(self, attrs=["name", "runtime.powerState"]):
        
        pSpec = self.PropertySpec(consts.VirtualMachine, pathSet=attrs)
        
        refs = self.getContentsRecursively(root=self.root, props=pSpec, recurse=True)
        out = []
        for ref in refs:
            out.append( VirtualMachine(self, name=ref.propSet[0].val) )
        return out

    def getHostSystem(self, name):
        mo = self.getDecendentsByName(_type=consts.HostSystem, name=name)
        return mo

    def getDatacenter(self, name):
        mo = self.getDecendentsByName(_type=consts.Datacenter, name=name)
        return mo
        
if __name__ == '__main__':
    from optparse import OptionParser
    import sys

    # Some command line argument parsing gorp to make the script a little more
    # user friendly.
    usage = '''Usage: %prog [options]

      This program will dump the containers of the ESX environment from the host specified with
      the -s option.'''
    
    parser = OptionParser(usage=usage)
    parser.add_option('-s', '--server', dest='server',
                  help='Specify the vCenter to connect to')
    parser.add_option('-u', '--username', dest='username',
                      help='Username (default is root)')
    parser.add_option('-p', '--password', dest='password',
                      help='Password (default is blank)')
    (options, args) = parser.parse_args()
    if options.server is None:
        print 'You must specify a server to connect to.  Use --help for usage'
        sys.exit(1)
    if options.username is None:
        options.username = 'root'
    if options.password is None:
        options.password = ''


    print "Connecting to " + options.server
    vim = Vim(options.server, verbose=3)
    vim.login(options.username, options.password)
    
    vms = vim.getAllVirtualMachineRefs()
    for ref in vms:
        name = ref.propSet[0].val
        power = ref.propSet[1].val
        print "%-20s %s" % (name, power)
            
        vm = vim.getVirtualMachine(name)
        sname = vm.createSnapshot()
        print sname
        
        snap = vm.getSnapshotByName(sname)
        print snap
        break
    
    vim.logout()

