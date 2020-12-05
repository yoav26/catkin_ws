;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::AngleArray)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'AngleArray (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::ANGLEARRAY")
  (make-package "BEGINNER_TUTORIALS::ANGLEARRAY"))

(in-package "ROS")
;;//! \htmlinclude AngleArray.msg.html


(defclass beginner_tutorials::AngleArray
  :super ros::object
  :slots (_theta1 _theta2 _theta3 _alpha _beta ))

(defmethod beginner_tutorials::AngleArray
  (:init
   (&key
    ((:theta1 __theta1) 0.0)
    ((:theta2 __theta2) 0.0)
    ((:theta3 __theta3) 0.0)
    ((:alpha __alpha) 0.0)
    ((:beta __beta) 0.0)
    )
   (send-super :init)
   (setq _theta1 (float __theta1))
   (setq _theta2 (float __theta2))
   (setq _theta3 (float __theta3))
   (setq _alpha (float __alpha))
   (setq _beta (float __beta))
   self)
  (:theta1
   (&optional __theta1)
   (if __theta1 (setq _theta1 __theta1)) _theta1)
  (:theta2
   (&optional __theta2)
   (if __theta2 (setq _theta2 __theta2)) _theta2)
  (:theta3
   (&optional __theta3)
   (if __theta3 (setq _theta3 __theta3)) _theta3)
  (:alpha
   (&optional __alpha)
   (if __alpha (setq _alpha __alpha)) _alpha)
  (:beta
   (&optional __beta)
   (if __beta (setq _beta __beta)) _beta)
  (:serialization-length
   ()
   (+
    ;; float32 _theta1
    4
    ;; float32 _theta2
    4
    ;; float32 _theta3
    4
    ;; float32 _alpha
    4
    ;; float32 _beta
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _theta1
       (sys::poke _theta1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _theta2
       (sys::poke _theta2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _theta3
       (sys::poke _theta3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _alpha
       (sys::poke _alpha (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _beta
       (sys::poke _beta (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _theta1
     (setq _theta1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _theta2
     (setq _theta2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _theta3
     (setq _theta3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _alpha
     (setq _alpha (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _beta
     (setq _beta (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get beginner_tutorials::AngleArray :md5sum-) "7b26027db0d620ae0522c6284a86339b")
(setf (get beginner_tutorials::AngleArray :datatype-) "beginner_tutorials/AngleArray")
(setf (get beginner_tutorials::AngleArray :definition-)
      "float32 theta1
float32 theta2
float32 theta3
float32 alpha
float32 beta

")



(provide :beginner_tutorials/AngleArray "7b26027db0d620ae0522c6284a86339b")


