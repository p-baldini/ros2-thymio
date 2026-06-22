# ROS2—Thymio-II interaction

This repository contains some information to use the Thymio-II robot with ROS2.
The procedure have been tested on a Arch Linux distribution and seems to work both for cable-connected and dongle-connected robots.
Unfortunately, the procedure does not seems to work under MacOS due to the impossibility of accessing the port from inside a container.

This readme file is organized as follows:
1. [Setup steps](#setup-steps)
2. [PC—Thymio-II interaction](#pcthymio-ii-interaction)
3. [Troubleshoot](#troubleshoot)

## Setup steps

1\. Install Docker:

```
$ sudo pacman -S docker
$ sudo systemctl start docker
$ sudo systemctl enable docker
$ sudo usermod -aG docker $USER # add your user to the docker group to run Docker commands without sudo
```

2\. Build the docker image:

```
$ docker buildx build --no-cache --debug -t pbaldini/ros-aseba:lyrical .
```

3\. Start the docker container with access to the connected devices:

```
$ docker run \                      # start a new container
    --rm \                          # the container is removed after termination
    -it \                           # start the container in interactive mode
    --privileged \                  # the container has access to all the devices connected to the system (potential vulnerability issue)
    -v `pwd`:/ros_ws/src \          # show the current directory in the container at the specified path
    --workdir /ros_ws/src \         # set the work directory insider the container as the mirror of this launch directory
    pbaldini/ros-aseba:lyrical \    # launch the ros-aseba foxy image
    bash                            # use the bash terminal as entrypoint
```

4\. Install your code package to be launched by ROS2:

```
$ colcon build --merge-install
$ source install/setup.sh
```

5\. Launch your ROS2 package:

```
$ ros2 launch PACKAGE_NAME FILE_NAME.launch
```

## PC—Thymio-II interaction

You can control the Thymio-II directly from the PC by using ROS2.
You can find some examples on how to do it via cli at [this link](https://github.com/jeguzzi/ros-aseba/blob/9f96bec7524c4c337110acf129a5c81da34345e7/docs/_sources/examples.rst.txt#L61), and on how to do it programmatically in the `example` folder.
In any case, the first step will be to open another shell in the container:

```
$ docker exec -it CONTAINER_NAME bash
$ source install/setup.sh
```

You can now interact with the node, for example by running:

```
$ ros2 topic echo /node_51214/aseba/description
$ ros2 topic pub -r 1 /node_51214/aseba/events/message asebaros_msgs/Event '{data:  [100]}'
```

## Troubleshoot

- If asebaros returns the error `Connection failed (0)` check that the Thymio-II is turned on.
- If asebaros returns the error `Connection failed (13)` you probably don't have the rights to used the device; in this case, you can run the following command `sudo chmod 777 /dev/ttyACM0` (note that the device name may differ).
- If specifying the name of the robot (i.e., `device:="ser:name=Thymio-II"`) does not permit finding the device, you can try to specify directly the path with `device:="ser:device=/dev/ttyACM0"`.
- If the robot behavior differs from what you code, ensure that the path variable in the .launch file points to the correct script.
- Using `device:="ser:name=Thymio-II"` seems to work also when using the USB dongle; nevertheless, in case of error you could try to use also `device:="ser:name=Thymio-II Wireless"`.
