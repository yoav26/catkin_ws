// Auto-generated. Do not edit!

// (in-package beginner_tutorials.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class coordinates {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.datax = null;
      this.datay = null;
      this.dataz = null;
    }
    else {
      if (initObj.hasOwnProperty('datax')) {
        this.datax = initObj.datax
      }
      else {
        this.datax = [];
      }
      if (initObj.hasOwnProperty('datay')) {
        this.datay = initObj.datay
      }
      else {
        this.datay = [];
      }
      if (initObj.hasOwnProperty('dataz')) {
        this.dataz = initObj.dataz
      }
      else {
        this.dataz = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type coordinates
    // Serialize message field [datax]
    bufferOffset = _arraySerializer.float64(obj.datax, buffer, bufferOffset, null);
    // Serialize message field [datay]
    bufferOffset = _arraySerializer.float64(obj.datay, buffer, bufferOffset, null);
    // Serialize message field [dataz]
    bufferOffset = _arraySerializer.float64(obj.dataz, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type coordinates
    let len;
    let data = new coordinates(null);
    // Deserialize message field [datax]
    data.datax = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [datay]
    data.datay = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [dataz]
    data.dataz = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.datax.length;
    length += 8 * object.datay.length;
    length += 8 * object.dataz.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'beginner_tutorials/coordinates';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6d9fdd56a82d84b20d8a69a500869003';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] datax
    float64[] datay
    float64[] dataz
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new coordinates(null);
    if (msg.datax !== undefined) {
      resolved.datax = msg.datax;
    }
    else {
      resolved.datax = []
    }

    if (msg.datay !== undefined) {
      resolved.datay = msg.datay;
    }
    else {
      resolved.datay = []
    }

    if (msg.dataz !== undefined) {
      resolved.dataz = msg.dataz;
    }
    else {
      resolved.dataz = []
    }

    return resolved;
    }
};

module.exports = coordinates;
