# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fee.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fee.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tfee.proto\x12\x02pb\"~\n\x03\x46\x65\x65\x12\"\n\x08\x63urrency\x18\x01 \x01(\x0e\x32\x10.pb.Fee.Currency\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x02\"2\n\x08\x43urrency\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03LBC\x10\x01\x12\x07\n\x03\x42TC\x10\x02\x12\x07\n\x03USD\x10\x03\x62\x06proto3')
)



_FEE_CURRENCY = _descriptor.EnumDescriptor(
  name='Currency',
  full_name='pb.Fee.Currency',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LBC', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BTC', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USD', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=93,
  serialized_end=143,
)
_sym_db.RegisterEnumDescriptor(_FEE_CURRENCY)


_FEE = _descriptor.Descriptor(
  name='Fee',
  full_name='pb.Fee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency', full_name='pb.Fee.currency', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='pb.Fee.address', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='pb.Fee.amount', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEE_CURRENCY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=143,
)

_FEE.fields_by_name['currency'].enum_type = _FEE_CURRENCY
_FEE_CURRENCY.containing_type = _FEE
DESCRIPTOR.message_types_by_name['Fee'] = _FEE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Fee = _reflection.GeneratedProtocolMessageType('Fee', (_message.Message,), dict(
  DESCRIPTOR = _FEE,
  __module__ = 'fee_pb2'
  # @@protoc_insertion_point(class_scope:pb.Fee)
  ))
_sym_db.RegisterMessage(Fee)


# @@protoc_insertion_point(module_scope)
