import json
import inspect


from pyjss.api_calls import delete_call, get_call, push_call, put_call
from pyjss.settings import Credentials

from pyjss.parse_engine import (get_no_parameter, get_by_field)

class Basic_get_object():

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


class Basic_put_object():

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)


class Basic_push_object():

    @classmethod
    def putById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

class Basic_delete_object():

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
    

class Basic_object(Basic_get_object, Basic_put_object, Basic_push_object, Basic_delete_object):
    pass
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


    @classmethod
    def deleteByUserName(cls, userName):
        return delete_call('{0}/username/{1}'.format(__class__.__name__.lower(), userName))

    @classmethod
    def deleteBUserId(cls, useriD):
        return delete_call('{0}/userid/{1}'.format(__class__.__name__.lower(), useriD))

    @classmethod
    def deleteByGroupId(cls, groupID):
        return delete_call('{0}/groupid/{1}'.format(__class__.__name__.lower(), groupID))

    @classmethod
    def deleteByGroupName(cls, groupName):
        return delete_call('{0}/groupname/{1}'.format(__class__.__name__.lower(), groupName))


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

class AllowedFileExtension():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByExtension(cls, extension):
        return get_call('{0}/extension/{1}'.format(__class__.__name__.lower(), extension))
    
    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


class Buildings(Basic_object):
    pass


class ByoProfiles(Basic_object):
'''verify basic object'''
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

    @classmethod
    def deleteById(cls, group_type, id_items, status):
        '''group_type could be one of the following: computers, computergroups, mobiledevices, mobiledevicegroups
        id_items could a single or multiple value ( separated by comma )
        status could be one of the following: Pending, Failed or Pending+Failed
        '''
        return delete_call('{0}/{1}/id/{2}/status/{3}'.format(__class__.__name__.lower(),group_type,id_items, status))


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

class ComputerCommands(Basic_get_object):

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


class ComputerInvitations(Basic_object):

    @classmethod
    def getByInvitation(cls, invitation_item):
        return get_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item))
    
    @classmethod
    def deleteInvitation(cls, invitation_item):
        return delete_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item))



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


class ComputerReports(Basic_get_object):
    pass

class Computers(Basic_object):

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
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))

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

    @classmethod
    def deleteByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return delete_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))

    @classmethod
    def deleteBySerial(cls, serial_item, start_date, en_date):
        '''Return Advanced searches'''
        return delete_call('{0}/serialnumber/{1}/{2}_{3}'.format(__class__.__name__.lower(), serial_item, start_date, en_date))

    @classmethod
    def deleteByMac(cls, mac_item, start_date, en_date):
        '''Return Advanced searches'''
        return delete_call('{0}/macaddress/{1}/{2}_{3}'.format(__class__.__name__.lower(), mac_item, start_date, en_date))



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

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


class LdapServers(Basic_object):

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

    @classmethod
    def deleteAllPolicies(cls, interval):
        '''For interval the supported values are a combination of [Zero, One, Two, Three, Six] and [Days, Weeks, Months, Years].'''
        return delete_call('{0}/policy/interval/{1}'.format(__class__.__name__.lower(), interval))
    
    @classmethod
    def deletePolicy(cls, id_item, interval):
        '''For interval the supported values are a combination of [Zero, One, Two, Three, Six] and [Days, Weeks, Months, Years].'''
        return delete_call('{0}/policy/id/{1}/interval/{2}'.format(__class__.__name__.lower(), id_item, interval))


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

class MobileDeviceCommands(Basic_get_object):

    @classmethod
    def getByUdid(cls, udid):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid))

    @classmethod
    def getByCommand(cls, command):
        '''Return Advanced searches'''
        return get_call('{0}/command/{1}'.format(__class__.__name__.lower(), command))


class MobileDeviceConfigurationProfiles(Basic_get_object):

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

    @classmethod
    def deleteInvitation(cls, invitation):
        return delete_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation))


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

    @classmethod
    def deleteById(cls, id_item):
        '''Return Advanced searches'''
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByInvitation(cls, invitation_item):
        return delete_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item))

class MobileDeviceProvisionningProfiles(Basic_object):
    
    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))

    @classmethod
    def deleteByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return delete_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))


class MobileDevices(Basic_object):

    @classmethod
    def getByMatch(cls, match_item):
        '''Return Advanced searches'''
        return get_call('{0}/match/{1}'.format(__class__.__name__.lower(), match_item))
    
    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))

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

    @classmethod
    def deleteByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return delete_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))

    @classmethod
    def deleteBySerial(cls, serial_item, start_date, en_date):
        '''Return Advanced searches'''
        return delete_call('{0}/serialnumber/{1}/{2}_{3}'.format(__class__.__name__.lower(), serial_item, start_date, en_date))

    @classmethod
    def deleteByMac(cls, mac_item, start_date, en_date):
        '''Return Advanced searches'''
        return delete_call('{0}/macaddress/{1}/{2}_{3}'.format(__class__.__name__.lower(), mac_item, start_date, en_date))



class NetbootServers(Basic_object):
    pass


class NetworkSegments(Basic_object):
    pass


class OsxConfigurationProfiles(Basic_object):
    
    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))


class Packages(Basic_object):
    pass


class Patches(Basic_object):
    
    @classmethod
    def getByBersion(cls, item_type, item, version):
        '''Item_type could be id/name'''
        return get_call('{0}/{1}/{2}/versopm/{3}'.format(__class__.__name__.lower(), item_type, item, version))
    pass


class PatchExternalSources(Basic_object):
    pass


class PatchInternalSources(Basic_get_object):
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

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

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

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))



class PeripheralsTypes():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))
    
    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


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

class SavedSearches(Basic_get_object):
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


class UserGroups(Basic_get_object):
    pass


class Users(Basic_object):

    @classmethod
    def getByEmail(cls, email):
        return get_call('{0}/email/{1}'.format(__class__.__name__.lower(), email))


class VppAccounts():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

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
