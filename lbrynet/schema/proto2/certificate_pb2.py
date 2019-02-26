# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: certificate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='certificate.proto',
  package='pb',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x63\x65rtificate.proto\x12\x02pb\"\x94\x01\n\x0b\x43\x65rtificate\x12(\n\x07version\x18\x01 \x02(\x0e\x32\x17.pb.Certificate.Version\x12\x1c\n\x07keyType\x18\x02 \x02(\x0e\x32\x0b.pb.KeyType\x12\x11\n\tpublicKey\x18\x04 \x02(\x0c\"*\n\x07Version\x12\x13\n\x0fUNKNOWN_VERSION\x10\x00\x12\n\n\x06_0_0_1\x10\x01*Q\n\x07KeyType\x12\x1b\n\x17UNKNOWN_PUBLIC_KEY_TYPE\x10\x00\x12\x0c\n\x08NIST256p\x10\x01\x12\x0c\n\x08NIST384p\x10\x02\x12\r\n\tSECP256k1\x10\x03')
)

_KEYTYPE = _descriptor.EnumDescriptor(
  name='KeyType',
  full_name='pb.KeyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PUBLIC_KEY_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NIST256p', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NIST384p', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECP256k1', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=176,
  serialized_end=257,
)
_sym_db.RegisterEnumDescriptor(_KEYTYPE)

KeyType = enum_type_wrapper.EnumTypeWrapper(_KEYTYPE)
UNKNOWN_PUBLIC_KEY_TYPE = 0
NIST256p = 1
NIST384p = 2
SECP256k1 = 3


_CERTIFICATE_VERSION = _descriptor.EnumDescriptor(
  name='Version',
  full_name='pb.Certificate.Version',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_VERSION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_0_0_1', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=132,
  serialized_end=174,
)
_sym_db.RegisterEnumDescriptor(_CERTIFICATE_VERSION)


_CERTIFICATE = _descriptor.Descriptor(
  name='Certificate',
  full_name='pb.Certificate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='pb.Certificate.version', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyType', full_name='pb.Certificate.keyType', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publicKey', full_name='pb.Certificate.publicKey', index=2,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CERTIFICATE_VERSION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=174,
)

_CERTIFICATE.fields_by_name['version'].enum_type = _CERTIFICATE_VERSION
_CERTIFICATE.fields_by_name['keyType'].enum_type = _KEYTYPE
_CERTIFICATE_VERSION.containing_type = _CERTIFICATE
DESCRIPTOR.message_types_by_name['Certificate'] = _CERTIFICATE
DESCRIPTOR.enum_types_by_name['KeyType'] = _KEYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Certificate = _reflection.GeneratedProtocolMessageType('Certificate', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATE,
  __module__ = 'certificate_pb2'
  # @@protoc_insertion_point(class_scope:pb.Certificate)
  ))
_sym_db.RegisterMessage(Certificate)


# @@protoc_insertion_point(module_scope)
