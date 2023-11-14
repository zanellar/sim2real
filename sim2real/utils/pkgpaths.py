
import os
import sim2real

 
class PkgPath():

    '''
    This class is used to store the paths to the folders in the package.
    '''

    _PACKAGE_PATH = sim2real.__path__[0]  

    CONFIGS = os.path.join(_PACKAGE_PATH, os.pardir, "data", "configs")  
    LOGS = os.path.join(_PACKAGE_PATH, os.pardir, "data", "logs")   
  
 