"""
Code written by Michele Castriotta and Andrea Bassi for controlling the Polimi shutter,
sending HIGH and LOW signal to the RTS line of the USB port. The shutter is implemented 
for working in ScopeFoundry (http://www.scopefoundry.org/).

11-10-2018, Milan

This script creates the hardware class for the shutter, that manages the GUI.
"""


from ScopeFoundry import HardwareComponent 
from shutter_device import ShutterDevice

class ShutterHW(HardwareComponent):
    """
    Define a new class ShutterHW, defined as a subclass of Hardware component (defined in ScopeFoundry)
    """
    
    name = 'Shutter' 
    
    def setup(self):
        """
        The setup function creates the logged quantities we need for controlling the shutter
        """
        #creates a port value in the GUI
        self.port = self.add_logged_quantity('port', dtype=str, initial = 'COM5') 
        #creates a boolean in the GUI for controlling the shutter
        self.shutter_closed = self.add_logged_quantity('shutter closed', dtype=bool, initial = True)
        
        
    def connect(self):
        
        #open connection to hardware
        self.port.change_readonly(True)
        #when we connect the shutter, we want a default value
        self.shutter_closed.update_value(True)
        #define a ShutterDevice object with the port attribute equal to the logged quantity value
        self.shutter = ShutterDevice(port = self.port.val, debug=self.debug_mode.val)
        #This instruction, through scope foundry functions, connect the value of shutter_closed to thechange_shutter function
        #Logged quantity shutter_closed ----> change_shutter! (a sort of connection between interface and device)
        self.shutter_closed.hardware_set_func = self.shutter.change_shutter

    def disconnect(self):
        self.port.change_readonly(False)
        #disconnect hardware
        if hasattr(self, 'shutter'):
            self.shutter.close()
            del self.shutter
            
        
        
        