import json
import inspect

from pyjss.api_calls import delete_call, get_call, push_call, put_call
from pyjss.settings import Credentials

from pyjss.parse_engine import process_data


def parser(*args,endpoints):
    print(args)
    print(len(args))
    print(endpoints)

class Accounts():

    @classmethod
    def get(cls, item=None, group_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. If the item is a group use the syntax get( id | name, groupname | groupid)'''
        process_data(__class__.__name__, item, group_item)

class ActivationCode():

    @classmethod
    def get(cls):
        '''No parameters. Return the Activation Code for your JAMF Pro instance.'''
        process_data(__class__.__name__)


class AdvancedComputerSearches():

    @classmethod
    def get(cls, item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        process_data(__class__.__name__, item)


class AdvancedMobileDeviceSearches():

    @classmethod
    def get(cls, item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        process_data(__class__.__name__, item)
class AdvancedUserSearches():

    @classmethod
    def get(cls,item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        process_data(__class__.__name__, item)

class AllowedFileExtension():

    @classmethod
    def get(cls, item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        process_data(__class__.__name__, item)

class Buildings():

    @classmethod
    def get(cls, item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        process_data(__class__.__name__, item)
        

class ByoProfiles():

    @classmethod
    def get(cls,item=None, site_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. If the item is a site use the syntax get('site', ID OR NAME)'''
        process_data(__class__.__name__, item, site_item)

class Categories():

    @classmethod
    def get(cls,item=None):
        process_data(__class__.__name__, item)


class Classes():

    @classmethod
    def get(cls, item=None):
        process_data(__class__.__name__, item)


class CommandFlush():
    '''no get'''
    pass


class ComputerApplications():
    
    @classmethod
    def get(cls, application, extra_item=None, extra_item2=None):
        '''Specity Name of the Application.
        The second argument could be  'version | inventory' with the data as a third argument.
        To get inventory information on a specific version please provide the version the second argument and the inventory data as the third.'''
        process_data(__class__.__name__, application, extra_item, extra_item2)



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
    def get(cls):
        process_data(__class__.__name__)

class HealthCareListener():
    '''Get,Put'''
    @classmethod
    def get(item_id=None):
        '''Specity id for the item. If no item has been specified return the full list.'''
        if item_id == None:
            data = get_call('JSSResource/healthcarelistener')
        else:
            if type(item_id) is int:
                data = get_call(
                    'JSSResource/healthcarelistener/id/{0}'.format(item_id))
            else:
                print('item_id should be an integer.')


class HealthCareListenerRule():
    '''Get, Put, Post'''
    @classmethod
    def get(item_id=None):
        '''Specity id for the item. If no item has been specified return the full list.'''
        if item_id == None:
            data = get_call('JSSResource/healthcarelistenerrule')
        else:
            if type(item_id) is int:
                data = get_call(
                    'JSSResource/healthcarelistenerrule/id/{0}'.format(item_id))
            else:
                print('item_id should be an integer.')

class Ibeacons():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/ibeacons')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/ibeacons/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/ibeacons/id/{0}'.format(item))
        return(data)


class InfrastructureManager():

    @classmethod
    def get():
        data = get_call('JSSResource/infrastructuremanager')
        return(data)


class JsonWebTokenConfigurations():

    @classmethod
    def get(db_id=None):
        if db_id == None:
            data = get_call('JSSResource/jsonwebtokenconfigurations')
        else:
            if type(db_id) is int:
                data = get_call(
                    'JSSResource/jsonwebtokenconfigurations/id/{0}'.format(db_id))
            else:
                print('Wrong type of data have been passed. The ID should be passed as integer')
        return(data)



class LdapServers():
    '''Get, Put, Post, Delete'''
    pass


class LicencedSoftware():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/licensedsoftware')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/licensedsoftware/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/licensedsoftware/id/{0}'.format(item))
        return(data)


class LogFlush():
    pass


class MacApplications():

    @classmethod
    def get(item=None, subset_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. subset_item is only available when use with id'''
        if item == None:
            data = get_call('JSSResource/macapplications')
        else:
            if subset_item != None:
                data = get_call(
                    'JSSResource/macapplications/id/{0}/subset/{1}'.format(item, subset_item))
            else:
                if type(item) is str:
                    data = get_call(
                        'JSSResource/macapplications/name/{0}'.format(item))
                elif type(item) is int:
                    data = get_call(
                        'JSSResource/macapplications/id/{0}'.format(item))
        return(data)


class ManagedPreferenceProfiles():

    @classmethod
    def get(item=None, subset_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. subset_item is only available when use with id'''
        if item == None:
            data = get_call('JSSResource/managedpreferenceprofiles')
        else:
            if subset_item != None:
                data = get_call(
                    'JSSResource/managedpreferenceprofiles/id/{0}/subset/{1}'.format(item, subset_item))
            else:
                if type(item) is str:
                    data = get_call(
                        'JSSResource/managedpreferenceprofiles/name/{0}'.format(item))
                elif type(item) is int:
                    data = get_call(
                        'JSSResource/managedpreferenceprofiles/id/{0}'.format(item))
        return(data)


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
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/managedpreferenceprofiles')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/managedpreferenceprofiles/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/managedpreferenceprofiles/id/{0}'.format(item))
        return(data)

class MobileDeviceEnrollementProfiles():
    pass


class MobileDeviceExtensionAttributes():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/mobiledeviceextensionattributes')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/mobiledeviceextensionattributes/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/mobiledeviceextensionattributes/id/{0}'.format(item))
        return(data)


class MobileDeviceExtensionGroups():

    @classmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/mobiledevicegroups')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/mobiledevicegroups/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/mobiledevicegroups/id/{0}'.format(item))
        return(data)


class MobileDeviceHistory():
    pass


class MobileDeviceInvitations():
    pass


class MobileDeviceProvisionningProfiles():
    pass

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
    def get():
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
