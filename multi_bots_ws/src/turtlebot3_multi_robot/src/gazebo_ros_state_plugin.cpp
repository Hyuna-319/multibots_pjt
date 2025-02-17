#include <gazebo/gazebo.hh>
#include <gazebo/common/Plugin.hh>

namespace gazebo
{
  class GazeboRosStatePlugin : public SystemPlugin
  {
    public: 
      void Load(int _argc, char **_argv) override
      {
        std::cout << "Gazebo ROS State Plugin Loaded!" << std::endl;
      }
  };
  
  
  GZ_REGISTER_SYSTEM_PLUGIN(GazeboRosStatePlugin)
}
