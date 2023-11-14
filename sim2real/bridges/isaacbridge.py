from sim2real.bridges.basebridge import BaseBridge

class IsaacBridge(BaseBridge):
    
    def __init__(self, config):
        super().__init__(config)

    def execute(self, action):
        pass
    
    def measure(self, id):
        return None
    
