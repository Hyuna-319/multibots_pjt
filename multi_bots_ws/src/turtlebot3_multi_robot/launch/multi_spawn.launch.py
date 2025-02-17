#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, RegisterEventHandler
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.event_handlers import OnProcessExit
from launch.conditions import IfCondition
import launch.logging
import xacro

def generate_launch_description():
    ld = LaunchDescription()

    
    robots = [
        {'name': 'tb3_0', 'x_pose': '9.5', 'y_pose': '-6.0', 'z_pose': '0.01', 'model': 'turtlebot3_waffle_0'},
        {'name': 'tb3_1', 'x_pose': '9.0', 'y_pose': '-7.0', 'z_pose': '0.01', 'model': 'turtlebot3_waffle_1'},
        {'name': 'tb3_2', 'x_pose': '-2.0', 'y_pose': '0.0', 'z_pose': '0.01', 'model': 'turtlebot3_waffle_2'}
    ]

    TURTLEBOT3_MODEL = 'waffle'
    turtlebot3_gazebo_dir = get_package_share_directory('turtlebot3_multi_robot')
    turtlebot3_urdf = os.path.join(turtlebot3_gazebo_dir, 'urdf', f'turtlebot3_{TURTLEBOT3_MODEL}.urdf')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    declare_use_sim_time = DeclareLaunchArgument(
        name='use_sim_time', default_value=use_sim_time, description='Use simulator time'
    )

    enable_drive = LaunchConfiguration('enable_drive', default='false')
    declare_enable_drive = DeclareLaunchArgument(
        name='enable_drive', default_value=enable_drive, description='Enable robot drive node'
    )
    
    turtlebot3_multi_robot = get_package_share_directory('turtlebot3_multi_robot')
    package_dir = get_package_share_directory('turtlebot3_multi_robot')

    world = os.path.join(
        get_package_share_directory('turtlebot3_multi_robot'),
        'worlds', 'moon.world')

   
    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items(),
    )

    
    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gzclient.launch.py')
        ),
    )

    ld.add_action(declare_use_sim_time)
    ld.add_action(declare_enable_drive)
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)
 
    
    last_action = None  
    
    for robot in robots:
        namespace = '/' + robot['name']

       
        sdf_file = os.path.join(turtlebot3_gazebo_dir, 'models', robot['model'], 'model.sdf')
        urdf_content = xacro.process_file(turtlebot3_urdf).toxml()

        remappings = [('/tf','tf'), ('/tf_static','tf_static')]
                      
        turtlebot_state_publisher = Node(
            package='robot_state_publisher',
            namespace=namespace,
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time,
                             'publish_frequency': 10.0,
                             'robot_description': urdf_content
                              }],
            remappings=remappings,
        )

        
        spawn_turtlebot3 = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-file', sdf_file,
                '-entity', robot['name'],
                '-x', robot['x_pose'], '-y', robot['y_pose'],
                '-z', '0.01', '-Y', '0.0',
                '-unpause',
            ],
            output='screen',
        )

        if last_action is None:
            
            ld.add_action(turtlebot_state_publisher)
            ld.add_action(spawn_turtlebot3)
        else:
            
            spawn_turtlebot3_event = RegisterEventHandler(
                event_handler=OnProcessExit(
                    target_action=last_action,
                    on_exit=[turtlebot_state_publisher, spawn_turtlebot3],
                )
            )
            ld.add_action(spawn_turtlebot3_event)

        
        last_action = spawn_turtlebot3

    return ld
