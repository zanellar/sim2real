
from sim2real.bridges.mujocobridge import MujocoBridge
from sim2real.bridges.isaacbridge import IsaacBridge
from sim2real.bridges.rosbridge import RosBridge

class RobotController:
    def __init__(self, config):
        if type(config) == str:
            import json
            with open(config, "r") as f:
                self.config = json.load(f)
        elif type(config) == dict:
            self.config = config 
        else:
            raise Exception("Config must be either a path to a json file or a dictionary")
        
        self.setbridge(self.config["bridge"])
 
    def setbridge(self, bridge):
        '''
        Set the bridge to be used. Available bridges are:
        - "mujoco" for using the Mujoco Simulator
        - "isaac" for using the Isaac Simulaor
        - "ros" for using the real robot by means of ROS
        '''
        if bridge == "mujoco":
            self.bridge = MujocoBridge(self.config)
        elif bridge == "isaac":
            self.bridge = IsaacBridge(self.config)
        elif bridge == "ros":
            self.bridge = RosBridge(self.config)
        else:
            raise Exception("Bridge not supported")

    def execute(self, action):
        '''
        Execute the action on the robot
        '''
        self.bridge.execute(action)

    def reset(self):
        '''
        Reset the robot and the environment
        '''
        self.bridge.reset()
 
    def measure(self, id):
        '''
        Get the observation from the environment specified by id. 
        Available ids are:
        - "eef_pos" for the end-effector position
        - "eef_quat" for the end-effector orientation
        - "eef_vel" for the end-effector velocity
        - "eef_omg" for the end-effector angular velocity
        - "joints" for the joint positions
        - "joints_vel" for the joint velocities
        - "joints_tor" for the joint torques
        '''
        return self.bridge.measure(id)