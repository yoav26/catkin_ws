#include <ros/ros.h>
#include <visualization_msgs/Marker.h>
#include <beginner_tutorials/coordinates.h>
#include "std_msgs/UInt16MultiArray.h"
#include <cmath>

#define ratio 100

class SubscribeAndPublish
{
public:
  SubscribeAndPublish()
  {
    //Topic you want to publish
    pub_ = n_.advertise<visualization_msgs::Marker>("visualization_marker", 10);

    //Topic you want to subscribe
    sub_ = n_.subscribe("current_coordinates", 1000, &SubscribeAndPublish::callback, this);
	


  }

  void callback(const beginner_tutorials::coordinates::ConstPtr& input)
  {
		visualization_msgs::Marker points, line_strip;
		points.header.frame_id = line_strip.header.frame_id = "/my_frame";
		points.header.stamp = line_strip.header.stamp = ros::Time::now();
		points.ns = line_strip.ns = "points_to_vis";
		points.action = line_strip.action = visualization_msgs::Marker::ADD;
		points.pose.orientation.w = line_strip.pose.orientation.w = 1.0;

		points.id = 0;
		line_strip.id = 1;

		points.type = visualization_msgs::Marker::POINTS;
		line_strip.type = visualization_msgs::Marker::LINE_STRIP;

		// POINTS markers use x and y scale for width/height respectively
		points.scale.x = 0.2;
		points.scale.y = 0.2;

		// LINE_STRIP markers use only the x component of scale, for the line width
		line_strip.scale.x = 0.1;

		// Points are red
		points.color.r = 1.0f;
		points.color.a = 1.0;

		// Line strip is blue
		line_strip.color.b = 1.0;
		line_strip.color.a = 1.0;

	  
	  
		geometry_msgs::Point p;
		
		for (uint32_t i = 0; i < input->datax.size(); ++i)
		{
			p.x = input->datax[i]/ratio;
			p.y = input->datay[i]/ratio;
			p.z = input->dataz[i]/ratio;
			points.points.push_back(p);
			line_strip.points.push_back(p);
		}
		pub_.publish(points);
		pub_.publish(line_strip);
  }

private:
  ros::NodeHandle n_; 
  ros::Publisher pub_;
  ros::Subscriber sub_;

};//End of class SubscribeAndPublish

int main(int argc, char **argv)
{
  //Initiate ROS
  ros::init(argc, argv, "subscribe_and_publish");

  //Create an object of class SubscribeAndPublish that will take care of everything
  SubscribeAndPublish SAPObject;
  



  ros::spin();

  return 0;
}
