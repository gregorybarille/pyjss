from pyjss.api_calls import delete_call, get_call, post_call, put_call
from pyjss.templates import default_policy_template, default_scope_template


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
    def postByUserId(cls, useriD, payload):
        return post_call('{0}/userid/{1}'.format(__class__.__name__.lower(), useriD), payload)

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
    def postByUserName(cls, userName, payload):
        return post_call('{0}/username/{1}'.format(__class__.__name__.lower(), userName), payload)

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
    def postByGroupId(cls, groupID, payload):
        return post_call('{0}/groupid/{1}'.format(__class__.__name__.lower(), groupID), payload)

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
    def postByGroupName(cls, groupName, payload):
        return post_call('{0}/groupname/{1}'.format(__class__.__name__.lower(), groupName), payload)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByExtension(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)
    
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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)


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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getByInvitation(cls, invitation_item):
        return get_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item))
    
    @classmethod
    def postByInvitation(cls, invitation_item, data):
        return post_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item), data)

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
        # type: () -> object
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return post_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item), data)

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
    def postBySerial(cls, serial_item, data):
        '''Return Advanced searches'''
        return post_call('{0}/serialnumber/{1}'.format(__class__.__name__.lower(), serial_item), data)

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
    def postByMac(cls, mac_item, data):
        '''Return Advanced searches'''
        return post_call('{0}/macaddress/{1}'.format(__class__.__name__.lower(), mac_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    """ to do """
    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)


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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)


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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class LogFlush():
    ''' to be done'''
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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))


class MobileDeviceApplications():

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name or bundleid'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))

    @classmethod
    def getByBundleid(cls, id_item):
        '''Return Advanced searches'''
        return get_call('{0}/bundleid/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def putByBundleid(cls, id_item, data):
        '''Return Advanced searches'''
        return put_call('{0}/bundleid/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteByBundleid(cls, id_item):
        '''Return Advanced searches'''
        return delete_call('{0}/bundleid/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByBundleid_version(cls, id_item, version_item):
        '''Return Advanced searches'''
        return get_call('{0}/bundleid/{1}/version/{2}'.format(__class__.__name__.lower(), id_item, version_item))

    @classmethod
    def putByBundleid_version(cls, id_item, version_item, data):
        '''Return Advanced searches'''
        return put_call('{0}/bundleid/{1}/version/{2}'.format(__class__.__name__.lower(), id_item, version_item), data)

    @classmethod
    def deleteByBundleid_version(cls, id_item, version_item):
        '''Return Advanced searches'''
        return delete_call('{0}/bundleid/{1}/version/{2}'.format(__class__.__name__.lower(), id_item, version_item))


class MobileDeviceCommands():
    ''' post to be done '''
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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))


class MobileDeviceEnrollementProfiles():
    
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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name or invitation'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))

    @classmethod
    def getByInvitation(cls, invitation):
        '''Return Advanced searches'''
        return get_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation))

    @classmethod
    def putByInvitation(cls, invitation, data):
        '''Return Advanced searches'''
        return put_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation), data)

    @classmethod
    def postByInvitation(cls, invitation, data):
        '''Return Advanced searches'''
        return post_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber/macaddress'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))


class MobileDeviceInvitations():
    
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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


    @classmethod
    def getByInvitation(cls, invitation_item):
        return get_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item))

    @classmethod
    def putByInvitation(cls, invitation_item, data):
        return put_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item), data)
    
    @classmethod
    def postByInvitation(cls, invitation_item, data):
        return post_call('{0}/invitation/{1}'.format(__class__.__name__.lower(), invitation_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))
    
    @classmethod
    def putByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return put_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item), data)

    @classmethod
    def postByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return post_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item), data)

    @classmethod
    def deleteByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return delete_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item))

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid'''
        return get_call('{0}/{1}/{2}/subset/{3}'.format(__class__.__name__.lower(), item_type, item, subset_items))


class MobileDevices():

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
    
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
    def postByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return post_call('{0}/udid/{1}'.format(__class__.__name__.lower(), udid_item), data)

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
    def postBySerial(cls, serial_item, data):
        '''Return Advanced searches'''
        return post_call('{0}/serialnumber/{1}'.format(__class__.__name__.lower(), serial_item), data)

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
    def postByMac(cls, mac_item, data):
        '''Return Advanced searches'''
        return post_call('{0}/macaddress/{1}'.format(__class__.__name__.lower(), mac_item), data)

    @classmethod
    def deleteByMac(cls, mac_item):
        '''Return Advanced searches'''
        return get_call('{0}/macaddress/{1}'.format(__class__.__name__.lower(), mac_item))


class NetbootServers():

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class PatchAvailableTitles():
    
    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/sourceid/{1}'.format(__class__.__name__.lower(), id_item))


class PatchExternalSources():

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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


class PatchReports():

    @classmethod
    def getById(cls, id_item):
        return get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        return get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getByVersion(cls, item_type, item, version):
        '''Item_type could be id/name'''
        return get_call('{0}/{1}/{2}/version/{3}'.format(__class__.__name__.lower(), item_type, item, version))


class PatchSoftwareTitles():
    
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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class PatchPolicies():

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))

    @classmethod
    def getSubset(cls, id_item, subset_items):
        '''Item_type could be id/name/'''
        return get_call('{0}/id/{1}/subset/{2}'.format(__class__.__name__.lower(), id_item, subset_items))

    @classmethod
    def getBySoftwareConfigId(cls, id_item):
        return get_call('{0}/softwaretitleconfigid/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def postBySoftwareConfigId(cls, id_item):
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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


class Policies():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        response = get_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))
        if type(response) == int:
            return response
        else:
            return Policy(response)

    @classmethod
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

    @classmethod
    def getByName(cls, name_item):
        response = get_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
        if type(response) == int:
            return response
        else:
            return Policy(response)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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

class Policy:

    def __init__(self, xml_data ):
        self.data = xml_data
        self._id = xml_data.policy.general.find('id', recursive=False)
        self._name = xml_data.policy.general.find('name', recursive=False)
        self._enabled = xml_data.policy.general.find('enabled', recursive=False)
        self._site = xml_data.policy.general.find('site',recursive=False)
        self._category = xml_data.policy.general.category
        self._trigger_checkin = xml_data.policy.general.find('trigger_checkin', recursive=False)
        self._trigger_enrollment_complete = xml_data.policy.general.find('trigger_enrollment_complete', recursive=False)
        self._trigger_login = xml_data.policy.general.find('trigger_login', recursive=False)
        self._trigger_logout = xml_data.policy.general.find('trigger_logout', recursive=False)
        self._trigger_network_state_changed = xml_data.policy.general.find('trigger_network_state_changed', recursive=False)
        self._trigger_startup = xml_data.policy.general.find('trigger_startup', recursive=False)
        self._trigger_other = xml_data.policy.general.find('trigger_other', recursive=False)
        self._offline = xml_data.policy.general.find('offline', recursive=False)
        self._frequency = xml_data.policy.general.find('frequency', recursive=False)
        self._target_drive = xml_data.policy.general.find('target_drive', recursive=False)
        self.packages = xml_data.policy.find('packages')
        self.scripts = xml_data.policy.find('scripts')
        self.printers = xml_data.policy.find('printers', recursive=False)
        self.bindings = xml_data.policy.find('directory_bindings')
        self.maintenance = xml_data.policy.find('maintenance')
        self._updateInventory = xml_data.policy.find('maintenance').find('recon')
        self._resetComputerName = xml_data.policy.find('maintenance').find('reset_name')
        self._installCachedPackages = xml_data.policy.find('maintenance').find('install_all_cached_packages')
        self._fixDiskPermissions = xml_data.policy.find('maintenance').find('permissions')
        self._fixByHost = xml_data.policy.find('maintenance').find('byhost')
        self._fixSystemCaches = xml_data.policy.find('maintenance').find('system_cache')
        self._fixUserCaches = xml_data.policy.find('maintenance').find('user_cache')
        self._verifyStartupDisk = xml_data.policy.find('maintenance').find('verify')
        self.files_processes = xml_data.policy.find('files_processes')
        self._search_by_path =xml_data.policy.find('files_processes').find('search_by_path')
        self._delete_file =xml_data.policy.find('files_processes').find('delete_file')
        self._search_by_filename =xml_data.policy.find('files_processes').find('filename')
        self._update_locate_database =xml_data.policy.find('files_processes').find('update_locate_database')
        self._search_spotlight =xml_data.policy.find('files_processes').find('spotlight_search')
        self._search_process =xml_data.policy.find('files_processes').find('search_for_process')
        self._kill_process = xml_data.policy.find('files_processes').find('kill_process')
        self._run_command = xml_data.policy.find('files_processes').find('run_command')
        self.scope = xml_data.policy.scope
        self.allcomputers = xml_data.policy.scope.all_computers
        self.computers = xml_data.policy.scope.computers
        self.computergroups = xml_data.policy.scope.computer_groups
        self.buildings = xml_data.policy.scope.buildings
        self.departments = xml_data.policy.scope.departments
        self.limitations = xml_data.policy.scope.limitations
        self.limitations_users = xml_data.policy.scope.limitations.users
        self.limitations_usergroups = xml_data.policy.scope.limitations.user_groups
        self.limitations.networksegments = xml_data.policy.scope.limitations.network_segments
        self.limitations.ibeacons = xml_data.policy.scope.limitations.ibeacons
        self.exclusions = xml_data.policy.scope.exclusions
        self.exclusions.computers = xml_data.policy.scope.exclusions.computers
        self.exclusions.computergroups = xml_data.policy.scope.exclusions.computer_groups
        self.exclusions.buildings = xml_data.policy.scope.exclusions.buildings
        self.exclusions.departments = xml_data.policy.scope.exclusions.departments
        self.exclusions.users = xml_data.policy.scope.exclusions.users
        self.exclusions.user_groups = xml_data.policy.scope.exclusions.user_groups
        self.exclusions.network_segments = xml_data.policy.scope.exclusions.network_segments
        self.exclusions.ibeacons = xml_data.policy.scope.exclusions.ibeacons

    def __repr__(self):
        return str(self.data.prettify())

    @property
    def name(self):
        return self._name.string

    @name.setter
    def name(self, value):
        self._name.string = value

    @property
    def id(self):
        return self._id.string

    @id.setter
    def id(self, value):
        self._id.string = value
    
    @property
    def enabled(self):
        return self._enabled.string

    @enabled.setter
    def enabled(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._enabled.string = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if type(value) == int:
            self._category.find('id').string = str(value)
            self._category.find('name').decompose()
        elif type(value) == str:
            try:
                self._category.find('name').string = value
            except AttributeError:
                new_tag = self.data.new_tag('name')
                new_tag.string = value
                self._category.append(new_tag)

    @category.deleter
    def category(self):
        self._category.find('id').string = '-1'
        self._category.find('name').string = 'None'
    
    @property
    def trigger_checkin(self):
        return self._trigger_checkin.string

    @trigger_checkin.setter
    def trigger_checkin(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_checkin.string = value

    @property
    def trigger_enrollment_complete(self):
        return self._trigger_checkin.string

    @trigger_enrollment_complete.setter
    def trigger_enrollment_complete(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_enrollment_complete.string = value
    
    @property
    def trigger_login(self):
        return self._trigger_login.string

    @trigger_login.setter
    def trigger_login(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_login.string = value

    @property
    def trigger_logout(self):
        return self._trigger_logout.string

    @trigger_logout.setter
    def trigger_logout(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_logout.string = value
    
    @property
    def trigger_network_state_changed(self):
        return self._trigger_network_state_changed.string

    @trigger_network_state_changed.setter
    def trigger_network_state_changed(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_network_state_changed.string = value

    @property
    def trigger_startup(self):
        return self._trigger_startup.string

    @trigger_startup.setter
    def trigger_startup(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_startup.string = value
    
    @property
    def trigger_other(self):
        return self._trigger_other.string
    
    @trigger_other.setter
    def trigger_other(self, value):
        self._trigger_other.string = value

    @trigger_other.deleter
    def trigger_other(self, value):
        del self._trigger_other

    @property
    def offline(self):
        return self._offline.string

    @offline.setter
    def offline(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._offline.string = value

    @property
    def frequency(self):
        return self._offline.string

    @frequency.setter
    def frequency(self, value):
        if value not in ['Once per computer', 'Once per user per computer', 'Once per user', 'Once every day', 'Once every week', 'Once every month', 'Ongoing']:
            raise ValueError
        else:
            self._frequency.string = value

    @property
    def target_drive(self):
        return self._target_drive.string

    @target_drive.setter
    def target_drive(self, value):
        self._target_drive.string = value

    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        if type(value) == int:
            print('test')
            self._site.find('id').string = str(value)
            self._site.find('name').decompose()
        elif type(value) == str:
            try:
                self._site.find('name').string = value
            except AttributeError:
                new_tag = self.data.new_tag('name')
                new_tag.string = value
                self._site.append(new_tag)
    @site.deleter
    def site(self):
        self._site.find('id').string = '-1'
        self._site.find('name').string = 'None'

    @property
    def updateInventory(self):
        return self._updateInventory.string

    @updateInventory.setter
    def updateInventory(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._updateInventory.string = value
    
    @property
    def resetComputerName(self):
        return self._resetComputerName.string

    @resetComputerName.setter
    def resetComputerName(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._resetComputerName.string = value

    @property
    def installCachedPackage(self):
        return self._installCachedPackages.string

    @installCachedPackage.setter
    def installCachedPackage(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._installCachedPackages.string = value

    @property
    def fixDiskPermissions(self):
        return self._offline.string

    @fixDiskPermissions.setter
    def fixDiskPermissions(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._fixDiskPermissions.string = value

    @property
    def fixByHost(self):
        return self._fixByHost.string

    @fixByHost.setter
    def fixByHost(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._fixByHost.string = value

    @property
    def fixSystemCaches(self):
        return self._fixSystemCaches.string

    @fixSystemCaches.setter
    def fixSystemCaches(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._fixSystemCaches.string = value

    @property
    def fixUserCaches(self):
        return self._fixUserCaches.string

    @fixUserCaches.setter
    def fixUserCaches(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._fixUserCaches.string = value

    @property
    def verifyStartupDisk(self):
        return self._verifyStartupDisk.string

    @verifyStartupDisk.setter
    def verifyStartupDisk(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._verifyStartupDisk.string = value

    @property
    def search_by_path(self):
        return self._search_by_path.string

    @search_by_path.setter
    def search_by_path(self, value):
        self._search_by_path.string = value

    @property
    def delete_file(self):
        return self._search_by_path.string

    @delete_file.setter
    def delete_file(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._delete_file.string = value

    @property
    def search_by_filename(self):
        return self._search_by_filename.string

    @search_by_filename.setter
    def search_by_filename(self, value):
        self._search_by_filename.string = value


    @property
    def update_locate_database(self):
        return self._update_locate_database.string

    @update_locate_database.setter
    def update_locate_database(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._update_locate_database.string = value

    @property
    def search_spotlight(self):
        return self._search_spotlight.string

    @search_spotlight.setter
    def search_spotlight(self, value):
        self._search_spotlight.string = value

    @property
    def search_process(self):
        return self._search_process.string

    @search_process.setter
    def search_process(self, value):
        self._search_process.string = value

    @property
    def kill_process(self):
        return self._kill_process.string

    @kill_process.setter
    def kill_process(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._kill_process.string = value
    
    @property
    def run_command(self):
        return self._run_command.string

    @run_command.setter
    def run_command(self, value):
        self._run_command.string = value

    def _create_tag(self, tag_name, arg):
        new_data_type = self.data.new_tag(tag_name)
        if type(arg) == int:
            new_sub_tag = self.data.new_tag('id')
        elif type(arg) == str:
            new_sub_tag = self.data.new_tag('name')
        new_sub_tag.string = str(arg)
        new_data_type.append(new_sub_tag)
        return new_data_type
    
    def _create_secondary_tag(self, tag_name, secondary_tag, secondary_arg, item):
        new_data_type = self.data.new_tag(tag_name)
        new_secondary_tag = self.data.new_tag(secondary_tag)
        if type(item) == int:
            new_sub_tag = self.data.new_tag('id')
        elif type(item) == str:
            new_sub_tag = self.data.new_tag('name')
        new_sub_tag.string = str(item)
        new_secondary_tag.string = str(secondary_arg)
        new_data_type.append(new_sub_tag)
        new_data_type.append(new_secondary_tag)
        return new_data_type

    def addComputers(self, *args):
        arg_tuple = tuple(filter(lambda x: not self.computers.find(string=x), args))
        list(map(lambda x: self.computers.append(self._create_tag('computer', x)), arg_tuple))

    def removeComputers(self, *args):
        list(map(lambda x: self.computers.find(string=x).find_parent('computer').decompose(), args))

    def addComputersGroups(self, *args):
        arg_tuple = tuple(filter(lambda x: not self.computergroups.find(string=x), args))
        list(map(lambda x: self.computergroups.append(self._create_tag('computer_group', x)), arg_tuple))

    def removeComputersGroups(self, *args):
        list(map(lambda x: self.computergroups.find(string=x).find_parent('computer_group').decompose(), args))

    def addBuildings(self, *args):
        arg_tuple = tuple(filter(lambda x: not self.buildings.find(string=x), args))
        list(map(lambda x: self.buildings.append(self._create_tag('building', x)), arg_tuple))

    def removeBuildings(self, *args):
        list(map(lambda x: self.buildings.find(string=x).find_parent('building').decompose(), args))

    def addDepartments(self, *args):
        arg_tuple = tuple(filter(lambda x: not self.departments.find(string=x), args))
        list(map(lambda x: self.departments.append(self._create_tag('department', x)), arg_tuple))

    def removeDepartments(self, *args):
        list(map(lambda x: self.buildings.find(string=x).find_parent('department').decompose(), args))

    def excludeComputers(self, *args):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.computers.find(string=x), args))
        list(map(lambda x: self.exclusions.computers.append(self._create_tag('computer', x)), arg_tuple))

    def removeExcludedComputers(self, *args):
        list(map(lambda x: self.exclusions.computers.find(string=x).find_parent('computer').decompose(), args))
    
    def excludeComputersGroups(self, *args):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.computergroups.find(string=x), args))
        list(map(lambda x: self.exclusions.computergroups.append(self._create_tag('computer_group', x)), arg_tuple))

    def removeExcludedComputersGroups(self, *args):
        list(map(lambda x: self.exclusions.computergroups.find(string=x).find_parent('computer_group').decompose(), args))

    def excludeBuildings(self, *args):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.buildings.find(string=x), args))
        list(map(lambda x: self.exclusions.buildings.append(self._create_tag('building', x)), arg_tuple))

    def removeExcludedBuildings(self, *args):
        list(map(lambda x: self.exclusions.buildings.find(string=x).find_parent('building').decompose(), args))

    def excludeDepartments(self, *args):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.departments.find(string=x), args))
        list(map(lambda x: self.exclusions.departments.append(self._create_tag('department', x)), arg_tuple))

    def removeExcludedDepartments(self, *args):
        list(map(lambda x: self.exclusions.departments.find(string=x).find_parent('department').decompose(), args))
    
    def clear_scope(self):
        #To correct
        return self.data.find('scope').replace_with(default_scope_template)
    
    def addScripts(self, **kwargs):
        [ self.scripts.append(self._create_secondary_tag( 'script', 'priority', x,y)) for x, y in kwargs.items() ]

    def removeScripts(self, *args):
        list(map(lambda x: self.scripts.find(string=x).find_parent('script').decompose(), args))
    
    def addPackages(self, **kwargs):
        [ self.packages.append(self._create_secondary_tag( 'package', 'action', x,y)) for x, y in kwargs.items() ]

    def removePackages(self, *args):
        list(map(lambda x: self.scripts.find(string=x).find_parent('package').decompose(), args))

    def mapPrinters(self, *args): 
        arg_tuple = tuple(filter(lambda x: not self.printers.find(string=x), args))
        list(map(lambda x: self.printers.append(self._create_secondary_tag('printer', 'action', 'install', x)), arg_tuple))

    def unmapPrinters(self, *args):
        arg_tuple = tuple(filter(lambda x: not self.printers.find(string=x), args))
        list(map(lambda x: self.printers.append(self._create_secondary_tag('printer', 'action', 'uninstall', x)), arg_tuple))

    def removePrinters(self, *args):
        list(map(lambda x: self.printers.find(string=x).find_parent('printer').decompose(), args))
    
    def addBinding(self, *args):
        arg_tuple = tuple(filter(lambda x: not self.bindings.find(string=x), args))
        list(map(lambda x: self.bindings.append(self._create_tag('binding', x)), arg_tuple))

    def removeBindings(self, *args):
        list(map(lambda x: self.bindings.find(string=x).find_parent('binding').decompose(), args))

    def update(self):
        return Policies.putById(str(self.id), str(self.data))
    
    def delete(self):
        return Policies.deleteById(str(self.id))


class Printers():

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))


class SmtpServer():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def put(cls, server):
        ''''''
        return put_call(__class__.__name__.lower(), server)


class SoftwareUpdateServers():

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
    
    @classmethod
    def getByEmail(cls, email):
        return get_call('{0}/email/{1}'.format(__class__.__name__.lower(), email))


class VppAccounts():

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


class VppAssignments():

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))


class VppInvitations():

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
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item))

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
    def putById(cls, id_item, data):
        return put_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call('{0}/id/{1}'.format(__class__.__name__.lower(), id_item), data)

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
    def postByName(cls, name_item, data):
        return post_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item), data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call('{0}/name/{1}'.format(__class__.__name__.lower(), name_item))
