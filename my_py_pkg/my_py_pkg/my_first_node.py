#first node in python in ros 2
#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node  

class MyNode(Node):
    
    def __init__(self): #contructor
        super().__init__("Py_test_first_N_OOP") # name of the node 

        self.counter_ = 0 #add a counter
        
        self.get_logger().info("Hello this Is first python node")#print something

        self.create_timer(1 , self.timer_callback)#create a timer ie how many time spam it will run
    
    
    # now write a function and use this timer for 0.5 hz && use the counter in the func
        
    def timer_callback(self): ## take care for intendation 
       
        self.counter_ += 1

        self.get_logger().info ( " Helloo " + str(self.counter_) )



def main (args =None): #init tos communication

    rclpy.init(args =args ) # Always write this too start ros communication

    node = MyNode()#call it from the class above 
    
    
    
    rclpy.spin(node)# program will not end



    rclpy.shutdown()#exit the node 


if __name__ == "__main__":
    main()

