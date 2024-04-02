# SUBSCRIBER TO SUBSCRIBE TO the information published by tv_news_station to the topic "robot_newws"

import rclpy
from rclpy.node import Node


from example_interfaces.msg import String  # data type should be same as publisher
 
 
class SmartphoneS(Node): # MODIFY NAME
    
    
    def __init__(self):
        super().__init__("smartphone_sub") # MODIFY NAME
        #this is name of sunscriber u will call before the main 
        self.subscriber = self.create_subscription(
                                String ,"robot_news", self.callback_robot_news,10) # last is callback


        self.get_logger().info("Smartphone node has been started")#starting message of node 




    def callback_robot_news(self,msg):

        self.get_logger().info(msg.data)






def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneS() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
