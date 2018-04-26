from pyjss.api_calls import get_call,delete_call,push_call
from pyjss.settings import Credentials
import json

class Accounts:
    
    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/accounts')
        else:
            if type(item) is str:
                data = get_call('JSSResource/accounts/username/{0}'.format(item))
            if type(item) is int:
                data = get_call('JSSResource/accounts/userid/{0}'.format(item))
        return(data)

class ActivationCode:

    @staticmethod
    def get():
        data = get_call('JSSResource/activationcode')
        print(data)


class AdvancedComputerSearches:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/advancedcomputersearches')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/advancedcomputersearches/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/advancedcomputersearches/id/{0}'.format(item))
        print(data) 


class AdvancedMobileDeviceSearches:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/advancedmobiledevicesearches')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/advancedcomputersearches/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/advancedcomputersearches/id/{0}'.format(item))
        print(data)


class AdvancedUserSearches:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/advancedusersearches')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/advancedusersearches/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/advancedusersearches/id/{0}'.format(item))
        print(data)

class AllowedFileExtension:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/allowedfileextensions')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/allowedfileextensions/extension/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/allowedfileextensions/id/{0}'.format(item))
        print(data)


class Buildings:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/buildings')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/buildings/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/buildings/id/{0}'.format(item))
        print(data)
        

class ByoProfiles:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/byoprofiles')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/byoprofiles/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/byoprofiles/id/{0}'.format(item))
        print(data)


class Categories:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/categories')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/categories/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/categories/id/{0}'.format(item))
        print(data)


class Classes:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/classes')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/classes/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/classes/id/{0}'.format(item))
        print(data)


class CommandFlush:
    pass


class ComputerApplications:
    pass


class ComputerApplicationsUsage:
    pass


class ComputerCheckin:

    @staticmethod
    def get():
        data = get_call('JSSResource/computercheckin')
        print(data)


class ComputerCommands:
    pass


class ComputerConfigurations:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/computerconfigurations')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/computerconfigurations/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/computerconfigurations/id/{0}'.format(item))
        print(data)


class ComputerExtensionAttributes:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/computerextensionattributes')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/computerextensionattributes/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/computerextensionattributes/id/{0}'.format(item))
        print(data)


class ComputerGroups:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/computergroups')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/computergroups/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/computergroups/id/{0}'.format(item))
        print(data)

class ComputerHardwareSoftwareReports:
    pass


class ComputerHistory:
    pass


class ComputerInventoryCollection:

    @staticmethod
    def get():
        data = get_call('JSSResource/computerinventorycollection')
        print(data)


class ComputerInvitations:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/computerinvitations')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/computerinvitations/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/computerinvitations/id/{0}'.format(item))
        print(data)


class ComputerManagement:
    pass


class ComputerReports:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/computerreports')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/computerreports/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/computerreports/id/{0}'.format(item))
        print(data)

class Computers:
    pass


class Departments:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/departments')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/departments/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/departments/id/{0}'.format(item))
        print(data)


class DirectoryBindings:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/directorybindings')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/directorybindings/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/directorybindings/id/{0}'.format(item))
        print(data)


class DiskEncryptionConfigurations:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/diskencryptionconfigurations')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/diskencryptionconfigurations/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/diskencryptionconfigurations/id/{0}'.format(item))
        print(data)


class DistributionPoints:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/distributionpoints')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/distributionpoints/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/distributionpoints/id/{0}'.format(item))
        print(data)


class DockItems:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/dockitems')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/dockitems/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/dockitems/id/{0}'.format(item))
        print(data)


class Ebooks:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/ebooks')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/ebooks/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/ebooks/id/{0}'.format(item))
        print(data)


class FileUploads:
    pass


class GsxConnexion:

    @staticmethod
    def get():
        data = get_call('JSSResource/gsxconnection')
        print(data)


class HealthCareListener:
    pass

class HealthCareListenerRule:
    pass


class Ibeacons:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/ibeacons')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/ibeacons/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/ibeacons/id/{0}'.format(item))
        print(data)


class InfrastructureManager:

    @staticmethod
    def get():
        data = get_call('JSSResource/infrastructuremanager')
        print(data)


class JsonWebTokenConfigurations:

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
        print(data)



class LdapServers:
    pass


class LicencedSoftware:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/licensedsoftware')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/licensedsoftware/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/licensedsoftware/id/{0}'.format(item))
        print(data)


class LogFlush:
    pass


class MacApplications:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/macapplications')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/macapplications/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/macapplications/id/{0}'.format(item))
        print(data)


class ManagedPreferenceProfile:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/managedpreferenceprofiles')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/managedpreferenceprofiles/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/managedpreferenceprofiles/id/{0}'.format(item))
        print(data)


class MobileDeviceApplications:
    pass


class MobileDeviceCommands:
    pass


class MobileDeviceConfigurationProfiles:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/managedpreferenceprofiles')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/managedpreferenceprofiles/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/managedpreferenceprofiles/id/{0}'.format(item))
        print(data)

class MobileDeviceEnrollementProfiles:
    pass


class MobileDeviceExtensionAttributes:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/mobiledeviceextensionattributes')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/mobiledeviceextensionattributes/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/mobiledeviceextensionattributes/id/{0}'.format(item))
        print(data)


class MobileDeviceExtensionGroups:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/mobiledevicegroups')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/mobiledevicegroups/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/mobiledevicegroups/id/{0}'.format(item))
        print(data)


class MobileDeviceHistory:
    pass


class MobileDeviceInvitations:
    pass


class MobileDeviceProvisionningProfiles:
    pass

class MobileDevices:
    pass


class NetbootServers:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/netbootservers')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/netbootservers/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/netbootservers/id/{0}'.format(item))
        print(data)


class NetworkSegments:
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
            if type(item) is int:
                data = get_call('JSSResource/networksegments/id/{0}'.format(item))
        print(data)


class OsxConfigurationProfiles:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/osxconfigurationprofiles')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/osxconfigurationprofiles/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/osxconfigurationprofiles/id/{0}'.format(item))
        print(data)


class Packages:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/packages')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/packages/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/packages/id/{0}'.format(item))
        print(data)


class Patches:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/patches')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/patches/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/patches/id/{0}'.format(item))
        print(data)


class PatchExternalSources:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/patchexternalsources')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/patchexternalsources/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/patchexternalsources/id/{0}'.format(item))
        print(data)


class PatchInternalSources:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/patchinternalsources')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/patchinternalsources/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/patchinternalsources/id/{0}'.format(item))
        print(data)


class PatchPolicies:
    pass


class Peripherals:

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
        print(data)


class PeripheralsTypes:

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
        print(data)

class Policies:
    pass


class Printers:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/printers')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/printers/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/printers/id/{0}'.format(item))
        print(data)


class RemovableMacAddresses:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/removablemacaddresses')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/removablemacaddresses/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/removablemacaddresses/id/{0}'.format(item))
        print(data)


class RestrictedSoftware:

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
        print(data)


class SavedSearches:
    pass


class Stripts:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/scripts')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/scripts/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/scripts/id/{0}'.format(item))
        print(data)


class Sites:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/sites')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/sites/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/sites/id/{0}'.format(item))
        print(data)


class SmtpServer:

    @staticmethod
    def get():
        data = get_call('JSSResource/smtpserver')
        print(data)


class SoftwareUpdateServers:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/softwareupdateservers')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/sitsoftwareupdateserverses/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/softwareupdateservers/id/{0}'.format(item))
        print(data)


class UserExtensionAttributes:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/userextensionattributes')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/userextensionattributes/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/userextensionattributes/id/{0}'.format(item))
        print(data)


class UserGroups:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/usergroups')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/usergroups/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/usergroups/id/{0}'.format(item))
        print(data)


class Users:
    pass


class VppAccounts:

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
        print(data)


class VppAssignments:

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
        print(data)


class VppInvitations:

    @staticmethod
    def get(item_id=None):
        if item_id == None:
            data = get_call('JSSResource/vppinvitations')
        else:
            if type(item_id) is int:
                data = get_call(
                    'JSSResource/vppinvitations/id/{0}'.format(item_id))
            else:
                print('Item_ID should be an integer.')
        print(data)


class Webhooks:

    @staticmethod
    def get(item=None):
        if item == None:
            data = get_call('JSSResource/webhooks')
        else:
            if type(item) is str:
                data = get_call(
                    'JSSResource/webhooks/name/{0}'.format(item))
            if type(item) is int:
                data = get_call(
                    'JSSResource/webhooks/id/{0}'.format(item))
        print(data)
