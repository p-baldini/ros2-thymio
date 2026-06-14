# ROS2—Thymio-II interaction

This repository contains some information to use the Thymio-II robot with ROS2.
The procedure have been tested on a Manjaro linux distribution with ROS2 Jazzy Jalisco.

## Setup steps

1\. Install conda:

```
$ curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash ./Miniconda3-latest-Linux-x86_64.sh
```

2\. Create the conda environment, add packages channels, and install required packages:

```
$ source ~/.bashrc
$ conda create -n ros_env python=3.12.13
$ conda activate ros_env
$ conda config --env --add channels conda-forge
$ conda config --env --add channels robostack
$ conda config --env --add channels robostack-jazzy
$ conda install ros-jazzy-desktop-full
$ conda install libudev
```

3\. Clone and install the ros-aseba package:

```
$ git clone https://github.com/jeguzzi/ros-aseba.git --branch ros2 --depth=1
$ source ~/miniconda3/envs/ros_env/setup.zsh
$ colcon build --merge-install
$ source install/setup.zsh
```

4\. Install the dashel package:

```
$ git clone https://github.com/aseba-community/dashel.git --depth=1
$ colcon build --merge-install --cmake-args -DCMAKE_POLICY_VERSION_MINIMUM=3.5
```

5\. Identify the port at which the Thymio-II is connected (from now on we will assume /dev/ttyACM0):

```
$ sudo dmesg
```

6\. If you are not root, you may want to get access to the device (note that this is potentially an unsafe approach):

```
$ sudo chmod 777 /dev/ttyACM0
```

7\. Install your code package to be launched by ROS2:

```
$ colcon build --merge-install
```

8\. Launch your ROS2 package:

```
$ ros2 launch PACKAGE_NAME FILE_NAME.launch device:="ser:name=Thymio-II"
```

## Troubleshoot

- If asebaros returns the error `Connection failed (0)` check that the Thymio-II is turned on.
- If asebaros returns the error `Connection failed (13)` you probably don't have the rights to used the device; in this case, you can run the following command `sudo chmod 777 /dev/ttyACM0` (note that the device name may differ).
- If specifying the name of the robot (i.e., `device:="ser:name=Thymio-II"`) does not permit finding the device, you can try to specify directly the path with `device:="ser:device=/dev/ttyACM0"`.
