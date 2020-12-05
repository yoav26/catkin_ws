;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::coordinates)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'coordinates (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::COORDINATES")
  (make-package "BEGINNER_TUTORIALS::COORDINATES"))

(in-package "ROS")
;;//! \htmlinclude coordinates.msg.html


(defclass beginner_tutorials::coordinates
  :super ros::object
  :slots (_datax _datay _dataz ))

(defmethod beginner_tutorials::coordinates
  (:init
   (&key
    ((:datax __datax) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:datay __datay) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:dataz __dataz) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _datax __datax)
   (setq _datay __datay)
   (setq _dataz __dataz)
   self)
  (:datax
   (&optional __datax)
   (if __datax (setq _datax __datax)) _datax)
  (:datay
   (&optional __datay)
   (if __datay (setq _datay __datay)) _datay)
  (:dataz
   (&optional __dataz)
   (if __dataz (setq _dataz __dataz)) _dataz)
  (:serialization-length
   ()
   (+
    ;; float64[] _datax
    (* 8    (length _datax)) 4
    ;; float64[] _datay
    (* 8    (length _datay)) 4
    ;; float64[] _dataz
    (* 8    (length _dataz)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _datax
     (write-long (length _datax) s)
     (dotimes (i (length _datax))
       (sys::poke (elt _datax i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _datay
     (write-long (length _datay) s)
     (dotimes (i (length _datay))
       (sys::poke (elt _datay i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _dataz
     (write-long (length _dataz) s)
     (dotimes (i (length _dataz))
       (sys::poke (elt _dataz i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _datax
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _datax (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _datax i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _datay
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _datay (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _datay i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _dataz
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _dataz (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _dataz i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get beginner_tutorials::coordinates :md5sum-) "6d9fdd56a82d84b20d8a69a500869003")
(setf (get beginner_tutorials::coordinates :datatype-) "beginner_tutorials/coordinates")
(setf (get beginner_tutorials::coordinates :definition-)
      "float64[] datax
float64[] datay
float64[] dataz

")



(provide :beginner_tutorials/coordinates "6d9fdd56a82d84b20d8a69a500869003")


