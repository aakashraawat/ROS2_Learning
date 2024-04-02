#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class SmartphoneNode : public rclcpp::Node
{
public:
    SmartphoneNode() : Node("smartphone")
    {
        subscriber_ = this->create_subscription<example_interfaces::msg::String>( // 
            "robot_news", 10, // subscribe to the same topic as the publisher
            
            std::bind(&SmartphoneNode::callbackRobotNews, this, std::placeholders::_1));// nind the callback , 



        RCLCPP_INFO(this->get_logger(), "Smartphone has been started."); // print for the call back
    }





private:
    void callbackRobotNews(const example_interfaces::msg::String::SharedPtr msg) // this is always same use of const
    {
        RCLCPP_INFO(this->get_logger(), "%s", msg->data.c_str());// print on the start
    }

    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;
};








int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<SmartphoneNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
