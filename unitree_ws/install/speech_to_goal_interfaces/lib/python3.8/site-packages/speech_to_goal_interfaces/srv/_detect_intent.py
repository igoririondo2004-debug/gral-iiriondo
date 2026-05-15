# generated from rosidl_generator_py/resource/_idl.py.em
# with input from speech_to_goal_interfaces:srv/DetectIntent.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_DetectIntent_Request(type):
    """Metaclass of message 'DetectIntent_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('speech_to_goal_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'speech_to_goal_interfaces.srv.DetectIntent_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__detect_intent__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__detect_intent__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__detect_intent__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__detect_intent__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__detect_intent__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DetectIntent_Request(metaclass=Metaclass_DetectIntent_Request):
    """Message class 'DetectIntent_Request'."""

    __slots__ = [
        '_text',
    ]

    _fields_and_field_types = {
        'text': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.text = kwargs.get('text', str())

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
        if self.text != other.text:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def text(self):
        """Message field 'text'."""
        return self._text

    @text.setter
    def text(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'text' field must be of type 'str'"
        self._text = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DetectIntent_Response(type):
    """Metaclass of message 'DetectIntent_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('speech_to_goal_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'speech_to_goal_interfaces.srv.DetectIntent_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__detect_intent__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__detect_intent__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__detect_intent__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__detect_intent__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__detect_intent__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DetectIntent_Response(metaclass=Metaclass_DetectIntent_Response):
    """Message class 'DetectIntent_Response'."""

    __slots__ = [
        '_intent',
    ]

    _fields_and_field_types = {
        'intent': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.intent = kwargs.get('intent', str())

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
        if self.intent != other.intent:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def intent(self):
        """Message field 'intent'."""
        return self._intent

    @intent.setter
    def intent(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'intent' field must be of type 'str'"
        self._intent = value


class Metaclass_DetectIntent(type):
    """Metaclass of service 'DetectIntent'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('speech_to_goal_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'speech_to_goal_interfaces.srv.DetectIntent')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__detect_intent

            from speech_to_goal_interfaces.srv import _detect_intent
            if _detect_intent.Metaclass_DetectIntent_Request._TYPE_SUPPORT is None:
                _detect_intent.Metaclass_DetectIntent_Request.__import_type_support__()
            if _detect_intent.Metaclass_DetectIntent_Response._TYPE_SUPPORT is None:
                _detect_intent.Metaclass_DetectIntent_Response.__import_type_support__()


class DetectIntent(metaclass=Metaclass_DetectIntent):
    from speech_to_goal_interfaces.srv._detect_intent import DetectIntent_Request as Request
    from speech_to_goal_interfaces.srv._detect_intent import DetectIntent_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
