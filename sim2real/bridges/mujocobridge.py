from sim2real.bridges.basebridge import BaseBridge
from mjrlenvs.scripts.env.mjenv import MjEnv 

class MujocoBridge(BaseBridge):
    
    def __init__(self, config):
        super().__init__(config)
        # Env params
        self.sim = MjEnv(
            env_name = self.config["env"],   
            max_episode_length = self.config["max_episode_length"],
            init_joint_config = self.config["init_joint_config"], 
        )

    def execute(self, action):
        self.sim.execute(action) 
        self.sim.render()
    
    def measure(self, id): 
        if id == "eef_pos":
            return self.sim.get_obj_pos("end_effector")
        if id == "joint_pos":
            return self.sim.get_joints_pos()
        if id == "joint_vel":
            return self.sim.get_joints_vel() 
    
