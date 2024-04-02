#use a default template of client
import rclpy

from rclpy.node import Node


from example_interfaces.srv import AddTwoInts 
from functools import partial
 
 
 
class AddTwoIntsClientNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("add_two_ints_client") # MODIFY NAME
        
        #call the service 
        self.call_add_two_ints_server(6,7)
    
    
    
    
    def call_add_two_ints_server(self,a,b):
        
        client = self.create_client(AddTwoInts,"add_two_ints" ) # creaze a client 
        
        while not client.wait_for_service (1.0):  # wait for the server 
            self.get_logger().warn("waiting for two ints too add...")
            
        
        request = AddTwoInts.Request()   #create a request 
        request.a = a
        request.b = b
        
        
        future = client.call_async(request)   # semd a request asynchronoly
        future.add_done_callback( partial(self.callback_call_add_two_ints, a= a ,b=b))
        
        
    def callback_call_add_two_ints(self, future,a,b): # init th callback
        try:  
            response = future.result()   # reponse is called in callback
            self.get_logger().info(str(request.a)+ "+" + str(request.b)  + "=" + str(response.sum) )
            
            
        except Exception as e :# if exception it will be failed
            
            self.get_logger().error("Service call failed %r"  % (e,))
        
        
        
            
        

 
def main(args=None):
    rclpy.init(args=args)
    
    node =AddTwoIntsClientNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
