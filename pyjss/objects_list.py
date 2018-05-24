import json
import inspect


from pyjss.api_calls import delete_call, get_call, push_call, put_call
from pyjss.settings import Credentials

from pyjss.parse_engine import (get_no_parameter, get_by_field)


class Accounts():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_no_parameter(__class__.__name__)

    @classmethod
    def getByUserId(cls, useriD):
        return get_by_field(__class__.__name__, 'id',useriD)

    @classmethod
    def getByUserName(cls, userName):
        return get_by_field(__class__.__name__, 'username', userName)

    @classmethod
    def getByGroupId(cls, groupID):
        return get_by_field(__class__.__name__, 'groupid', groupID)

    @classmethod
    def getByGroupName(cls, groupName):
        return get_by_field(__class__.__name__, 'groupname', groupName)

class ActivationCode():

    @classmethod
    def get(cls):
        '''Return Activation Code'''
        return get_no_parameter(__class__.__name__)



class AdvancedComputerSearches():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_no_parameter(__class__.__name__)

    @classmethod
    def getById(cls, id_item):
        return get_by_field(__class__.__name__, 'id', id_item)

    @classmethod
    def getByName(cls, name_item):
        return get_by_field(__class__.__name__, 'name', name_item)


class AdvancedMobileDeviceSearches():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_no_parameter(__class__.__name__)

    @classmethod
    def getById(cls, id_item):
        return get_by_field(__class__.__name__, 'id', id_item)

    @classmethod
    def getByName(cls, name_item):
        return get_by_field(__class__.__name__, 'name', name_item)


class AdvancedUserSearches():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_no_parameter(__class__.__name__)

    @classmethod
    def getById(cls, id_item):
        return get_by_field(__class__.__name__, 'id', id_item)

    @classmethod
    def getByName(cls, name_item):
        return get_by_field(__class__.__name__, 'name', name_item)

class AllowedFileExtension():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_no_parameter(__class__.__name__)

    @classmethod
    def getById(cls, id_item):
        return get_by_field(__class__.__name__, 'id', id_item)

    @classmethod
    def getByName(cls, name_item):
        return get_by_field(__class__.__name__, 'extension', name_item)


class Buildings():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_no_parameter(__class__.__name__)

    @classmethod
    def getById(cls, id_item):
        return get_by_id(__class__.__name__, id_item)

    @classmethod
    def getByName(cls, name_item):
        return get_by_name(__class__.__name__, name_item)

class ByoProfiles():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_no_parameter(__class__.__name__)

    @classmethod
    def getByUserId(cls, useriD):
        return get_by_userid(__class__.__name__, useriD)

    @classmethod
    def getByUserName(cls, userName):
        return get_by_username(__class__.__name__, userName)

    @classmethod
    def getBysiteId(cls, siteID):
        return get_by_siteid(__class__.__name__, siteID)

    @classmethod
    def getBySitepName(cls, siteName):
        return get_by_sitename(__class__.__name__, siteName)

class Categories():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_no_parameter(__class__.__name__)

    @classmethod
    def getById(cls, id_item):
        return get_by_id(__class__.__name__, id_item)

    @classmethod
    def getByName(cls, name_item):
        return get_by_name(__class__.__name__, name_item)


class Classes():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_no_parameter(__class__.__name__)

    @classmethod
    def getById(cls, id_item):
        return get_by_id(__class__.__name__, id_item)

    @classmethod
    def getByName(cls, name_item):
        return get_by_name(__class__.__name__, name_item)


class CommandFlush():
    '''no get'''
    pass


class ComputerApplications():
    
    @classmethod
    def getApp(cls, application):
        '''Return Advanced searches'''
        return get_by_application(__class__.__name__)

    @classmethod
    def getAppInfo(cls, application, info_items):
        '''Return Advanced searches'''
        return get_by_application(__class__.__name__, application, info_items)

    @classmethod
    def getAppVersion(cls, application, version):
        return get_by_application(__class__.__name__, application, version)

    @classmethod
    def getAppVersionInfo(cls, application, version, info_items):
        return get_by_application(__class__.__name__, application, version, info_items)



class ComputerApplicationsUsage():

    @classmethod
    def get(cls, item_type, item, date):
        process_data(__class__.__name__, item_type, item, date)
        


class ComputerCheckin():

    @classmethod
    def get(cls,):
        '''No parameters. Return the computer checking settings for your JAMF Pro instance. '''
        process_data(__class__.__name__)


class ComputerCommands():
    
    @classmethod
    def get(cls, item=None, item_type=None, extra_item=None, extra_item2=None):
        '''Item type could be id, uuid. statusuuid, name. If empty returns all computer commands.'''
        process_data(__class__.__name__, item, item_type,extra_item, extra_item2)


class ComputerConfigurations():

    @classmethod
    def get(cls,item=None):
        process_data(__class__.__name__, item)


class ComputerExtensionAttributes():

    @classmethod
    def get(cls, item=None):
        process_data(__class__.__name__, item)

class ComputerGroups():

    @classmethod
    def get(cls, item=None):
        process_data(__class__.__name__, item)

class ComputerHardwareSoftwareReports():
    
    @classmethod
    def get(item_type, item, date, subset=None):
        process_data(__class__.__name__, item_type, item, date, subset)


class ComputerHistory():
    
    @classmethod
    def get(item_type, item, subset=None):
        process_data(__class__.__name__, item_type, item, subset)

class ComputerInventoryCollection():

    @classmethod
    def get(cls):
        '''No parameters. Return the Computer inventory collection for your JAMF Pro instance.'''
        process_data(__class__.__name__)


class ComputerInvitations():

    @classmethod
    def get(cls,item_type, item):
        '''Specity ID or Name for the item. If no item has been specified return the full list. If the item is a invitation number use the syntax get('invitation', invitationnumber) '''
        process_data(__class__.__name__, item_type, item)


class ComputerManagement():
    'get to be done'
    pass


class ComputerReports():

    @classmethod
    def get(cls,item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        process_data(__class__.__name__, item)

class Computers():
    
    @classmethod
    def get(item_type=None, item=None, subset_item=None):
        '''Item type could be None, subset, id,name, match, matchname,udid,serialnumber or macaddress. subset_item is only available when use with id'''
        '''to be done'''


class Departments():

    @classmethod
    def get(cls,item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        process_data(__class__.__name__, item)
    

class DirectoryBindings():

    @classmethod
    def get(cls, item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        process_data(__class__.__name__, item)


class DiskEncryptionConfigurations():

    @classmethod
    def get(cls,item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        process_data(__class__.__name__, item)


class DistributionPoints():

    @classmethod
    def get(cls, item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        process_data(__class__.__name__, item)


class DockItems():

    @classmethod
    def get(cls, item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        process_data(__class__.__name__, item)


class Ebooks():

    @classmethod
    def get(cls, item=None, subset_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. subset_item is only available when use with id'''
        process_data(__class__.__name__, item, subset_item)


class FileUploads():
    ''' Only post method '''
    pass


class GsxConnexion():

    @classmethod
    def get(cls, item_id=None):
        process_data(__class__.__name__,item_id)

class HealthCareListener():
    '''Get,Put'''
    @classmethod
    def get(cls, item_id=None):
        process_data(__class__.__name__, item_id)

class HealthCareListenerRule():
    '''Get, Put, Post'''
    @classmethod
    def get(cls, item_id=None):
        process_data(__class__.__name__, item_id)

class Ibeacons():

    @classmethod
    def get(cls, item_id=None):
        process_data(__class__.__name__, item_id)


class InfrastructureManager():

    @classmethod
    def get(cls, item_id=None):
        process_data(__class__.__name__, item_id)


class JsonWebTokenConfigurations():

    @classmethod
    def get(cls, item_id=None):
        process_data(__class__.__name__, item_id)


class LdapServers():
    '''Get, Put, Post, Delete'''
    '''todo'''



class LicencedSoftware():

    @classmethod
    def get(cls, item_id=None):
        process_data(__class__.__name__, item_id)


class LogFlush():
    ''' only delete'''
    pass


class MacApplications():

    @classmethod
    def get(cls, item=None, subset_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. subset_item is only available when use with id'''
        process_data(__class__.__name__, item, subset_item)


class ManagedPreferenceProfiles():

    @classmethod
    def get(cls, item=None, subset_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. subset_item is only available when use with id'''
        process_data(__class__.__name__, item, subset_item)

class MobileDeviceApplications():
    
    @classmethod
    def get(item_type=None, item=None, extra_item=None):
        '''Item could be id, bundleid, name. If no item has been specified return the full list. extra_item is only available when use with id and bundleid'''
        if item_type == None:
            data = get_call('JSSResource/mobiledeviceapplications')
        elif item_type == 'id':
            if extra_item != None:
                data = get_call(
                    'JSSResource/mobiledeviceapplications/id/{0}'.format(item))
            else:
                data = get_call(
                    'JSSResource/mobiledeviceapplications/id/{0}/subset/{1}'.format(item,extra_item))
        elif item_type == 'bundleid':
            if extra_item == None:
                data = get_call(
                    'JSSResource/mobiledeviceapplications/bundleid/{0}'.format(item))
            else:
                data = get_call('JSSResource/mobiledeviceapplications/bundleid/{0}/version/{1}'.format(item,extra_item))
        return(data)


class MobileDeviceCommands():
    pass


class MobileDeviceConfigurationProfiles():

    @classmethod
    def get(cls, item=None, subset_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. subset_item is only available when use with id'''
        process_data(__class__.__name__, item, subset_item)

class MobileDeviceEnrollementProfiles():
    pass


class MobileDeviceExtensionAttributes():

    @classmethod
    def get(cls, item_id=None):
        process_data(__class__.__name__, item_id)


class MobileDeviceExtensionGroups():

    @classmethod
    def get(cls, item_id=None):
        process_data(__class__.__name__, item_id)


class MobileDeviceHistory():
    
    @classmethod
    def get(cls, item_type,item, subset_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. subset_item is only available when use with id'''
        process_data(__class__.__name__, item_type, item, subset_item)



class MobileDeviceInvitations():
    
    @classmethod
    def get(cls, item_id=None):
        process_data(__class__.__name__, item_id)


class MobileDeviceProvisionningProfiles():
    
    @classmethod
    def get(cls, item_type,item, subset_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. subset_item is only available when use with id'''
        process_data(__class__.__name__, item_type, item, subset_item)


class MobileDevices():
    pass


class NetbootServers():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/netbootservers')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/netbootservers/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/netbootservers/id/{0}'.format(item))
        return(data)


class NetworkSegments():
    def __init__(self, name, starting_ip, ending_ip):
        self.name = name
        self.starting_ip = starting_ip
        self.ending_ip = ending_ip
    
    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/networksegments')
        else:
            if type(item) is str:
                data = get_call('JSSResource/networksegments/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call('JSSResource/networksegments/id/{0}'.format(item))
        return(data)


class OsxConfigurationProfiles():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/osxconfigurationprofiles')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/osxconfigurationprofiles/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/osxconfigurationprofiles/id/{0}'.format(item))
        return(data)


class Packages():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/packages')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/packages/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/packages/id/{0}'.format(item))
        return(data)


class Patches():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/patches')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/patches/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/patches/id/{0}'.format(item))
        return(data)


class PatchExternalSources():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/patchexternalsources')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/patchexternalsources/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/patchexternalsources/id/{0}'.format(item))
        return(data)


class PatchInternalSources():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/patchinternalsources')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/patchinternalsources/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/patchinternalsources/id/{0}'.format(item))
        return(data)


class PatchPolicies():
    pass


class Peripherals():

    @classmethod
    def get(item_id=None):
        if item_id == None:
            data = get_call('JSSResource/peripherals')
        else:
            if type(item_id) is int:
                data = get_call(
                    'JSSResource/peripherals/id/{0}'.format(item_id))
            else:
                print('Item_ID should be an integer.')
        return(data)


class PeripheralsTypes():

    @classmethod
    def get(item_id=None):
        if item_id == None:
            data = get_call('JSSResource/peripheraltypes')
        else:
            if type(item_id) is int:
                data = get_call(
                    'JSSResource/peripheraltypes/id/{0}'.format(item_id))
            else:
                print('Item_ID should be an integer.')
        return(data)

class Policies():
    pass    


class Printers():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/printers')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/printers/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/printers/id/{0}'.format(item))
        return(data)


class RemovableMacAddresses():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/removablemacaddresses')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/removablemacaddresses/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/removablemacaddresses/id/{0}'.format(item))
        return(data)


class RestrictedSoftware():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/restrictedsoftware')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/restrictedsoftware/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/restrictedsoftware/id/{0}'.format(item))
        return(data)


class SavedSearches():
    pass


class Stripts():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/scripts')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/scripts/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/scripts/id/{0}'.format(item))
        return(data)


class Sites():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/sites')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/sites/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/sites/id/{0}'.format(item))
        return(data)


class SmtpServer():

    @classmethod
    def get(cls):
        data = get_call('JSSResource/smtpserver')
        return(data)


class SoftwareUpdateServers():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/softwareupdateservers')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/sitsoftwareupdateserverses/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/softwareupdateservers/id/{0}'.format(item))
        return(data)


class UserExtensionAttributes():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/userextensionattributes')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/userextensionattributes/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/userextensionattributes/id/{0}'.format(item))
        return(data)


class UserGroups():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/usergroups')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/usergroups/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/usergroups/id/{0}'.format(item))
        return(data)


class Users():
    pass


class VppAccounts():

    @classmethod
    def get(item_id=None):
        if item_id == None:
            data = get_call('JSSResource/vppaccounts')
        else:
            if type(item_id) is int:
                data = get_call(
                    'JSSResource/vppaccounts/id/{0}'.format(item_id))
            else:
                print('Item_ID should be an integer.')
        return(data)


class VppAssignments():

    @classmethod
    def get(item_id=None):
        if item_id == None:
            data = get_call('JSSResource/vppassignments')
        else:
            if type(item_id) is int:
                data = get_call(
                    'JSSResource/vppassignments/id/{0}'.format(item_id))
            else:
                print('Item_ID should be an integer.')
        return(data)


class VppInvitations():

    @classmethod
    def get(item_id=None):
        if item_id == None:
            data = get_call('JSSResource/vppinvitations')
        else:
            if type(item_id) is int:
                data = get_call(
                    'JSSResource/vppinvitations/id/{0}'.format(item_id))
            else:
                print('item_id should be an integer.')
        return(data)


class Webhooks():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/webhooks')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/webhooks/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/webhooks/id/{0}'.format(item))
        return(data)
