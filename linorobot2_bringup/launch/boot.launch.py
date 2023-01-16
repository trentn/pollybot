from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare("linorobot2_bringup"), '/launch', '/bringup.launch.py']
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare("linorobot2_navigation"), '/launch', '/slam.launch.py']
            )
        ),
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource([
        #         FindPackageShare("linorobot2_navigation"), '/launch', '/navigation.launch.py']
        #     )
        # ),
    ])