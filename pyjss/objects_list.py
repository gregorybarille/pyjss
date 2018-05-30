import json
import inspect


from pyjss.api_calls import delete_call, get_call, push_call, put_call
from pyjss.settings import Credentials

from pyjss.parse_engine import (get_no_parameter, get_by_field)

class Basic_object():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item)) 
    
class Accounts():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getByUserId(cls, useriD):
        return get_call('{0}/userid/{1}'.format(__class__.__name__.lower(),useriD))

    @classmethod
    def getByUserName(cls, userName):
        return get_call('{0}/username/{1}'.format(__class__.__name__.lower(), userName))

    @classmethod
    def getByGroupId(cls, groupID):
        return get_call('{0}/groupid/{1}'.format(__class__.__name__.lower(), groupID))
    @classmethod
    def getByGroupName(cls, groupName):
        return get_call('{0}/groupname/{1}'.format(__class__.__name__.lower(), groupName))

class ActivationCode():

    @classmethod
    def get(cls):
        '''Return Activation Code'''
        return get_call(__class__.__name__.lower())


class AdvancedComputerSearches(Basic_object):
    pass


class AdvancedMobileDeviceSearches(Basic_object):
    pass


class AdvancedUserSearches(Basic_object):
    pass

class AllowedFileExtension(Basic_object):
    pass


class Buildings(Basic_object):
    pass


class ByoProfiles(Basic_object):

    @classmethod
    def getBysiteId(cls, siteID):
        return get_call('{0}/siteid/{1}'.format(__class__.__name__.lower(), siteID))

    @classmethod
    def getBySiteName(cls, siteName):
        return get_call('{0}/sitename/{1}'.format(__class__.__name__.lower(), siteName))


class Categories(Basic_object):
    pass


class Classes(Basic_object):
    pass


class CommandFlush():
    '''no get'''
    pass


class ComputerApplications():
    
    @classmethod
    def getApp(cls, application):
        '''Return Advanced searches'''
        return get_call('{0}/application/{1}'.format(__class__.__name__.lower(), application))

    @classmethod
    def getAppInfo(cls, application, inventory_items):
        '''Return Advanced searches'''
        return get_call('{0}/application/{1}/inventory/{2}'.format(__class__.__name__.lower(), application, inventory_items))

    @classmethod
    def getAppVersion(cls, application, version):
        return get_call('{0}/application/{1}/version/{2}'.format(__class__.__name__.lower(), application, version))

    @classmethod
    def getAppVersionInfo(cls, application, version, info_items):
        return get_call('{0}/application/{1}/version/{2}/inventory/{3}'.format(__class__.__name__.lower(), application, version, info_items))



class ComputerApplicationsUsage():

    @classmethod
    def getById(cls, id_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}/{2}_{3}'.format(__class__.__name__.lower(), id_item, start_date, en_date))

    @classmethod
    def getByName(cls, name_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/name/{1}/{2}_{3}'.format(__class__.__name__.lower(), name_item, start_date, en_date))

    @classmethod
    def getByUdid(cls, udid_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}/{2}_{3}'.format(__class__.__name__.lower(), udid_item, start_date, en_date))
    
    @classmethod
    def getBySerial(cls, serial_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/serialnumber/{1}/{2}_{3}'.format(__class__.__name__.lower(), serial_item, start_date, en_date))

    @classmethod
    def getByMac(cls, mac_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/macaddress/{1}/{2}_{3}'.format(__class__.__name__.lower(), mac_item, start_date, en_date))

class ComputerCheckin():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

class ComputerCommands(Basic_object):

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))
    
    @classmethod
    def getByStatus(cls, status_item):
        '''Return Advanced searches'''
        return get_call('{0}/status/{1}'.format(__class__.__name__.lower(), status_item))
    

class ComputerConfigurations(Basic_object):
    pass


class ComputerExtensionAttributes(Basic_object):
    pass


class ComputerGroups(Basic_object):
    pass

class ComputerHardwareSoftwareReports():
    
    @classmethod
    def getById(cls, id_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}/{2}_{3}'.format(__class__.__name__.lower(), id_item, start_date, en_date))

    @classmethod
    def getByIdSubset(cls, id_item, start_date, en_date, subset_items):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}/{2}_{3}/subset/{4}'.format(__class__.__name__.lower(), id_item, start_date, en_date, subset_items))

    @classmethod
    def getByName(cls, name_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/name/{1}/{2}_{3}'.format(__class__.__name__.lower(), name_item, start_date, en_date))

    @classmethod
    def getByUdid(cls, udid_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}/{2}_{3}'.format(__class__.__name__.lower(), udid_item, start_date, en_date))
    
    @classmethod
    def getBySerial(cls, serial_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/serialnumber/{1}/{2}_{3}'.format(__class__.__name__.lower(), serial_item, start_date, en_date))

    @classmethod
    def getByMac(cls, mac_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/macaddress/{1}/{2}_{3}'.format(__class__.__name__.lower(), mac_item, start_date, en_date))

class ComputerHistory():
    
    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(),item_type, item, subset_items))

    @classmethod
    def getByName(cls, name_item):
        '''Return Advanced searches'''
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))
    
    @classmethod
    def getBySerial(cls, serial):
        '''Return Advanced searches'''
        return get_call('{0}/serialnumber/{1}'.format(__class__.__name__.lower(), serial))
    
    @classmethod
    def getByMac(cls, mac_address):
        '''Return Advanced searches'''
        return get_call('{0}/macaddress/{1}'.format(__class__.__name__.lower(), mac_address))

class ComputerInventoryCollection():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())


class ComputerInvitations():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByInvitation(cls, invitation_item):
        return get_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item))


class ComputerManagement():
   
    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))
    
    @classmethod
    def getByIdUsername(cls, id_item, username):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}/username/{2}'.format(__class__.__name__.lower(), id_item, username))

    @classmethod
    def getByIdPatchFilter(cls, id_item, filter_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}/patchfilter/{2}/'.format(__class__.__name__.lower(), id_item, filter_item))
    
    @classmethod
    def getSubsetByUsername(cls, username, item_types, item, subset_items):
        '''Return Advanced searches'''
        return get_call('{0}/{1}/{2}/username/{3}/subset/{4}'.format(__class__.__name__.lower(), item_types, item,username, subset_items))

    @classmethod
    def getByName(cls, name_item):
        '''Return Advanced searches'''
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))
    
    @classmethod
    def getBySerial(cls, serial):
        '''Return Advanced searches'''
        return get_call('{0}/serialnumber/{1}'.format(__class__.__name__.lower(), serial))
    
    @classmethod
    def getByMac(cls, mac_address):
        '''Return Advanced searches'''
        return get_call('{0}/macaddress/{1}'.format(__class__.__name__.lower(), mac_address))


class ComputerReports(Basic_object):
    pass

class Computers():
    
    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())
    
    @classmethod
    def getMoreInfo(cls):
        '''Return Advanced searches'''
        return get_call('{}/subset/basic'.format(__class__.__name__.lower()))

    @classmethod
    def getByMatch(cls, match_item):
        '''Return Advanced searches'''
        return get_call('{0}/match/{1}'.format(__class__.__name__.lower(), match_item))

    @classmethod
    def getByMatchName(cls, match_name):
        '''Return Advanced searches'''
        return get_call('{0}/match/name/{1}'.format(__class__.__name__.lower(), match_name))

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))
    
    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))

    @classmethod
    def getByName(cls, name_item):
        '''Return Advanced searches'''
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))
    
    @classmethod
    def getBySerial(cls, serial_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/serialnumber/{1}/{2}_{3}'.format(__class__.__name__.lower(), serial_item, start_date, en_date))

    @classmethod
    def getByMac(cls, mac_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call('{0}/macaddress/{1}/{2}_{3}'.format(__class__.__name__.lower(), mac_item, start_date, en_date))


class Departments(Basic_object):
    pass


class DirectoryBindings(Basic_object):
    pass


class DiskEncryptionConfigurations(Basic_object):
    pass


class DistributionPoints(Basic_object):
    pass


class DockItems(Basic_object):
    pass

class Ebooks(Basic_object):

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))




class FileUploads():
    ''' Only post method '''
    pass


class GsxConnexion():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

class HealthCareListener():
    
    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

class HealthCareListenerRule():
    
    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


class Ibeacons(Basic_object):
    pass

class InfrastructureManager():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


class JsonWebTokenConfigurations():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


class LdapServers():
    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getUser(cls, server_item, user_name):
        '''Return Advanced searches'''
        if type(server_item) == int:
            return get_call('{0}/id/{1}/user/{2}'.format(__class__.__name__.lower(), server_item, user_name))
        else:
            return get_call('{0}/name/{1}/user/{2}'.format(__class__.__name__.lower(), server_item, user_name))

    @classmethod
    def getByGroup(cls, server_item, group_name):
        '''Return Advanced searches'''
        if type(server_item) == int:
            return get_call('{0}/id/{1}/group/{2}'.format(__class__.__name__.lower(), server_item, group_name))
        else:
            return get_call('{0}/name/{1}/group/{2}'.format(__class__.__name__.lower(), server_item, group_name))

    @classmethod
    def getUserByGroup(cls, server_item, group_name, user_name):
        '''Return Advanced searches'''
        if type(server_item) == int:
            return get_call('{0}/id/{1}/group/{2}/user/{3}'.format(__class__.__name__.lower(), server_item, group_name, user_name))
        else:
            return get_call('{0}/name/{1}/group/{2}/user/{3}'.format(__class__.__name__.lower(), server_item, group_name, user_name))



class LicencedSoftware(Basic_object):
    pass

class LogFlush():
    ''' only delete'''
    pass


class MacApplications(Basic_object):

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))


class ManagedPreferenceProfiles(Basic_object):

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))

class MobileDeviceApplications(Basic_object):
    
    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))

    @classmethod
    def getByBundleid(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/bundleid/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByBundleid_version(cls, id_item, version_item):
        '''Return Advanced searches'''
        return get_call('{0}/bundleid/{1}/version/{2}'.format(__class__.__name__.lower(), id_item, version_item))

class MobileDeviceCommands(Basic_object):

    @classmethod
    def getByUdid(cls, udid):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid))

    @classmethod
    def getByCommand(cls, command):
        '''Return Advanced searches'''
        return get_call('{0}/command/{1}'.format(__class__.__name__.lower(), command))


class MobileDeviceConfigurationProfiles(Basic_object):

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))


class MobileDeviceEnrollementProfiles(Basic_object):

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))

    @classmethod
    def getByInvitation(cls, invitation):
        '''Return Advanced searches'''
        return get_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation))


class MobileDeviceExtensionAttributes(Basic_object):
    pass


class MobileDeviceGroups(Basic_object):
    pass

class MobileDeviceHistory():
    
    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        '''Return Advanced searches'''
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))

    @classmethod
    def getBySerial(cls, serial):
        '''Return Advanced searches'''
        return get_call('{0}/serialnumber/{1}'.format(__class__.__name__.lower(), serial))

    @classmethod
    def getByMac(cls, mac_address):
        '''Return Advanced searches'''
        return get_call('{0}/macaddress/{1}'.format(__class__.__name__.lower(), mac_address))




class MobileDeviceInvitations():
    
    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByInvitation(cls, invitation_item):
        return get_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item))


class MobileDeviceProvisionningProfiles(Basic_object):
    
    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))

class MobileDevices():
    pass


class NetbootServers(Basic_object):
    pass


class NetworkSegments(Basic_object):
    pass

class OsxConfigurationProfiles():
    pass


class Packages(Basic_object):
    pass


class Patches():
    pass


class PatchExternalSources(Basic_object):
    pass


class PatchInternalSources(Basic_object):
    pass

class PatchPolicies():
    
    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getSubset(cls, id_item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/id/{1}/subset/{2}'.format(__class__.__name__.lower(), id_item, subset_items))

    @classmethod
    def getBySoftwareConfigId(cls, id_item):
        return get_call('{0}/softwaretitleconfigid/id/{1}'.format(__class__.__name__.lower(), id_item))

class Peripherals():
    
    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getSubset(cls, id_item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/id/{1}/subset/{2}'.format(__class__.__name__.lower(), id_item, subset_items))



class PeripheralsTypes():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


class Policies(Basic_object):

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))

    @classmethod
    def getByCategory(cls, category):
        return get_call('{0}/category/{1}'.format(__class__.__name__.lower(), category))

    @classmethod
    def getByCreator(cls, creator_name):
        return get_call('{0}/createdBy/{1}'.format(__class__.__name__.lower(), creator_name))


class Printers(Basic_object):
    pass


class RemovableMacAddresses(Basic_object):
    pass


class RestrictedSoftware(Basic_object):
    pass

class SavedSearches():
    pass


class Scripts(Basic_object):
    pass


class Sites(Basic_object):
    pass

class SmtpServer():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())


class SoftwareUpdateServers(Basic_object):
    pass


class UserExtensionAttributes(Basic_object):
    pass


class UserGroups(Basic_object):
    pass

class Users():
    pass


class VppAccounts():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


class VppAssignments():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


class VppInvitations():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getSubset(cls, item, subset_items):
        return get_call('{0}/id/{1}/subset/{2}'.format(__class__.__name__.lower(), item, subset_items))


class Webhooks(Basic_object):
    pass
