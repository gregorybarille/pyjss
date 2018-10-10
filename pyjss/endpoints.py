endpoints = {
    'Accounts': {
        0: {
            'methods': ['get']
        },
        2: {
            'id': {
                'endpoint': '/userid/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/username/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'groupid': {
                'endpoint': '/groupid/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'groupname': {
                'endpoint': '/groupname/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'ActivationCode': {
        0: {
            'methods': ['get', 'put']
        }
    },
    'AdvancedComputerSearches': {
        0: {
            'methods': ['get']
        },
        2: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'AdvancedMobileDeviceSearches': {
        0: {
            'methods': ['get']
        },
        2: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'AdvancedUserSearches': {
        0: {
            'methods': ['get']
        },
        2: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'AllowedFileExtension': {
        0: {
            'methods': ['get']
        },
        2: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'extension': {
                'endpoint': '/extension/{0}',
                'methods': ['get']
            }
        }
    },
    'Buildings': {
        0: {
            'methods': ['get']
        },
        2: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'ByoProfiles': {
        0: {
            'methods': ['get']
        },
        2: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'siteid': {
                'endpoint': '/groupid/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'sitename': {
                'endpoint': '/groupname/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'Categories': {
        0: {
            'methods': ['get']
        },
        2: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'Classes': {
        0: {
            'methods': ['get']
        },
        2: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'ComputerApplications': {
        1: {
            'name': {
                'endpoint': '/application/{0}',
                'methods': ['get']
            }
        },
        2: {
            'inventory': {
                'endpoint': '/application/{0}/inventory/{1}',
                'methods': ['get']
            },
            'version': {
                'endpoint': '/application/{0}/version/{1}',
                'methods': ['get']
            }
        },
        3: {
            'name': {
                'endpoint': '/application/{0}/version/{1}/inventory/{2}',
                            'methods': ['get']
            }
        }
    },
    'ComputerApplicationsUsage': {
        3: {
            'id': {
                'endpoint': '/id/{0}/{1}',
                'methods': ['get']
            },
            'name': {
                'endpoint': '/name/{0}/{1}',
                'methods': ['get']
            },
            'udid': {
                'endpoint': '/udid/{0}/{1}',
                'methods': ['get']
            },
            'serialnumber': {
                'endpoint': '/serialnumber/{0}/{1}',
                'methods': ['get']
            },
            'macaddress': {
                'endpoint': '/macaddress/{0}/{1}',
                'methods': ['get']
            }
        }
    },
    'ComputerCheckin': {
        0: {
            'methods': ['get', 'put']
        }
    },
    'ComputerCommands': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get']
            }
        },
        2: {
            'uuid': {
                'endpoint': '/uuid/{0}',
                'methods': ['get']
            },
            'statusuuid': {
                'endpoint': '/statusuuid/{0}',
                'methods': ['get']
            },
            'command': {
                'endpoint': '/command/{0}',
                'methods': ['post']
            }
        },
        3: {
            'command': {
                'endpoint': '/command/{0}/id/{1}',
                'methods': ['get']
            },
            'statusuuid': {
                'endpoint': '/statusuuid/{0}',
                'methods': ['get']
            }
        },
        4: {
            'command': {
                'endpoint': '/command/{0}/passcode/{1}/id/{2}',
                'methods': ['get']
            }
        }
    },
    'ComputerConfigurations': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'ComputerExtensionAttributes': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'ComputerGroups': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'ComputerHardwareSoftwareReports': {
        3: {
            'id': {
                'endpoint': '/id/{0}/{1}',
                'methods': ['get']
            },
            'name': {
                'endpoint': '/name/{0}/{1}',
                'methods': ['get']
            },
            'udid': {
                'endpoint': '/udid/{0}/{1}',
                'methods': ['get']
            },
            'serialnumber': {
                'endpoint': '/serialnumber/{0}/{1}',
                'methods': ['get']
            },
            'macaddress': {
                'endpoint': '/macaddress/{0}/{1}',
                'methods': ['get']
            }
        },
        4: {
            'id': {
                'endpoint': '/id/{0}/{1}/subset/{2}',
                'methods': ['get']
            }
        }
    },
    'ComputerHistory': {
        2: {
            'id': {
                'endpoint': '/id/{0}/{1}',
                'methods': ['get']
            },
            'name': {
                'endpoint': '/name/{0}/{1}',
                'methods': ['get']
            },
            'udid': {
                'endpoint': '/udid/{0}/{1}',
                'methods': ['get']
            },
            'serialnumber': {
                'endpoint': '/serialnumber/{0}/{1}',
                'methods': ['get']
            },
            'macaddress': {
                'endpoint': '/macaddress/{0}/{1}',
                'methods': ['get']
            }
        },
        3: {
            'id': {
                'endpoint': '/id/{0}/subset/{1}',
                'methods': ['get']
            }
        }
    },
    'ComputerInventoryCollection': {
        0: {
            'methods': ['get', 'put']
        }
    },
    'ComputerInvitations': {
        0: {
            'methods': ['get']
        },
        2: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'invitation': {
                'endpoint': '/invitation/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'ComputerReports': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get']
            }
        }
    },
    'Departments': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'DirectoryBindings': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'DiskEncryptionConfigurations': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'DistributionPoints': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'DockItems': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'Ebooks': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        },
        2: {
            'id': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'FileUploads': {
        3: {
            '': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'GsxConnexion': {
        0: {
            'methods': ['get', 'put']
        }
    },
    'HealthCareListener': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put']
            }
        }
    },
    'HealthCareListenerRule': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post']
            }
        }
    },
    'DockItems': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'Ibeacons': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'InfrastructureManager': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put']
            }
        }
    },
    'JsonWebTokenConfigurations': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'LdapServers': {

    },
    'LicencedSoftware': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'LogFlush': {
    },
    'MacApplications': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        },
        2: {
            'id': {
                'endpoint': '/id/{0}/subset/{1}',
                'methods': ['get']
            }
        }
    },
    'ManagedPreferenceProfiles': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        },
        2: {
            'id': {
                'endpoint': '/id/{0}/subset/{1}',
                'methods': ['get']
            }
        }
    },
    'MobileDeviceApplications': {

    },
    'MobileDeviceCommands': {

    },
    'MobileDeviceConfigurationProfiles': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        },
        2: {
            'id': {
                'endpoint': '/id/{0}/subset/{1}',
                'methods': ['get']
            }
        }
    },
    'MobileDeviceConfigurationProfiles': {

    },
    'MobileDeviceEnrollementProfiles': {

    },
    'MobileDeviceExtensionAttributes': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'MobileDeviceExtensionGroups': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'MobileDeviceHistory': {
        2: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get']
            },
            'udid': {
                'endpoint': '/udid/{0}',
                'methods': ['get']
            },
            'serialnumber': {
                'endpoint': '/serialnumber/{0}',
                'methods': ['get']
            },
            'macaddress': {
                'endpoint': '/macaddress/{0}',
                'methods': ['get']
            }
        },
        3: {
            'id': {
                'endpoint': '/id/{0}/subset/',
                'methods': ['get']
            }
        }
    },
    'MobileDeviceInvitations': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/invitation/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'MobileDeviceExtensionGroups': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        }
    },
    'MobileDeviceProvisionningProfiles': {
        2: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get']
            },
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get']
            },
            'udid': {
                'endpoint': '/udid/{0}',
                'methods': ['get']
            },
            'serialnumber': {
                'endpoint': '/serialnumber/{0}',
                'methods': ['get']
            },
            'macaddress': {
                'endpoint': '/macaddress/{0}',
                'methods': ['get']
            }
        },
        3: {
            'id': {
                'endpoint': '/id/{0}/subset/',
                'methods': ['get']
            }
        }
    }
}
