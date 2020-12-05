; Auto-generated. Do not edit!


(cl:in-package beginner_tutorials-msg)


;//! \htmlinclude AngleArray.msg.html

(cl:defclass <AngleArray> (roslisp-msg-protocol:ros-message)
  ((theta1
    :reader theta1
    :initarg :theta1
    :type cl:float
    :initform 0.0)
   (theta2
    :reader theta2
    :initarg :theta2
    :type cl:float
    :initform 0.0)
   (theta3
    :reader theta3
    :initarg :theta3
    :type cl:float
    :initform 0.0)
   (alpha
    :reader alpha
    :initarg :alpha
    :type cl:float
    :initform 0.0)
   (beta
    :reader beta
    :initarg :beta
    :type cl:float
    :initform 0.0))
)

(cl:defclass AngleArray (<AngleArray>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AngleArray>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AngleArray)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-msg:<AngleArray> is deprecated: use beginner_tutorials-msg:AngleArray instead.")))

(cl:ensure-generic-function 'theta1-val :lambda-list '(m))
(cl:defmethod theta1-val ((m <AngleArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:theta1-val is deprecated.  Use beginner_tutorials-msg:theta1 instead.")
  (theta1 m))

(cl:ensure-generic-function 'theta2-val :lambda-list '(m))
(cl:defmethod theta2-val ((m <AngleArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:theta2-val is deprecated.  Use beginner_tutorials-msg:theta2 instead.")
  (theta2 m))

(cl:ensure-generic-function 'theta3-val :lambda-list '(m))
(cl:defmethod theta3-val ((m <AngleArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:theta3-val is deprecated.  Use beginner_tutorials-msg:theta3 instead.")
  (theta3 m))

(cl:ensure-generic-function 'alpha-val :lambda-list '(m))
(cl:defmethod alpha-val ((m <AngleArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:alpha-val is deprecated.  Use beginner_tutorials-msg:alpha instead.")
  (alpha m))

(cl:ensure-generic-function 'beta-val :lambda-list '(m))
(cl:defmethod beta-val ((m <AngleArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:beta-val is deprecated.  Use beginner_tutorials-msg:beta instead.")
  (beta m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AngleArray>) ostream)
  "Serializes a message object of type '<AngleArray>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'theta1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'theta2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'theta3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'alpha))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'beta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AngleArray>) istream)
  "Deserializes a message object of type '<AngleArray>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'theta1) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'theta2) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'theta3) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'alpha) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'beta) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AngleArray>)))
  "Returns string type for a message object of type '<AngleArray>"
  "beginner_tutorials/AngleArray")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AngleArray)))
  "Returns string type for a message object of type 'AngleArray"
  "beginner_tutorials/AngleArray")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AngleArray>)))
  "Returns md5sum for a message object of type '<AngleArray>"
  "7b26027db0d620ae0522c6284a86339b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AngleArray)))
  "Returns md5sum for a message object of type 'AngleArray"
  "7b26027db0d620ae0522c6284a86339b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AngleArray>)))
  "Returns full string definition for message of type '<AngleArray>"
  (cl:format cl:nil "float32 theta1~%float32 theta2~%float32 theta3~%float32 alpha~%float32 beta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AngleArray)))
  "Returns full string definition for message of type 'AngleArray"
  (cl:format cl:nil "float32 theta1~%float32 theta2~%float32 theta3~%float32 alpha~%float32 beta~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AngleArray>))
  (cl:+ 0
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AngleArray>))
  "Converts a ROS message object to a list"
  (cl:list 'AngleArray
    (cl:cons ':theta1 (theta1 msg))
    (cl:cons ':theta2 (theta2 msg))
    (cl:cons ':theta3 (theta3 msg))
    (cl:cons ':alpha (alpha msg))
    (cl:cons ':beta (beta msg))
))
