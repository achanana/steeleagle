# SPDX-FileCopyrightText: 2023 Carnegie Mellon University - Satyalab
#
# SPDX-License-Identifier: GPL-2.0-only

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cnc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cnc.proto',
  package='cnc',
  syntax='proto3',
  serialized_options=b'\n\025edu.cmu.cs.steeleagleB\006Protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tcnc.proto\x12\x03\x63nc\"O\n\x08Location\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x04 \x01(\x01\"=\n\x04PCMD\x12\x0b\n\x03gaz\x18\x01 \x01(\x05\x12\x0b\n\x03yaw\x18\x02 \x01(\x05\x12\r\n\x05pitch\x18\x03 \x01(\x05\x12\x0c\n\x04roll\x18\x04 \x01(\x05\"\x96\x01\n\x07\x43ommand\x12\x14\n\x0c\x66or_drone_id\x18\x01 \x01(\t\x12\x12\n\nscript_url\x18\x02 \x01(\t\x12\x0c\n\x04halt\x18\x03 \x01(\x08\x12\x17\n\x04pcmd\x18\x04 \x01(\x0b\x32\t.cnc.PCMD\x12\x0f\n\x07takeoff\x18\x05 \x01(\x08\x12\x0c\n\x04land\x18\x06 \x01(\x08\x12\x0e\n\x06manual\x18\x07 \x01(\x08\x12\x0b\n\x03rth\x18\x08 \x01(\x08\"`\n\x0b\x44roneStatus\x12\x0f\n\x07\x62\x61ttery\x18\x01 \x01(\x03\x12\x14\n\x0cgimbal_pitch\x18\x02 \x01(\x01\x12\x0f\n\x07\x62\x65\x61ring\x18\x03 \x01(\x01\x12\x0c\n\x04rssi\x18\x04 \x01(\x03\x12\x0b\n\x03mag\x18\x05 \x01(\x03\"\xbc\x01\n\x06\x45xtras\x12\x13\n\x0bregistering\x18\x01 \x01(\x08\x12\x10\n\x08\x64rone_id\x18\x02 \x01(\t\x12\x14\n\x0c\x63ommander_id\x18\x03 \x01(\t\x12\x19\n\x03\x63md\x18\x04 \x01(\x0b\x32\x0c.cnc.Command\x12\x1f\n\x08location\x18\x05 \x01(\x0b\x32\r.cnc.Location\x12 \n\x06status\x18\x06 \x01(\x0b\x32\x10.cnc.DroneStatus\x12\x17\n\x0f\x64\x65tection_model\x18\x07 \x01(\tB\x1f\n\x15\x65\x64u.cmu.cs.steeleagleB\x06Protosb\x06proto3'
)




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='cnc.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cnc.Location.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='cnc.Location.latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='cnc.Location.longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='cnc.Location.altitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=97,
)


_PCMD = _descriptor.Descriptor(
  name='PCMD',
  full_name='cnc.PCMD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gaz', full_name='cnc.PCMD.gaz', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='cnc.PCMD.yaw', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='cnc.PCMD.pitch', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roll', full_name='cnc.PCMD.roll', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=160,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='cnc.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='for_drone_id', full_name='cnc.Command.for_drone_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='script_url', full_name='cnc.Command.script_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='halt', full_name='cnc.Command.halt', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pcmd', full_name='cnc.Command.pcmd', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='takeoff', full_name='cnc.Command.takeoff', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='land', full_name='cnc.Command.land', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='manual', full_name='cnc.Command.manual', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rth', full_name='cnc.Command.rth', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=313,
)


_DRONESTATUS = _descriptor.Descriptor(
  name='DroneStatus',
  full_name='cnc.DroneStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='battery', full_name='cnc.DroneStatus.battery', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gimbal_pitch', full_name='cnc.DroneStatus.gimbal_pitch', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bearing', full_name='cnc.DroneStatus.bearing', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='cnc.DroneStatus.rssi', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mag', full_name='cnc.DroneStatus.mag', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=411,
)


_EXTRAS = _descriptor.Descriptor(
  name='Extras',
  full_name='cnc.Extras',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='registering', full_name='cnc.Extras.registering', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drone_id', full_name='cnc.Extras.drone_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commander_id', full_name='cnc.Extras.commander_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cmd', full_name='cnc.Extras.cmd', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='cnc.Extras.location', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='cnc.Extras.status', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detection_model', full_name='cnc.Extras.detection_model', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=414,
  serialized_end=602,
)

_COMMAND.fields_by_name['pcmd'].message_type = _PCMD
_EXTRAS.fields_by_name['cmd'].message_type = _COMMAND
_EXTRAS.fields_by_name['location'].message_type = _LOCATION
_EXTRAS.fields_by_name['status'].message_type = _DRONESTATUS
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['PCMD'] = _PCMD
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['DroneStatus'] = _DRONESTATUS
DESCRIPTOR.message_types_by_name['Extras'] = _EXTRAS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'cnc_pb2'
  # @@protoc_insertion_point(class_scope:cnc.Location)
  })
_sym_db.RegisterMessage(Location)

PCMD = _reflection.GeneratedProtocolMessageType('PCMD', (_message.Message,), {
  'DESCRIPTOR' : _PCMD,
  '__module__' : 'cnc_pb2'
  # @@protoc_insertion_point(class_scope:cnc.PCMD)
  })
_sym_db.RegisterMessage(PCMD)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'cnc_pb2'
  # @@protoc_insertion_point(class_scope:cnc.Command)
  })
_sym_db.RegisterMessage(Command)

DroneStatus = _reflection.GeneratedProtocolMessageType('DroneStatus', (_message.Message,), {
  'DESCRIPTOR' : _DRONESTATUS,
  '__module__' : 'cnc_pb2'
  # @@protoc_insertion_point(class_scope:cnc.DroneStatus)
  })
_sym_db.RegisterMessage(DroneStatus)

Extras = _reflection.GeneratedProtocolMessageType('Extras', (_message.Message,), {
  'DESCRIPTOR' : _EXTRAS,
  '__module__' : 'cnc_pb2'
  # @@protoc_insertion_point(class_scope:cnc.Extras)
  })
_sym_db.RegisterMessage(Extras)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
