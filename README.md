# ROS2—Thymio-II interaction

This repository contains some information to use the Thymio-II robot with ROS2.
The procedure have been tested on a Manjaro linux distribution with ROS2 Jazzy Jalisco, and seems to work both for cable-connected and dongle-connected robots.

This readme file is organized as follows:
1. [Setup steps](#setup-steps)
2. [PC—Thymio-II interaction](#pcthymio-ii-interaction)
3. [Troubleshoot](#troubleshoot)

## Setup steps

1\. Install Conda:

```
$ curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash ./Miniconda3-latest-Linux-x86_64.sh
```

2\. Create the Conda environment, add packages channels, and install required packages:

```
$ conda create -n ros2 python=3.12.13
$ conda activate ros2
$ conda config --env --add channels conda-forge
$ conda config --env --add channels robostack-jazzy
$ conda install ros-jazzy-desktop-full
$ conda install libudev # OPTIONAL; useful under linux
$ python -m ensurepip
$ python -m pip install colcon-common-extensions # OPTIONAL; under linux it gets installed automatically
$ source $CONDA_PREFIX/setup.zsh
```

3\. Install the ros-aseba and the dashel packages (submodules of this repository):

```
$ colcon build --merge-install
$ source install/setup.zsh
```

4\. Identify the port at which the Thymio-II is connected (from now on we will assume /dev/ttyACM0):

```
$ sudo dmesg
```

5\. If you are not root, you may want to get access to the device (note that this is potentially an unsafe approach):

```
$ sudo chmod 777 /dev/ttyACM0
```

6\. Install your code package to be launched by ROS2:

```
$ colcon build --merge-install
```

7\. Launch your ROS2 package:

```
$ ros2 launch PACKAGE_NAME FILE_NAME.launch device:="ser:name=Thymio-II"
```

## PC—Thymio-II interaction

You can control the Thymio-II directly from the PC by using ROS2.
You can find some examples on how to do it at [this link](https://github.com/jeguzzi/ros-aseba/blob/9f96bec7524c4c337110acf129a5c81da34345e7/docs/_sources/examples.rst.txt#L61).

## Troubleshoot

- If asebaros returns the error `Connection failed (0)` check that the Thymio-II is turned on.
- If asebaros returns the error `Connection failed (13)` you probably don't have the rights to used the device; in this case, you can run the following command `sudo chmod 777 /dev/ttyACM0` (note that the device name may differ).
- If specifying the name of the robot (i.e., `device:="ser:name=Thymio-II"`) does not permit finding the device, you can try to specify directly the path with `device:="ser:device=/dev/ttyACM0"`.
- If the robot behavior differs from what you code, ensure that the path variable in the .launch file points to the correct script.
- Using `device:="ser:name=Thymio-II"` seems to work also when using the USB dongle; nevertheless, in case of error you could try to use also `device:="ser:name=Thymio-II Wireless"`.
