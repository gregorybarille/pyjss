default_scope_template = """<scope>
  <all_computers>
   false
  </all_computers>
  <computers/>
  <computer_groups/>
  <buildings/>
  <departments/>
  <limit_to_users>
   <user_groups/>
  </limit_to_users>
  <limitations>
   <users/>
   <user_groups/>
   <network_segments/>
   <ibeacons/>
  </limitations>
  <exclusions>
   <computers/>
   <computer_groups/>
   <buildings/>
   <departments/>
   <users/>
   <user_groups/>
   <network_segments/>
   <ibeacons/>
  </exclusions>
 </scope>"""

# default_policy_template = """<policy>
#  <general>
#   <id>
#    0
#   </id>
#   <name>
#    no_name
#   </name>
#   <enabled>
#    false
#   </enabled>
#   <trigger>
#    EVENT
#   </trigger>
#   <trigger_checkin>
#    false
#   </trigger_checkin>
#   <trigger_enrollment_complete>
#    false
#   </trigger_enrollment_complete>
#   <trigger_login>
#    false
#   </trigger_login>
#   <trigger_logout>
#    false
#   </trigger_logout>
#   <trigger_network_state_changed>
#    false
#   </trigger_network_state_changed>
#   <trigger_startup>
#    false
#   </trigger_startup>
#   <trigger_other/>
#   <frequency>
#    Once per computer
#   </frequency>
#   <location_user_only>
#    false
#   </location_user_only>
#   <target_drive>
#    /
#   </target_drive>
#   <offline>
#    false
#   </offline>
#   <category>
#    <id>
#     -1
#    </id>
#    <name>
#     No category assigned
#    </name>
#   </category>
#   <date_time_limitations>
#    <activation_date/>
#    <activation_date_epoch>
#     0
#    </activation_date_epoch>
#    <activation_date_utc/>
#    <expiration_date/>
#    <expiration_date_epoch>
#     0
#    </expiration_date_epoch>
#    <expiration_date_utc/>
#    <no_execute_on/>
#    <no_execute_start/>
#    <no_execute_end/>
#   </date_time_limitations>
#   <network_limitations>
#    <minimum_network_connection>
#     No Minimum
#    </minimum_network_connection>
#    <any_ip_address>
#     true
#    </any_ip_address>
#    <network_segments/>
#   </network_limitations>
#   <override_default_settings>
#    <target_drive>
#     default
#    </target_drive>
#    <distribution_point/>
#    <force_afp_smb>
#     false
#    </force_afp_smb>
#    <sus>
#     default
#    </sus>
#    <netboot_server>
#     current
#    </netboot_server>
#   </override_default_settings>
#   <network_requirements>
#    Any
#   </network_requirements>
#   <site>
#    <id>
#     -1
#    </id>
#    <name>
#     None
#    </name>
#   </site>
#  </general>
#  <scope>
#   <all_computers>
#    false
#   </all_computers>
#   <computers/>
#   <computer_groups/>
#   <buildings/>
#   <departments/>
#   <limit_to_users>
#    <user_groups/>
#   </limit_to_users>
#   <limitations>
#    <users/>
#    <user_groups/>
#    <network_segments/>
#    <ibeacons/>
#   </limitations>
#   <exclusions>
#    <computers/>
#    <computer_groups/>
#    <buildings/>
#    <departments/>
#    <users/>
#    <user_groups/>
#    <network_segments/>
#    <ibeacons/>
#   </exclusions>
#  </scope>
#  <self_service>
#   <use_for_self_service>
#    false
#   </use_for_self_service>
#   <self_service_display_name/>
#   <install_button_text>
#    Install
#   </install_button_text>
#   <reinstall_button_text>
#    Reinstall
#   </reinstall_button_text>
#   <self_service_description/>
#   <force_users_to_view_description>
#    false
#   </force_users_to_view_description>
#   <self_service_icon/>
#   <feature_on_main_page>
#    false
#   </feature_on_main_page>
#   <self_service_categories>
#    <category>
#     <id>
#      43
#     </id>
#     <name>
#      Testing
#     </name>
#     <display_in>
#      true
#     </display_in>
#     <feature_in>
#      false
#     </feature_in>
#    </category>
#   </self_service_categories>
#   <notification>
#    false
#   </notification>
#   <notification>
#    Self Service
#   </notification>
#   <notification_subject>
#    Test_policy
#   </notification_subject>
#   <notification_message/>
#  </self_service>
#  <package_configuration>
#   <packages>
#    <size>
#     0
#    </size>
#   </packages>
#  </package_configuration>
#  <scripts>
#   <size>
#    0
#   </size>
#  </scripts>
#  <printers>
#   <size>
#    0
#   </size>
#   <leave_existing_default/>
#  </printers>
#  <dock_items>
#   <size>
#    0
#   </size>
#  </dock_items>
#  <account_maintenance>
#   <accounts>
#    <size>
#     0
#    </size>
#   </accounts>
#   <directory_bindings>
#    <size>
#     0
#    </size>
#   </directory_bindings>
#   <management_account>
#    <action>
#     doNotChange
#    </action>
#   </management_account>
#   <open_firmware_efi_password>
#    <of_mode>
#     none
#    </of_mode>
#    <of_password_sha256 since="9.23">
#     e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
#    </of_password_sha256>
#   </open_firmware_efi_password>
#  </account_maintenance>
#  <reboot>
#   <message>
#    This computer will restart in 5 minutes. Please save anything you are working on and log out by choosing Log Out from the bottom of the Apple menu.
#   </message>
#   <startup_disk>
#    Current Startup Disk
#   </startup_disk>
#   <specify_startup/>
#   <no_user_logged_in>
#    Restart if a package or update requires it
#   </no_user_logged_in>
#   <user_logged_in>
#    Restart if a package or update requires it
#   </user_logged_in>
#   <minutes_until_reboot>
#    5
#   </minutes_until_reboot>
#   <file_vault_2_reboot>
#    false
#   </file_vault_2_reboot>
#  </reboot>
#  <maintenance>
#   <recon>
#    false
#   </recon>
#   <reset_name>
#    false
#   </reset_name>
#   <install_all_cached_packages>
#    false
#   </install_all_cached_packages>
#   <heal>
#    false
#   </heal>
#   <prebindings>
#    false
#   </prebindings>
#   <permissions>
#    false
#   </permissions>
#   <byhost>
#    false
#   </byhost>
#   <system_cache>
#    false
#   </system_cache>
#   <user_cache>
#    false
#   </user_cache>
#   <verify>
#    false
#   </verify>
#  </maintenance>
#  <files_processes>
#   <search_by_path/>
#   <delete_file>
#    false
#   </delete_file>
#   <locate_file/>
#   <update_locate_database>
#    false
#   </update_locate_database>
#   <spotlight_search/>
#   <search_for_process/>
#   <kill_process>
#    false
#   </kill_process>
#   <run_command/>
#  </files_processes>
#  <user_interaction>
#   <message_start/>
#   <allow_users_to_defer>
#    false
#   </allow_users_to_defer>
#   <allow_deferral_until_utc/>
#   <message_finish/>
#  </user_interaction>
#  <disk_encryption>
#   <action>
#    none
#   </action>
#  </disk_encryption>
# </policy> """

default_policy_template = """<policy><general><id>0</id><name>no_name</name><enabled>false</enabled><trigger>EVENT</trigger><trigger_checkin>false</trigger_checkin><trigger_enrollment_complete>false</trigger_enrollment_complete><trigger_login>false</trigger_login><trigger_logout>false</trigger_logout><trigger_network_state_changed>false</trigger_network_state_changed><trigger_startup>false</trigger_startup><trigger_other/><frequency>Oncepercomputer</frequency><location_user_only>false</location_user_only><target_drive>/</target_drive><offline>false</offline><category><id>-1</id><name>Nocategoryassigned</name></category><date_time_limitations><activation_date/><activation_date_epoch>0</activation_date_epoch><activation_date_utc/><expiration_date/><expiration_date_epoch>0</expiration_date_epoch><expiration_date_utc/><no_execute_on/><no_execute_start/><no_execute_end/></date_time_limitations><network_limitations><minimum_network_connection>NoMinimum</minimum_network_connection><any_ip_address>true</any_ip_address><network_segments/></network_limitations><override_default_settings><target_drive>default</target_drive><distribution_point/><force_afp_smb>false</force_afp_smb><sus>default</sus><netboot_server>current</netboot_server></override_default_settings><network_requirements>Any</network_requirements><site><id>-1</id><name>None</name></site></general><scope><all_computers>false</all_computers><computers/><computer_groups/><buildings/><departments/><limit_to_users><user_groups/></limit_to_users><limitations><users/><user_groups/><network_segments/><ibeacons/></limitations><exclusions><computers/><computer_groups/><buildings/><departments/><users/><user_groups/><network_segments/><ibeacons/></exclusions></scope><self_service><use_for_self_service>false</use_for_self_service><self_service_display_name/><install_button_text>Install</install_button_text><reinstall_button_text>Reinstall</reinstall_button_text><self_service_description/><force_users_to_view_description>false</force_users_to_view_description><self_service_icon/><feature_on_main_page>false</feature_on_main_page><self_service_categories><category><id>43</id><name>Testing</name><display_in>true</display_in><feature_in>false</feature_in></category></self_service_categories><notification>false</notification><notification>SelfService</notification><notification_subject>Test_policy</notification_subject><notification_message/></self_service><package_configuration><packages><size>0</size></packages></package_configuration><scripts><size>0</size></scripts><printers><size>0</size><leave_existing_default/></printers><dock_items><size>0</size></dock_items><account_maintenance><accounts><size>0</size></accounts><directory_bindings><size>0</size></directory_bindings><management_account><action>doNotChange</action></management_account><open_firmware_efi_password><of_mode>none</of_mode><of_password_sha256since="9.23">e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</of_password_sha256></open_firmware_efi_password></account_maintenance><reboot><message>Thiscomputerwillrestartin5minutes.PleasesaveanythingyouareworkingonandlogoutbychoosingLogOutfromthebottomoftheApplemenu.</message><startup_disk>CurrentStartupDisk</startup_disk><specify_startup/><no_user_logged_in>Restartifapackageorupdaterequiresit</no_user_logged_in><user_logged_in>Restartifapackageorupdaterequiresit</user_logged_in><minutes_until_reboot>5</minutes_until_reboot><file_vault_2_reboot>false</file_vault_2_reboot></reboot><maintenance><recon>false</recon><reset_name>false</reset_name><install_all_cached_packages>false</install_all_cached_packages><heal>false</heal><prebindings>false</prebindings><permissions>false</permissions><byhost>false</byhost><system_cache>false</system_cache><user_cache>false</user_cache><verify>false</verify></maintenance><files_processes><search_by_path/><delete_file>false</delete_file><locate_file/><update_locate_database>false</update_locate_database><spotlight_search/><search_for_process/><kill_process>false</kill_process><run_command/></files_processes><user_interaction><message_start/><allow_users_to_defer>false</allow_users_to_defer><allow_deferral_until_utc/><message_finish/></user_interaction><disk_encryption><action>none</action></disk_encryption></policy>"""
