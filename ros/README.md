# Robot Operating System (ROS)

# Clang How-To
Install the clang ecosystem
```bash
wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add -
sudo add-apt-repository 'deb http://apt.llvm.org/bionic/ llvm-toolchain-bionic main'
sudo apt update
sudo apt install -y clangd clang-format clang-tidy
```
Install vscode's clang-d extension, and disable any current C/C++ linter.



## Setting up your catkin workspace
```bash
catkin create pkg PKG_NAME std_msgs roscpp rospy
```
[How to and when to implement ROS timers](https://answers.ros.org/question/199727/how-to-use-timer/)