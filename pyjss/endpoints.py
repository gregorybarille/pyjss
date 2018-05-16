endpoints = {
    'Accounts': {
		0: {
			'methods': ['get']
		},
		1: {
			'id': {
				'endpoint': '/userid/{0}',
				'methods': ['get', 'put', 'post', 'delete']
			},
			'name': {
				'endpoint': '/username/{0}',
				'methods': ['get', 'put', 'post', 'delete']
			}
		},
		2: {
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
   	'ActivationCode':{
        0: {
            'methods': ['get', 'put']
        }
	},
   	'AdvancedComputerSearches':{
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
   	'AdvancedMobileDeviceSearches': {
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
   	'AdvancedUserSearches': {
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
   	'AllowedFileExtension': {
        0: {
            'methods': ['get']
        },
        1: {
            'id': {
                'endpoint': '/id/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            },
            'name': {
                'endpoint': '/extension/{0}',
                'methods': ['get']
            }
        }
    },
   	'Buildings': {
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
   	'ByoProfiles': {
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
   	'Classes': {
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
   	'ComputerApplications': {
        1: {
            'name': {
                'endpoint': '/name/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
        },
      	2: {
            'siteid': {
				'endpoint': '/groupid/{0}',
				'methods': ['get', 'put', 'post', 'delete']
            },
            'sitename': {
                'endpoint': '/groupname/{0}',
                'methods': ['get', 'put', 'post', 'delete']
            }
    	},
		3: {
			'name':{
				'endpoint': '/groupid/{0}',
				'methods': ['get', 'put', 'post', 'delete']
			}
		}
    },
}
