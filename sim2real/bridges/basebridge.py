class BaseBridge:

    def __init__(self, config):
        '''
        Initialize the bridge with the configuration specified in config file (dict)
        '''
        self.config = config
    
    def execute(self, action):
        '''
        Execute the action on the robot
        '''
        raise NotImplementedError
    
    def reset(self):
        '''
        Reset the robot and the environment
        '''
        raise NotImplementedError
    
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
        if id == "eef_pos":
            return self.sim.get_obj_pos("end_effector")  
        if id == "eef_quat":
            raise NotImplementedError
        if id == "eef_vel":
            raise NotImplementedError
        if id == "eef_omg":
            raise NotImplementedError
        if id == "joint_pos":
            return self.sim.get_joints_pos()
        if id == "joint_vel":
            return self.sim.get_joints_vel()
        if id == "joint_tor":
            raise NotImplementedError
        return None
    

        