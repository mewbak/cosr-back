# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: urlserver.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='urlserver.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0furlserver.proto\"\xd7\x01\n\x0bUrlMetadata\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tdomain_id\x18\x02 \x01(\x03\x12\x13\n\x0b\x61lexa_top1m\x18\x03 \x01(\x05\x12\x12\n\ndmoz_title\x18\x04 \x01(\t\x12\x18\n\x10\x64moz_description\x18\x05 \x01(\t\x12\x15\n\rut1_blacklist\x18\x06 \x03(\t\x12\x19\n\x11webdatacommons_hc\x18\x07 \x01(\x02\x12\x16\n\x0ewikidata_title\x18\x08 \x01(\t\x12\x1c\n\x14wikidata_description\x18\t \x01(\t\"\x13\n\x05UrlId\x12\n\n\x02id\x18\x01 \x01(\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_URLMETADATA = _descriptor.Descriptor(
  name='UrlMetadata',
  full_name='UrlMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UrlMetadata.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='UrlMetadata.domain_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alexa_top1m', full_name='UrlMetadata.alexa_top1m', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dmoz_title', full_name='UrlMetadata.dmoz_title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dmoz_description', full_name='UrlMetadata.dmoz_description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ut1_blacklist', full_name='UrlMetadata.ut1_blacklist', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='webdatacommons_hc', full_name='UrlMetadata.webdatacommons_hc', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wikidata_title', full_name='UrlMetadata.wikidata_title', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wikidata_description', full_name='UrlMetadata.wikidata_description', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=235,
)


_URLID = _descriptor.Descriptor(
  name='UrlId',
  full_name='UrlId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UrlId.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=256,
)

DESCRIPTOR.message_types_by_name['UrlMetadata'] = _URLMETADATA
DESCRIPTOR.message_types_by_name['UrlId'] = _URLID

UrlMetadata = _reflection.GeneratedProtocolMessageType('UrlMetadata', (_message.Message,), dict(
  DESCRIPTOR = _URLMETADATA,
  __module__ = 'urlserver_pb2'
  # @@protoc_insertion_point(class_scope:UrlMetadata)
  ))
_sym_db.RegisterMessage(UrlMetadata)

UrlId = _reflection.GeneratedProtocolMessageType('UrlId', (_message.Message,), dict(
  DESCRIPTOR = _URLID,
  __module__ = 'urlserver_pb2'
  # @@protoc_insertion_point(class_scope:UrlId)
  ))
_sym_db.RegisterMessage(UrlId)


# @@protoc_insertion_point(module_scope)
