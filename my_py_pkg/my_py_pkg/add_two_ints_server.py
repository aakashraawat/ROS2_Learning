import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts 
 
 
class AddTwoIntServerNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("add_two_ints_server") # node name NAME
        
        
        
        
        #Create a service !!!! (service type , name of service , callback function(needed when u send request  u need a function return something))
        self.server_ = self.create_service(AddTwoInts ,"add_two_ints",self.callback_add_two_int)
        
        self.get_logger().info("Add server have been started")
        
        
        #callback function 
    
    def callback_add_two_int(self,request,response):
            response.sum = request.a + request.b# request for the noth ints a and b
            
            self.get_logger().info(str(request.a)+ "+" + str(request.b)  + "=" + str(response.sum) )
            return response
        
        
        

        
    

 
 
 
def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntServerNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()