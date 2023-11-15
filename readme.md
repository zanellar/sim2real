 
## Installation ##

Install MuJoCo (2.1)

Make sure you have installed nvidia drivers.

Install GLFW dynamic library
``` 
sudo apt update
sudo apt upgrade
sudo apt install libosmesa6-dev libgl1-mesa-glx libglfw3
sudo apt-get install libglew-dev
``` 

Download and extract MuJoCo v2.1
``` 
wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz
mkdir ~/.mujoco/
tar -xf mujoco210-linux-x86_64.tar.gz -C ~/.mujoco/
rm mujoco210-linux-x86_64.tar.gz 
``` 

Add the following line to the `.bashrc ` (replacing [your-user])
``` 
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/[your-user]/.mujoco/mujoco210/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so
``` 

Verify the installation of MuJoCo
```
cd ~/.mujoco/mujoco210/bin
./simulate ../model/humanoid.xml
```

Create conda environment
```
conda env create -f environment.yml
```
  
Install 'mjrlenv': 
```
git clone https://github.com/zanellar/mjrlenvs.git
cd mjrlenvs
pip install -e .
```

Install 'sim2real' (this packege)
```
cd ..
cd sim2real
pip install -e .
``` 


## Mujoco ##
## XML
quaternions are in the format [qw,qx,qy,qz]

### Contact Forces bug
Issue: https://github.com/openai/mujoco-py/pull/487
Need to modify 'mujoco_py/mjviewer.py' in the conda env as follow:
https://github.com/openai/mujoco-py/pull/487/commits/ab026c1ff8df54841a549cfd39374b312e8f00dd

 