#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "OusterSDK::ouster_client" for configuration "Release"
set_property(TARGET OusterSDK::ouster_client APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OusterSDK::ouster_client PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libouster_client.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS OusterSDK::ouster_client )
list(APPEND _IMPORT_CHECK_FILES_FOR_OusterSDK::ouster_client "${_IMPORT_PREFIX}/lib/libouster_client.a" )

# Import target "OusterSDK::nmea" for configuration "Release"
set_property(TARGET OusterSDK::nmea APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OusterSDK::nmea PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libnmea.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS OusterSDK::nmea )
list(APPEND _IMPORT_CHECK_FILES_FOR_OusterSDK::nmea "${_IMPORT_PREFIX}/lib/libnmea.a" )

# Import target "OusterSDK::ouster_sensor" for configuration "Release"
set_property(TARGET OusterSDK::ouster_sensor APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OusterSDK::ouster_sensor PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libouster_sensor.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS OusterSDK::ouster_sensor )
list(APPEND _IMPORT_CHECK_FILES_FOR_OusterSDK::ouster_sensor "${_IMPORT_PREFIX}/lib/libouster_sensor.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
