#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


from example_interfaces.msg import String 
 
 
class RobotNewsStationNode(Node): # MODIFY NAME
    
    def __init__(self):
        super().__init__("Robot_news_station") # NODE NAME or publisher name
        #parameters 
        
        self.declare_parameter("robot_name","Aakashoid") # paramete name and what it i
        
        self.robot_name_ = self.get_parameter("robot_name").value # dont forget the value 
        
        
        
        
        
        
        
        
        # init a punlisher 
        self.publisher_ = self.create_publisher(String, "robot_news" , 10)  # when writing a publsiher everytime (msg_type(import), "Topic_name ", (que size ))

        #create a timer for the publishing (time, callback function)

        self.timer_ = self.create_timer(0.5, self.publish_news )
        self.get_logger().info("Robot new timer has been started ") # start of the timer




    # make a function for publisher 
    def publish_news(self):
        msg = String()   # you can check topics by running ros2 run publisher and type ros2 ztopic list and than _<----------->
        
        msg.data ="Hello this is "+ \
            str(self.robot_name_) +"message published from topic robot_news"  # ros2 topic echo / topic_name (here its robot news)
        
        
        #publish the message 
        self.publisher_.publish(msg)

        




 









 
def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()