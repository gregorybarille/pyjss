import json
import inspect


from pyjss.api_calls import delete_call, get_call, push_call, put_call
from pyjss.settings import Credentials

from pyjss.parse_engine import (get_no_parameter, get_by_field)

class Accounts():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getByUserId(cls, useriD):
        return get_call('{0}/userid/{1}'.format(__class__.__name__.lower(),useriD))

    @classmethod
    def putByUserId(cls, useriD, payload):
        return put_call('{0}/userid/{1}'.format(__class__.__name__.lower(),useriD), payload)

    @classmethod
    def pushByUserId(cls, useriD, payload):
        return push_call('{0}/userid/{1}'.format(__class__.__name__.lower(), useriD), payload)

    @classmethod
    def deleteBUserId(cls, useriD):
        return delete_call('{0}/userid/{1}'.format(__class__.__name__.lower(), useriD))

    @classmethod
    def getByUserName(cls, userName):
        return get_call('{0}/username/{1}'.format(__class__.__name__.lower(), userName))
    
    @classmethod
    def putByUserName(cls, userName, payload):
        return put_call('{0}/username/{1}'.format(__class__.__name__.lower(), userName), payload)

    @classmethod
    def pushByUserName(cls, userName, payload):
        return push_call('{0}/username/{1}'.format(__class__.__name__.lower(), userName), payload)

    @classmethod
    def deleteByUserName(cls, userName):
        return delete_call('{0}/username/{1}'.format(__class__.__name__.lower(), userName))

    @classmethod
    def getByGroupId(cls, groupID):
        return get_call('{0}/groupid/{1}'.format(__class__.__name__.lower(), groupID))
    
    @classmethod
    def putByGroupId(cls, groupID, payload):
        return put_call('{0}/groupid/{1}'.format(__class__.__name__.lower(), groupID), payload)
    
    @classmethod
    def pushByGroupId(cls, groupID, payload):
        return push_call('{0}/groupid/{1}'.format(__class__.__name__.lower(), groupID), payload)

    @classmethod
    def deleteByGroupId(cls, groupID):
        return delete_call('{0}/groupid/{1}'.format(__class__.__name__.lower(), groupID))

    @classmethod
    def getByGroupName(cls, groupName):
        return get_call('{0}/groupname/{1}'.format(__class__.__name__.lower(), groupName))
    
    @classmethod
    def putByGroupName(cls, groupName, payload):
        return put_call('{0}/groupname/{1}'.format(__class__.__name__.lower(), groupName), payload)

    @classmethod
    def pushByGroupName(cls, groupName, payload):
        return push_call('{0}/groupname/{1}'.format(__class__.__name__.lower(), groupName), payload)

    @classmethod
    def deleteByGroupName(cls, groupName):
        return delete_call('{0}/groupname/{1}'.format(__class__.__name__.lower(), groupName))


class ActivationCode():

    @classmethod
    def get(cls):
        '''Return Activation Code'''
        return get_call(__class__.__name__.lower())
    
    @classmethod
    def put(cls, activation_code):
        '''Return Activation Code'''
        return put_call(__class__.__name__.lower(), activation_code)


class AdvancedComputerSearches():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class AdvancedMobileDeviceSearches():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

class AdvancedUserSearches():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

class AllowedFileExtension():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))
    
    @classmethod
    def getByExtension(cls, extension):
        return get_call('{0}/extension/{1}'.format(__class__.__name__.lower(), extension))
    
    @classmethod
    def putByExtension(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByExtension(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteByExtension(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))



class Buildings():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class ByoProfiles():
    '''verify basic object'''
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)
    
    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getBysiteId(cls, siteID):
        return get_call('{0}/siteid/{1}'.format(__class__.__name__.lower(), siteID))

    @classmethod
    def putBysiteId(cls, siteID, data):
        return put_call('{0}/siteid/{1}'.format(__class__.__name__.lower(), siteID), data)

    @classmethod
    def getBySiteName(cls, siteName):
        return get_call('{0}/sitename/{1}'.format(__class__.__name__.lower(), siteName))

    @classmethod
    def putBySiteName(cls, siteName, data):
        return put_call('{0}/sitename/{1}'.format(__class__.__name__.lower(), siteName), data)

class Categories():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class Classes():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


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



class ComputerApplicationUsage():

    @classmethod
    def getById(cls, id_item, start_date, en_date):
        '''Return Advanced searches'''
        print('{0}/id/{1}/{2}_{3}'.format(__class__.__name__.lower(),
                                          id_item, start_date, en_date))
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
        ''''''
        return get_call(__class__.__name__.lower())

    @classmethod
    def put(cls, checkin):
        ''''''
        return put_call(__class__.__name__.lower(), checkin)

class ComputerCommands():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    

class ComputerConfigurations():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class ComputerExtensionAttributes():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class ComputerGroups():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


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
        '''Return Activation Code'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def put(cls, settings):
        '''Return Activation Code'''
        return put_call(__class__.__name__.lower(), settings)


class ComputerInvitations():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getByInvitation(cls, invitation_item):
        return get_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item))
    
    @classmethod
    def pushByInvitation(cls, invitation_item, data):
        return push_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item), data)

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


class ComputerReports():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class Computers():
    
    @classmethod
    def getListID(cls):
        '''Return list of accounts'''
        data = get_call(__class__.__name__.lower())
        computer_list = []
        for computer in data['computers']:
            computer_list.append(computer['id'])
        return computer_list
    
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
    
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
    def putByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return put_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item), data)

    @classmethod
    def pushByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return push_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item), data)

    @classmethod
    def deleteByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return delete_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))

    @classmethod
    def getBySerial(cls, serial_item):
        '''Return Advanced searches'''
        return get_call('{0}/serialnumber/{1}'.format(__class__.__name__.lower(), serial_item))

    @classmethod
    def putBySerial(cls, serial_item, data):
        '''Return Advanced searches'''
        return put_call('{0}/serialnumber/{1}'.format(__class__.__name__.lower(), serial_item), data)

    @classmethod
    def pushBySerial(cls, serial_item, data):
        '''Return Advanced searches'''
        return push_call('{0}/serialnumber/{1}'.format(__class__.__name__.lower(), serial_item), data)

    @classmethod
    def deleteBySerial(cls, serial_item):
        '''Return Advanced searches'''
        return get_call('{0}/serialnumber/{1}'.format(__class__.__name__.lower(), serial_item))

    @classmethod
    def getByMac(cls, mac_item):
        '''Return Advanced searches'''
        return get_call('{0}/macaddress/{1}'.format(__class__.__name__.lower(), mac_item))

    @classmethod
    def putByMac(cls, mac_item, data):
        '''Return Advanced searches'''
        return put_call('{0}/macaddress/{1}'.format(__class__.__name__.lower(), mac_item), data)

    @classmethod
    def pushByMac(cls, mac_item, data):
        '''Return Advanced searches'''
        return push_call('{0}/macaddress/{1}'.format(__class__.__name__.lower(), mac_item), data)

    @classmethod
    def deleteByMac(cls, mac_item):
        '''Return Advanced searches'''
        return get_call('{0}/macaddress/{1}'.format(__class__.__name__.lower(), mac_item))



class Departments():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class DirectoryBindings():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class DiskEncryptionConfigurations():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class DistributionPoints():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class DockItems():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

class Ebooks():
    
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

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
        ''''''
        return get_call(__class__.__name__.lower())

    @classmethod
    def put(cls, settings):
        ''''''
        return put_call(__class__.__name__.lower(), settings)

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


class Ibeacons():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

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


class LdapServers():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

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



class LicencedSoftware():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

class LogFlush():

    @classmethod
    def deleteAllPolicies(cls, interval):
        '''For interval the supported values are a combination of [Zero, One, Two, Three, Six] and [Days, Weeks, Months, Years].'''
        return delete_call('{0}/policy/interval/{1}'.format(__class__.__name__.lower(), interval))
    
    @classmethod
    def deletePolicy(cls, id_item, interval):
        '''For interval the supported values are a combination of [Zero, One, Two, Three, Six] and [Days, Weeks, Months, Years].'''
        return delete_call('{0}/policy/id/{1}/interval/{2}'.format(__class__.__name__.lower(), id_item, interval))


class MacApplications():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))


class ManagedPreferenceProfiles():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))


class MobileDeviceApplications():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

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

class MobileDeviceCommands():
    
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
    @classmethod
    def getByUdid(cls, udid):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid))

    @classmethod
    def getByCommand(cls, command):
        '''Return Advanced searches'''
        return get_call('{0}/command/{1}'.format(__class__.__name__.lower(), command))


class MobileDeviceConfigurationProfiles():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))


class MobileDeviceEnrollementProfiles():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

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


class MobileDeviceExtensionAttributes():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class MobileDeviceGroups():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

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

class MobileDeviceProvisionningProfiles():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
        
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


class MobileDevices():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
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



class NetbootServers():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class NetworkSegments():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class OsxConfigurationProfiles():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))


class Packages():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class Patches():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
    @classmethod
    def getByBersion(cls, item_type, item, version):
        '''Item_type could be id/name'''
        return get_call('{0}/{1}/{2}/versopm/{3}'.format(__class__.__name__.lower(), item_type, item, version))
    pass


class PatchExternalSources():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class PatchInternalSources():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

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


class Policies():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
        
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


class Printers():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class RemovableMacAddresses():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class RestrictedSoftware():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

class SavedSearches():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class Scripts():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class Sites():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

class SmtpServer():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())


class SoftwareUpdateServers():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class UserExtensionAttributes():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class UserGroups():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class Users():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
    
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


class Webhooks():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def pushById(cls, id_item, data):
        return push_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def pushByName(cls, name_item, data):
        return push_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
