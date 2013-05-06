#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import StatestoreTypes.ttypes
import Status.ttypes
import Types.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class StateStoreSubscriberServiceVersion:
  V1 = 0

  _VALUES_TO_NAMES = {
    0: "V1",
  }

  _NAMES_TO_VALUES = {
    "V1": 0,
  }


class TUpdateStateRequest:
  """
  Attributes:
   - protocolVersion
   - service_memberships
   - updated_objects
   - deleted_object_keys
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'protocolVersion', None,     0, ), # 1
    (2, TType.LIST, 'service_memberships', (TType.STRUCT,(StatestoreTypes.ttypes.TServiceMembership, StatestoreTypes.ttypes.TServiceMembership.thrift_spec)), None, ), # 2
    (3, TType.LIST, 'updated_objects', (TType.STRUCT,(StatestoreTypes.ttypes.TVersionedObject, StatestoreTypes.ttypes.TVersionedObject.thrift_spec)), None, ), # 3
    (4, TType.LIST, 'deleted_object_keys', (TType.STRING,None), None, ), # 4
  )

  def __init__(self, protocolVersion=thrift_spec[1][4], service_memberships=None, updated_objects=None, deleted_object_keys=None,):
    self.protocolVersion = protocolVersion
    self.service_memberships = service_memberships
    self.updated_objects = updated_objects
    self.deleted_object_keys = deleted_object_keys

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.protocolVersion = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.service_memberships = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = StatestoreTypes.ttypes.TServiceMembership()
            _elem5.read(iprot)
            self.service_memberships.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.updated_objects = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = StatestoreTypes.ttypes.TVersionedObject()
            _elem11.read(iprot)
            self.updated_objects.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.deleted_object_keys = []
          (_etype15, _size12) = iprot.readListBegin()
          for _i16 in xrange(_size12):
            _elem17 = iprot.readString();
            self.deleted_object_keys.append(_elem17)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TUpdateStateRequest')
    if self.protocolVersion is not None:
      oprot.writeFieldBegin('protocolVersion', TType.I32, 1)
      oprot.writeI32(self.protocolVersion)
      oprot.writeFieldEnd()
    if self.service_memberships is not None:
      oprot.writeFieldBegin('service_memberships', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.service_memberships))
      for iter18 in self.service_memberships:
        iter18.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.updated_objects is not None:
      oprot.writeFieldBegin('updated_objects', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.updated_objects))
      for iter19 in self.updated_objects:
        iter19.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.deleted_object_keys is not None:
      oprot.writeFieldBegin('deleted_object_keys', TType.LIST, 4)
      oprot.writeListBegin(TType.STRING, len(self.deleted_object_keys))
      for iter20 in self.deleted_object_keys:
        oprot.writeString(iter20)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.protocolVersion is None:
      raise TProtocol.TProtocolException(message='Required field protocolVersion is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TUpdateStateResponse:
  """
  Attributes:
   - status
   - updated_objects
   - deleted_object_keys
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'status', (Status.ttypes.TStatus, Status.ttypes.TStatus.thrift_spec), None, ), # 1
    (2, TType.LIST, 'updated_objects', (TType.STRUCT,(StatestoreTypes.ttypes.TVersionedObject, StatestoreTypes.ttypes.TVersionedObject.thrift_spec)), None, ), # 2
    (3, TType.LIST, 'deleted_object_keys', (TType.STRING,None), None, ), # 3
  )

  def __init__(self, status=None, updated_objects=None, deleted_object_keys=None,):
    self.status = status
    self.updated_objects = updated_objects
    self.deleted_object_keys = deleted_object_keys

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.status = Status.ttypes.TStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.updated_objects = []
          (_etype24, _size21) = iprot.readListBegin()
          for _i25 in xrange(_size21):
            _elem26 = StatestoreTypes.ttypes.TVersionedObject()
            _elem26.read(iprot)
            self.updated_objects.append(_elem26)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.deleted_object_keys = []
          (_etype30, _size27) = iprot.readListBegin()
          for _i31 in xrange(_size27):
            _elem32 = iprot.readString();
            self.deleted_object_keys.append(_elem32)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TUpdateStateResponse')
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRUCT, 1)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    if self.updated_objects is not None:
      oprot.writeFieldBegin('updated_objects', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.updated_objects))
      for iter33 in self.updated_objects:
        iter33.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.deleted_object_keys is not None:
      oprot.writeFieldBegin('deleted_object_keys', TType.LIST, 3)
      oprot.writeListBegin(TType.STRING, len(self.deleted_object_keys))
      for iter34 in self.deleted_object_keys:
        oprot.writeString(iter34)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
