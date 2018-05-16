import json
import inspect

from pyjss.api_calls import delete_call, get_call, push_call, put_call
from pyjss.settings import Credentials

from pyjss.parse_engine import clean_args, retrieve_endpoint, process_data

def parser(*args,endpoints):
    print(args)
    print(len(args))
    print(endpoints)

class Accounts():

    description = {
            0: {
                'endpoint': 'accounts',
                'methods': ['get']
            },
            1: {
                'id': {
                    'endpoint': 'accounts/userid/',
                    'methods': ['get', 'put', 'post', 'delete']
                },
                'name':{
                    'endpoint': 'accounts/username/',
                    'methods': ['get', 'put', 'post', 'delete']
                }
            },
            2: {
                'groupid': {
                    'endpoint': 'accounts/groupid/',
                    'methods': ['get', 'put', 'post', 'delete']
                    },
                'groupname':{
                    'endpoint': 'accounts/groupname/',
                    'methods': ['get', 'put', 'post', 'delete']
                    } 
                }
            }

    @classmethod
    def get(cls, item=None, group_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. If the item is a group use the syntax get( id | name, groupname | groupid)'''
        process_data(cls, item, group_item)

class ActivationCode():

    @staticmethod
    def get():
        '''No parameters. Return the Activation Code for your JAMF Pro instance.'''
        data = get_call('JSSResource/activationcode')
        return(data)


class AdvancedComputerSearches():

    @staticmethod
    def get(item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        if item == None:
            data = get_call('JSSResource/advancedcomputersearches')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/advancedcomputersearches/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/advancedcomputersearches/id/{0}'.format(item))
        return(data)


class AdvancedMobileDeviceSearches():

    @staticmethod
    def get(item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        if item == None:
            data = get_call('JSSResource/advancedmobiledevicesearches')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/advancedcomputersearches/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/advancedcomputersearches/id/{0}'.format(item))
        return(data)


class AdvancedUserSearches():

    @staticmethod
    def get(item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        if item == None:
            data = get_call('JSSResource/advancedusersearches')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/advancedusersearches/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/advancedusersearches/id/{0}'.format(item))
        return(data)

class AllowedFileExtension():

    @staticmethod
    def get(item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        if item == None:
            data = get_call('JSSResource/allowedfileextensions')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/allowedfileextensions/extension/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/allowedfileextensions/id/{0}'.format(item))
        return(data)


class Buildings():

    @staticmethod
    def get(item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        if item == None:
            data = get_call('JSSResource/buildings')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/buildings/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/buildings/id/{0}'.format(item))
        return(data)
        

class ByoProfiles():

    @staticmethod
    def get(item=None, site_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. If the item is a site use the syntax get('site', ID OR NAME)'''
        if item == None:
            data = get_call('JSSResource/byoprofiles')
        else:
            if item != 'site':
                if type(item) is str:
                    data = get_call(
                        'JSSResource/byoprofiles/name/{0}'.format(item))
                elif type(item) is int:
                    data = get_call(
                        'JSSResource/byoprofiles/id/{0}'.format(item))
            else:
                if type(site_item) is str:
                    data = get_call(
                        'JSSResource/byoprofiles/site/name/{0}'.format(site_item))
                elif type(site_item) is int:
                    data = get_call(
                        'JSSResource/byoprofiles/site/id/{0}'.format(site_item))
        return(data)


class Categories():

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/categories')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/categories/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/categories/id/{0}'.format(item))
        return(data)


class Classes():

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/classes')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/classes/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/classes/id/{0}'.format(item))
        return(data)


class CommandFlush():
    '''no get'''
    pass


class ComputerApplications():
    pass


class ComputerApplicationsUsage():

    @staticmethod
    def get(item_type=None, item=None, start_date=None, end_date=None):
        '''Item type could be id,name,udid,serialnumber or macaddress. All parameters are required.'''
        if item_type == 'id':
             data = get_call(
                 'JSSResource/computerapplicationusage/id/{0}/{1}_{2}'.format(item, start_date, end_date))
        elif item_type == 'name':
             data = get_call(
                 'JSSResource/computerapplicationusage/name/{0}/{1}_{2}'.format(item, start_date, end_date))
        elif item_type == 'udid':
             data = get_call(
                 'JSSResource/computerapplicationusage/udid/{0}/{1}_{2}'.format(item, start_date, end_date))
        elif item_type == 'serialnumber':
             data = get_call(
                 'JSSResource/computerapplicationusage/serialnumber/{0}/{1}_{2}'.format(item, start_date, end_date))
        elif item_type == 'macaddress':
             data = get_call(
                 'JSSResource/computerapplicationusage/macaddress/{0}/{1}_{2}'.format(item, start_date, end_date))
        return(data)


class ComputerCheckin():

    @staticmethod
    def get():
        '''No parameters. Return the computer checking settings for your JAMF Pro instance. '''
        data = get_call('JSSResource/computercheckin')
        return(data)


class ComputerCommands():
    
    @staticmethod
    def get(item_type=None, item=None):
        '''Item type could be id, uuid. statusuuid, name. If empty returns all computer commands.'''
        if item_type == None:
            data = get_call('JSSResource/computercommands')
        else:
            if item_type == 'id':
                data = get_call('JSSResource/computercommands/id/{0}'.format(item))
            elif item_type == 'uuid':
                data = get_call('JSSResource/computercommands/uuid/{0}'.format(item))
            elif item_type == 'statusuuid':
                data = get_call('JSSResource/computercommands/status/{0}'.format(item))
            elif item_type == 'name':
                data = get_call('JSSResource/computercommands/name/{0}'.format(item))
        return(data)


class ComputerConfigurations():

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/computerconfigurations')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/computerconfigurations/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/computerconfigurations/id/{0}'.format(item))
        return(data)


class ComputerExtensionAttributes():

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/computerextensionattributes')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/computerextensionattributes/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/computerextensionattributes/id/{0}'.format(item))
        return(data)


class ComputerGroups():

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/computergroups')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/computergroups/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/computergroups/id/{0}'.format(item))
        return(data)

class ComputerHardwareSoftwareReports():
    
    @staticmethod
    def get(item_type=None, item=None, start_date=None, end_date=None):
        '''Item type could be id,name,udid,serialnumber or macaddress. All parameters are required.'''
        if item_type == 'id':
             data = get_call(
                 'JSSResource/computerhardwaresoftwarereports/id/{0}/{1}_{2}'.format(item, start_date, end_date))
        elif item_type == 'name':
             data = get_call(
                 'JSSResource/computerhardwaresoftwarereports/name/{0}/{1}_{2}'.format(item, start_date, end_date))
        elif item_type == 'udid':
             data = get_call(
                 'JSSResource/computerhardwaresoftwarereports/udid/{0}/{1}_{2}'.format(item, start_date, end_date))
        elif item_type == 'serialnumber':
             data = get_call(
                 'JSSResource/computerhardwaresoftwarereports/serialnumber/{0}/{1}_{2}'.format(item, start_date, end_date))
        elif item_type == 'macaddress':
             data = get_call(
                 'JSSResource/computerhardwaresoftwarereports/macaddress/{0}/{1}_{2}'.format(item, start_date, end_date))
        return(data)


class ComputerHistory():
    
    @staticmethod
    def get(item_type=None, item=None, subset_item=None):
        '''Item type could be id,name,udid,serialnumber or macaddress. Subset is only available when use with id'''
        if item_type == 'id':
            if subset_item == None:
                data = get_call(
                    'JSSResource/computerhistory/id/{0}'.format(item))
            else:
                data = get_call(
                    'JSSResource/computerhistory/id/{0}/subset/{1}'.format(item,subset_item))
        elif item_type == 'name':
             data = get_call(
                 'JSSResource/computerhistory/name/{0}'.format(item))
        elif item_type == 'udid':
             data = get_call(
                 'JSSResource/computerhistory/udid/{0}'.format(item))
        elif item_type == 'serialnumber':
             data = get_call(
                 'JSSResource/computerhistory/serialnumber/{0}'.format(item))
        elif item_type == 'macaddress':
             data = get_call(
                 'JSSResource/computerhistory/macaddress/{0}'.format(item))
        return(data)


class ComputerInventoryCollection():

    @staticmethod
    def get():
        '''No parameters. Return the Computer inventory collection for your JAMF Pro instance.'''
        data = get_call('JSSResource/computerinventorycollection')
        return(data)


class ComputerInvitations():

    @staticmethod
    def get(item=None, invitation_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. If the item is a invitation number use the syntax get('invitation', invitationnumber) '''
        if item == None:
            data = get_call('JSSResource/computerinvitations')
        else:
            if item != 'invitation':
                if type(item) is str:
                    data = get_call(
                        'JSSResource/computerinvitations/name/{0}'.format(item))
                elif type(item) is int:
                    data = get_call(
                        'JSSResource/computerinvitations/id/{0}'.format(item))
            else:
                data = get_call(
                    'JSSResource/computerinvitations/invitation/{0}'.format(item))
        return(data)


class ComputerManagement():
    pass


class ComputerReports():

    @staticmethod
    def get(item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        if item == None:
            data = get_call('JSSResource/computerreports')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/computerreports/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/computerreports/id/{0}'.format(item))
        return(data)

class Computers():
    
    @staticmethod
    def get(item_type=None, item=None, subset_item=None):
        '''Item type could be None, subset, id,name, match, matchname,udid,serialnumber or macaddress. subset_item is only available when use with id'''
        if item_type == None:
            data = get_call('JSSResource/computers')
        else:
            if item_type == 'subset':
                data = get_call('JSSResource/computers/subset/basic')
            elif item_type == 'id':
                if subset_item == None:
                    data = get_call(
                        'JSSResource/computers/id/{0}'.format(item))
                else:
                    data = get_call(
                        'JSSResource/computers/id/{0}/subset/{1}'.format(item, subset_item))
            elif item_type == 'name':
                data = get_call(
                    'JSSResource/computers/name/{0}'.format(item))
            elif item_type == 'udid':
                data = get_call(
                    'JSSResource/computers/udid/{0}'.format(item))
            elif item_type == 'serialnumber':
                data = get_call(
                    'JSSResource/computers/serialnumber/{0}'.format(item))
            elif item_type == 'macaddress':
                data = get_call(
                    'JSSResource/computers/macaddress/{0}'.format(item))
            elif item_type == 'match':
                data = get_call(
                    'JSSResource/computers/match/{0}'.format(item))
            elif item_type == 'matchname':
                data = get_call(
                    'JSSResource/computers/match/name/{0}'.format(item))
        return(data)


class Departments():

    @staticmethod
    def get(item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        if item == None:
            data = get_call('JSSResource/departments')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/departments/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/departments/id/{0}'.format(item))
        return(data)


class DirectoryBindings():

    @staticmethod
    def get(item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        if item == None:
            data = get_call('JSSResource/directorybindings')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/directorybindings/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/directorybindings/id/{0}'.format(item))
        return(data)


class DiskEncryptionConfigurations():

    @staticmethod
    def get(item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        if item == None:
            data = get_call('JSSResource/diskencryptionconfigurations')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/diskencryptionconfigurations/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/diskencryptionconfigurations/id/{0}'.format(item))
        return(data)


class DistributionPoints():

    @staticmethod
    def get(item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        if item == None:
            data = get_call('JSSResource/distributionpoints')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/distributionpoints/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/distributionpoints/id/{0}'.format(item))
        return(data)


class DockItems():

    @staticmethod
    def get(item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list.'''
        if item == None:
            data = get_call('JSSResource/dockitems')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/dockitems/name/{0}'.format(item))
            elif type(item) is int:
                data = get_call(
                    'JSSResource/dockitems/id/{0}'.format(item))
        return(data)

class Ebooks():

    @staticmethod
    def get(item=None, subset_item=None):
        '''Specity ID or Name for the item. If no item has been specified return the full list. subset_item is only available when use with id'''
        if item == None:
            data = get_call('JSSResource/ebooks')
        else:
            if subset_item != None:
                data = get_call(
                    'JSSResource/ebooks/id/{0}/subset/{1}'.format(item, subset_item))
            else:
                if type(item) is str:
                    data = get_call(
                        'JSSResource/ebooks/name/{0}'.format(item))
                if type(item) is int:
                    data = get_call(
                        'JSSResource/ebooks/id/{0}'.format(item))
        return(data)


class FileUploads():
    ''' Only post method '''
    pass


class GsxConnexion():

    @staticmethod
    def get():
        data = get_call('JSSResource/gsxconnection')
        return(data)


class HealthCareListener():
    '''Get,Put'''
    @staticmethod
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
    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def get():
        data = get_call('JSSResource/infrastructuremanager')
        return(data)


class JsonWebTokenConfigurations():

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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
    
    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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
    
    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def get():
        data = get_call('JSSResource/smtpserver')
        return(data)


class SoftwareUpdateServers():

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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
