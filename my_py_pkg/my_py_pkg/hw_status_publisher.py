
import rclpy
from rclpy.node import Node

from my_robot_interface.msg import HardwareStatus


#add msg type here
 
 
class HwStatusPublisherNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("hw_status_publisher") # MODIFY NAME
        # 1. what to publish and what frequecy and whats the topic
        self.hw_status_publisher_ = self.create_publisher(HardwareStatus, "hardware_status" , 10)
        
        # create a timer use same function as u created for publishing
        
        self.timer_ = self.create_timer(1 , self.publish_hw_status)
        #3.print something
        self.get_logger().info("Hardware status information is publishing")
        
        
        
    # 2.(publishing of data )function to publish a news     
    def publish_hw_status(self):
        msg = HardwareStatus()
        msg.temperature= 45
        msg.motors_ready= True
        msg.debug_message = "Nothing special just to debug " 
        
        # publish the message
        self.hw_status_publisher_.publish(msg)
 
def main(args=None):
    rclpy.init(args=args)
    node = HwStatusPublisherNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
