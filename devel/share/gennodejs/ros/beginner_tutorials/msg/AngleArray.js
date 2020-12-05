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

class AngleArray {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.theta1 = null;
      this.theta2 = null;
      this.theta3 = null;
      this.alpha = null;
      this.beta = null;
    }
    else {
      if (initObj.hasOwnProperty('theta1')) {
        this.theta1 = initObj.theta1
      }
      else {
        this.theta1 = 0.0;
      }
      if (initObj.hasOwnProperty('theta2')) {
        this.theta2 = initObj.theta2
      }
      else {
        this.theta2 = 0.0;
      }
      if (initObj.hasOwnProperty('theta3')) {
        this.theta3 = initObj.theta3
      }
      else {
        this.theta3 = 0.0;
      }
      if (initObj.hasOwnProperty('alpha')) {
        this.alpha = initObj.alpha
      }
      else {
        this.alpha = 0.0;
      }
      if (initObj.hasOwnProperty('beta')) {
        this.beta = initObj.beta
      }
      else {
        this.beta = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type AngleArray
    // Serialize message field [theta1]
    bufferOffset = _serializer.float32(obj.theta1, buffer, bufferOffset);
    // Serialize message field [theta2]
    bufferOffset = _serializer.float32(obj.theta2, buffer, bufferOffset);
    // Serialize message field [theta3]
    bufferOffset = _serializer.float32(obj.theta3, buffer, bufferOffset);
    // Serialize message field [alpha]
    bufferOffset = _serializer.float32(obj.alpha, buffer, bufferOffset);
    // Serialize message field [beta]
    bufferOffset = _serializer.float32(obj.beta, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type AngleArray
    let len;
    let data = new AngleArray(null);
    // Deserialize message field [theta1]
    data.theta1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [theta2]
    data.theta2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [theta3]
    data.theta3 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [alpha]
    data.alpha = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [beta]
    data.beta = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'beginner_tutorials/AngleArray';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7b26027db0d620ae0522c6284a86339b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 theta1
    float32 theta2
    float32 theta3
    float32 alpha
    float32 beta
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new AngleArray(null);
    if (msg.theta1 !== undefined) {
      resolved.theta1 = msg.theta1;
    }
    else {
      resolved.theta1 = 0.0
    }

    if (msg.theta2 !== undefined) {
      resolved.theta2 = msg.theta2;
    }
    else {
      resolved.theta2 = 0.0
    }

    if (msg.theta3 !== undefined) {
      resolved.theta3 = msg.theta3;
    }
    else {
      resolved.theta3 = 0.0
    }

    if (msg.alpha !== undefined) {
      resolved.alpha = msg.alpha;
    }
    else {
      resolved.alpha = 0.0
    }

    if (msg.beta !== undefined) {
      resolved.beta = msg.beta;
    }
    else {
      resolved.beta = 0.0
    }

    return resolved;
    }
};

module.exports = AngleArray;
