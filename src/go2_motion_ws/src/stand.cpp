#include <unistd.h>
#include <iostream>
#include <string>

#include <unitree/robot/channel/channel_factory.hpp>
#include <unitree/robot/go2/sport/sport_client.hpp>

int main(int argc, char** argv)
{
    std::cout << "Go2 stand start" << std::endl;

    if (argc < 2)
    {
        std::cout << "Usage: ros2 run go2_motion_ws standandlie <networkInterface>" << std::endl;
        std::cout << "Example: ros2 run go2_motion_ws standandlie eno1" << std::endl;
        return -1;
    }

    std::cout << "network interface: " << argv[1] << std::endl;

    std::cout << "ChannelFactory Init..." << std::endl;
    unitree::robot::ChannelFactory::Instance()->Init(0, argv[1]);

    std::cout << "SportClient create..." << std::endl;
    unitree::robot::go2::SportClient sport_client;

    std::cout << "SportClient Init..." << std::endl;
    sport_client.SetTimeout(10.0f);
    sport_client.Init();

    std::cout << "Go2 command ready" << std::endl;
    std::cout << "commands: stand / lie / balance / stop / exit" << std::endl;

    std::string input;

    while (true)
    {
        std::cout << "> ";
        std::cin >> input;

        if (input == "stand")
        {
            std::cout << "StandUp..." << std::endl;
            sport_client.StandUp();
            sleep(3);
            sport_client.BalanceStand();
        }
        else if (input == "lie")
        {
            std::cout << "StandDown..." << std::endl;
            sport_client.StandDown();
            sleep(3);
        }
        else if (input == "balance")
        {
            std::cout << "BalanceStand..." << std::endl;
            sport_client.BalanceStand();
        }
        else if (input == "stop")
        {
            std::cout << "StopMove..." << std::endl;
            sport_client.StopMove();
        }
        else if (input == "exit")
        {
            std::cout << "Exit" << std::endl;
            break;
        }
        else
        {
            std::cout << "unknown command" << std::endl;
        }
    }

    return 0;
}