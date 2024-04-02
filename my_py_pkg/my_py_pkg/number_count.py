## always check the intendation error as both init and callback function should be in the smae file
import rclpy
from rclpy.node import Node


from example_interfaces.msg import Int64
 
 
class NumberCounterNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("number_count") # MODIFY NAME
        
        self.counter_ = 0 #init a counter 
        
        #publisher!!
        self.number_count_publisher_ = self.create_publisher(Int64, "number_count", 10)# change the topic name to the question (given)
        
        
        
        
        
        
        
        #subscriber
        self.number_subscriber_ = self.create_subscription(
                                Int64 ,"number", self.callback_number,10) # last is callback and same topic as publisher

        self.get_logger().info("Number counter subs has been started")#starting message of node
        
        
        
        
    def callback_number(self,msg): # when we recieve message
            
            self.counter_ += msg.data #here is our messge we will get when we subscribe to topic ie everytime we reciever we will be +1 

            #self.get_logger().info(str(self.counter_))
            pub_msg = Int64()
            pub_msg.data= self.counter_ ## take the msg from the subscriber node ie self_counter
            self.number_count_publisher_.publish(pub_msg) 
            
            
            
            

        
 
 
def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
