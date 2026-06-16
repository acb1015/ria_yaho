# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ouster_sensor_msgs:msg/Telemetry.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Telemetry(type):
    """Metaclass of message 'Telemetry'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'THERMAL_SHUTDOWN_NORMAL': 0,
        'THERMAL_SHUTDOWN_IMMINENT': 1,
        'SHOT_LIMITING_NORMAL': 0,
        'SHOT_LIMITING_IMMINENT': 1,
        'SHOT_LIMITING_REDUCTION_0_10': 2,
        'SHOT_LIMITING_REDUCTION_10_20': 3,
        'SHOT_LIMITING_REDUCTION_20_30': 4,
        'SHOT_LIMITING_REDUCTION_30_40': 5,
        'SHOT_LIMITING_REDUCTION_40_50': 6,
        'SHOT_LIMITING_REDUCTION_50_60': 7,
        'SHOT_LIMITING_REDUCTION_60_70': 8,
        'SHOT_LIMITING_REDUCTION_70_75': 9,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ouster_sensor_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ouster_sensor_msgs.msg.Telemetry')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__telemetry
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__telemetry
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__telemetry
            cls._TYPE_SUPPORT = module.type_support_msg__msg__telemetry
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__telemetry

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'THERMAL_SHUTDOWN_NORMAL': cls.__constants['THERMAL_SHUTDOWN_NORMAL'],
            'THERMAL_SHUTDOWN_IMMINENT': cls.__constants['THERMAL_SHUTDOWN_IMMINENT'],
            'SHOT_LIMITING_NORMAL': cls.__constants['SHOT_LIMITING_NORMAL'],
            'SHOT_LIMITING_IMMINENT': cls.__constants['SHOT_LIMITING_IMMINENT'],
            'SHOT_LIMITING_REDUCTION_0_10': cls.__constants['SHOT_LIMITING_REDUCTION_0_10'],
            'SHOT_LIMITING_REDUCTION_10_20': cls.__constants['SHOT_LIMITING_REDUCTION_10_20'],
            'SHOT_LIMITING_REDUCTION_20_30': cls.__constants['SHOT_LIMITING_REDUCTION_20_30'],
            'SHOT_LIMITING_REDUCTION_30_40': cls.__constants['SHOT_LIMITING_REDUCTION_30_40'],
            'SHOT_LIMITING_REDUCTION_40_50': cls.__constants['SHOT_LIMITING_REDUCTION_40_50'],
            'SHOT_LIMITING_REDUCTION_50_60': cls.__constants['SHOT_LIMITING_REDUCTION_50_60'],
            'SHOT_LIMITING_REDUCTION_60_70': cls.__constants['SHOT_LIMITING_REDUCTION_60_70'],
            'SHOT_LIMITING_REDUCTION_70_75': cls.__constants['SHOT_LIMITING_REDUCTION_70_75'],
        }

    @property
    def THERMAL_SHUTDOWN_NORMAL(self):
        """Message constant 'THERMAL_SHUTDOWN_NORMAL'."""
        return Metaclass_Telemetry.__constants['THERMAL_SHUTDOWN_NORMAL']

    @property
    def THERMAL_SHUTDOWN_IMMINENT(self):
        """Message constant 'THERMAL_SHUTDOWN_IMMINENT'."""
        return Metaclass_Telemetry.__constants['THERMAL_SHUTDOWN_IMMINENT']

    @property
    def SHOT_LIMITING_NORMAL(self):
        """Message constant 'SHOT_LIMITING_NORMAL'."""
        return Metaclass_Telemetry.__constants['SHOT_LIMITING_NORMAL']

    @property
    def SHOT_LIMITING_IMMINENT(self):
        """Message constant 'SHOT_LIMITING_IMMINENT'."""
        return Metaclass_Telemetry.__constants['SHOT_LIMITING_IMMINENT']

    @property
    def SHOT_LIMITING_REDUCTION_0_10(self):
        """Message constant 'SHOT_LIMITING_REDUCTION_0_10'."""
        return Metaclass_Telemetry.__constants['SHOT_LIMITING_REDUCTION_0_10']

    @property
    def SHOT_LIMITING_REDUCTION_10_20(self):
        """Message constant 'SHOT_LIMITING_REDUCTION_10_20'."""
        return Metaclass_Telemetry.__constants['SHOT_LIMITING_REDUCTION_10_20']

    @property
    def SHOT_LIMITING_REDUCTION_20_30(self):
        """Message constant 'SHOT_LIMITING_REDUCTION_20_30'."""
        return Metaclass_Telemetry.__constants['SHOT_LIMITING_REDUCTION_20_30']

    @property
    def SHOT_LIMITING_REDUCTION_30_40(self):
        """Message constant 'SHOT_LIMITING_REDUCTION_30_40'."""
        return Metaclass_Telemetry.__constants['SHOT_LIMITING_REDUCTION_30_40']

    @property
    def SHOT_LIMITING_REDUCTION_40_50(self):
        """Message constant 'SHOT_LIMITING_REDUCTION_40_50'."""
        return Metaclass_Telemetry.__constants['SHOT_LIMITING_REDUCTION_40_50']

    @property
    def SHOT_LIMITING_REDUCTION_50_60(self):
        """Message constant 'SHOT_LIMITING_REDUCTION_50_60'."""
        return Metaclass_Telemetry.__constants['SHOT_LIMITING_REDUCTION_50_60']

    @property
    def SHOT_LIMITING_REDUCTION_60_70(self):
        """Message constant 'SHOT_LIMITING_REDUCTION_60_70'."""
        return Metaclass_Telemetry.__constants['SHOT_LIMITING_REDUCTION_60_70']

    @property
    def SHOT_LIMITING_REDUCTION_70_75(self):
        """Message constant 'SHOT_LIMITING_REDUCTION_70_75'."""
        return Metaclass_Telemetry.__constants['SHOT_LIMITING_REDUCTION_70_75']


class Telemetry(metaclass=Metaclass_Telemetry):
    """
    Message class 'Telemetry'.

    Constants:
      THERMAL_SHUTDOWN_NORMAL
      THERMAL_SHUTDOWN_IMMINENT
      SHOT_LIMITING_NORMAL
      SHOT_LIMITING_IMMINENT
      SHOT_LIMITING_REDUCTION_0_10
      SHOT_LIMITING_REDUCTION_10_20
      SHOT_LIMITING_REDUCTION_20_30
      SHOT_LIMITING_REDUCTION_30_40
      SHOT_LIMITING_REDUCTION_40_50
      SHOT_LIMITING_REDUCTION_50_60
      SHOT_LIMITING_REDUCTION_60_70
      SHOT_LIMITING_REDUCTION_70_75
    """

    __slots__ = [
        '_header',
        '_countdown_thermal_shutdown',
        '_countdown_shot_limiting',
        '_thermal_shutdown',
        '_shot_limiting',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'countdown_thermal_shutdown': 'uint16',
        'countdown_shot_limiting': 'uint16',
        'thermal_shutdown': 'uint8',
        'shot_limiting': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.countdown_thermal_shutdown = kwargs.get('countdown_thermal_shutdown', int())
        self.countdown_shot_limiting = kwargs.get('countdown_shot_limiting', int())
        self.thermal_shutdown = kwargs.get('thermal_shutdown', int())
        self.shot_limiting = kwargs.get('shot_limiting', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.countdown_thermal_shutdown != other.countdown_thermal_shutdown:
            return False
        if self.countdown_shot_limiting != other.countdown_shot_limiting:
            return False
        if self.thermal_shutdown != other.thermal_shutdown:
            return False
        if self.shot_limiting != other.shot_limiting:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def countdown_thermal_shutdown(self):
        """Message field 'countdown_thermal_shutdown'."""
        return self._countdown_thermal_shutdown

    @countdown_thermal_shutdown.setter
    def countdown_thermal_shutdown(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'countdown_thermal_shutdown' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'countdown_thermal_shutdown' field must be an unsigned integer in [0, 65535]"
        self._countdown_thermal_shutdown = value

    @builtins.property
    def countdown_shot_limiting(self):
        """Message field 'countdown_shot_limiting'."""
        return self._countdown_shot_limiting

    @countdown_shot_limiting.setter
    def countdown_shot_limiting(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'countdown_shot_limiting' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'countdown_shot_limiting' field must be an unsigned integer in [0, 65535]"
        self._countdown_shot_limiting = value

    @builtins.property
    def thermal_shutdown(self):
        """Message field 'thermal_shutdown'."""
        return self._thermal_shutdown

    @thermal_shutdown.setter
    def thermal_shutdown(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'thermal_shutdown' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'thermal_shutdown' field must be an unsigned integer in [0, 255]"
        self._thermal_shutdown = value

    @builtins.property
    def shot_limiting(self):
        """Message field 'shot_limiting'."""
        return self._shot_limiting

    @shot_limiting.setter
    def shot_limiting(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'shot_limiting' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'shot_limiting' field must be an unsigned integer in [0, 255]"
        self._shot_limiting = value
