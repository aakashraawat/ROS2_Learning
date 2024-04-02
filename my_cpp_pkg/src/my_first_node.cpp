#include "rclcpp/rclcpp.hpp"
//use shift +alt+p c/c++:config and add ros/humble/include 

using namespace std ;



// everthing you write will be in the node class and change name accordingly too usage

class MyNode: public  rclcpp::Node // take care of capital letters

{ // name of the node 

public:
    MyNode(): Node ("cpp_test"),counter_(0) // Constructor node wíth the node name 
    {

       

        RCLCPP_INFO(this-> get_logger(), "Hello Cpp node"); // print  somethimh


        timer_ = this-> create_wall_timer(std::chrono::seconds(1), // create a timer

                                            std ::bind(&MyNode::timerCallback,this )); // call the function callnack

    }




private : 
    // add a timer (callback) so it can give the print with desired feq
    void timerCallback() {

        counter_++;// increment


        RCLCPP_INFO(this-> get_logger(), "Hello %d " , counter_) ; // print in the call back function
    }

        rclcpp::TimerBase::SharedPtr timer_; // declare timer

        int counter_;// declare counter 



};
    




int main(int argc , char **argv){

    rclcpp::init(argc , argv);// init ros2 communication




    auto node = make_shared<MyNode>(); // create a node (its a shared pointer to node)!!!!!

   

    
    rclcpp::spin(node); // stop the program with ctrl +c before that function will be workinh
    rclcpp::shutdown(); // it will shutdown when we press the c and kil the node 





    return 0;
}