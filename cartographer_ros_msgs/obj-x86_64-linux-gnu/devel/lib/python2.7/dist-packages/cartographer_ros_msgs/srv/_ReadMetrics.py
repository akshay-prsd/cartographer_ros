# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cartographer_ros_msgs/ReadMetricsRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ReadMetricsRequest(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "cartographer_ros_msgs/ReadMetricsRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """













"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ReadMetricsRequest, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cartographer_ros_msgs/ReadMetricsResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import cartographer_ros_msgs.msg
import genpy

class ReadMetricsResponse(genpy.Message):
  _md5sum = "a1fe8d7dcf3708e96e015774b1df470e"
  _type = "cartographer_ros_msgs/ReadMetricsResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """cartographer_ros_msgs/StatusResponse status
cartographer_ros_msgs/MetricFamily[] metric_families
time timestamp


================================================================================
MSG: cartographer_ros_msgs/StatusResponse
# Copyright 2018 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# A common message type to indicate the outcome of a service call.
uint8 code
string message

================================================================================
MSG: cartographer_ros_msgs/MetricFamily
# 2018 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

string name
string description
cartographer_ros_msgs/Metric[] metrics

================================================================================
MSG: cartographer_ros_msgs/Metric
# 2018 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

uint8 TYPE_COUNTER=0
uint8 TYPE_GAUGE=1
uint8 TYPE_HISTOGRAM=2

uint8 type
cartographer_ros_msgs/MetricLabel[] labels

# TYPE_COUNTER or TYPE_GAUGE
float64 value

# TYPE_HISTOGRAM
cartographer_ros_msgs/HistogramBucket[] counts_by_bucket

================================================================================
MSG: cartographer_ros_msgs/MetricLabel
# 2018 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

string key
string value

================================================================================
MSG: cartographer_ros_msgs/HistogramBucket
# 2018 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# A histogram bucket counts values x for which:
#   previous_boundary < x <= bucket_boundary
# holds.
float64 bucket_boundary
float64 count
"""
  __slots__ = ['status','metric_families','timestamp']
  _slot_types = ['cartographer_ros_msgs/StatusResponse','cartographer_ros_msgs/MetricFamily[]','time']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       status,metric_families,timestamp

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ReadMetricsResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.status is None:
        self.status = cartographer_ros_msgs.msg.StatusResponse()
      if self.metric_families is None:
        self.metric_families = []
      if self.timestamp is None:
        self.timestamp = genpy.Time()
    else:
      self.status = cartographer_ros_msgs.msg.StatusResponse()
      self.metric_families = []
      self.timestamp = genpy.Time()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_B().pack(self.status.code))
      _x = self.status.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.metric_families)
      buff.write(_struct_I.pack(length))
      for val1 in self.metric_families:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.description
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.metrics)
        buff.write(_struct_I.pack(length))
        for val2 in val1.metrics:
          buff.write(_get_struct_B().pack(val2.type))
          length = len(val2.labels)
          buff.write(_struct_I.pack(length))
          for val3 in val2.labels:
            _x = val3.key
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _x = val3.value
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
          buff.write(_get_struct_d().pack(val2.value))
          length = len(val2.counts_by_bucket)
          buff.write(_struct_I.pack(length))
          for val3 in val2.counts_by_bucket:
            _x = val3
            buff.write(_get_struct_2d().pack(_x.bucket_boundary, _x.count))
      _x = self
      buff.write(_get_struct_2I().pack(_x.timestamp.secs, _x.timestamp.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.status is None:
        self.status = cartographer_ros_msgs.msg.StatusResponse()
      if self.metric_families is None:
        self.metric_families = None
      if self.timestamp is None:
        self.timestamp = genpy.Time()
      end = 0
      start = end
      end += 1
      (self.status.code,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.message = str[start:end].decode('utf-8')
      else:
        self.status.message = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.metric_families = []
      for i in range(0, length):
        val1 = cartographer_ros_msgs.msg.MetricFamily()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.description = str[start:end].decode('utf-8')
        else:
          val1.description = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.metrics = []
        for i in range(0, length):
          val2 = cartographer_ros_msgs.msg.Metric()
          start = end
          end += 1
          (val2.type,) = _get_struct_B().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.labels = []
          for i in range(0, length):
            val3 = cartographer_ros_msgs.msg.MetricLabel()
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.key = str[start:end].decode('utf-8')
            else:
              val3.key = str[start:end]
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.value = str[start:end].decode('utf-8')
            else:
              val3.value = str[start:end]
            val2.labels.append(val3)
          start = end
          end += 8
          (val2.value,) = _get_struct_d().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.counts_by_bucket = []
          for i in range(0, length):
            val3 = cartographer_ros_msgs.msg.HistogramBucket()
            _x = val3
            start = end
            end += 16
            (_x.bucket_boundary, _x.count,) = _get_struct_2d().unpack(str[start:end])
            val2.counts_by_bucket.append(val3)
          val1.metrics.append(val2)
        self.metric_families.append(val1)
      _x = self
      start = end
      end += 8
      (_x.timestamp.secs, _x.timestamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      self.timestamp.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_B().pack(self.status.code))
      _x = self.status.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.metric_families)
      buff.write(_struct_I.pack(length))
      for val1 in self.metric_families:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.description
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.metrics)
        buff.write(_struct_I.pack(length))
        for val2 in val1.metrics:
          buff.write(_get_struct_B().pack(val2.type))
          length = len(val2.labels)
          buff.write(_struct_I.pack(length))
          for val3 in val2.labels:
            _x = val3.key
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _x = val3.value
            length = len(_x)
            if python3 or type(_x) == unicode:
              _x = _x.encode('utf-8')
              length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
          buff.write(_get_struct_d().pack(val2.value))
          length = len(val2.counts_by_bucket)
          buff.write(_struct_I.pack(length))
          for val3 in val2.counts_by_bucket:
            _x = val3
            buff.write(_get_struct_2d().pack(_x.bucket_boundary, _x.count))
      _x = self
      buff.write(_get_struct_2I().pack(_x.timestamp.secs, _x.timestamp.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.status is None:
        self.status = cartographer_ros_msgs.msg.StatusResponse()
      if self.metric_families is None:
        self.metric_families = None
      if self.timestamp is None:
        self.timestamp = genpy.Time()
      end = 0
      start = end
      end += 1
      (self.status.code,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.message = str[start:end].decode('utf-8')
      else:
        self.status.message = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.metric_families = []
      for i in range(0, length):
        val1 = cartographer_ros_msgs.msg.MetricFamily()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.description = str[start:end].decode('utf-8')
        else:
          val1.description = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.metrics = []
        for i in range(0, length):
          val2 = cartographer_ros_msgs.msg.Metric()
          start = end
          end += 1
          (val2.type,) = _get_struct_B().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.labels = []
          for i in range(0, length):
            val3 = cartographer_ros_msgs.msg.MetricLabel()
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.key = str[start:end].decode('utf-8')
            else:
              val3.key = str[start:end]
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
              val3.value = str[start:end].decode('utf-8')
            else:
              val3.value = str[start:end]
            val2.labels.append(val3)
          start = end
          end += 8
          (val2.value,) = _get_struct_d().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.counts_by_bucket = []
          for i in range(0, length):
            val3 = cartographer_ros_msgs.msg.HistogramBucket()
            _x = val3
            start = end
            end += 16
            (_x.bucket_boundary, _x.count,) = _get_struct_2d().unpack(str[start:end])
            val2.counts_by_bucket.append(val3)
          val1.metrics.append(val2)
        self.metric_families.append(val1)
      _x = self
      start = end
      end += 8
      (_x.timestamp.secs, _x.timestamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      self.timestamp.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2d = None
def _get_struct_2d():
    global _struct_2d
    if _struct_2d is None:
        _struct_2d = struct.Struct("<2d")
    return _struct_2d
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
class ReadMetrics(object):
  _type          = 'cartographer_ros_msgs/ReadMetrics'
  _md5sum = 'a1fe8d7dcf3708e96e015774b1df470e'
  _request_class  = ReadMetricsRequest
  _response_class = ReadMetricsResponse
