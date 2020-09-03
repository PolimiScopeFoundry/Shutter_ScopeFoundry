"""
Code written by Michele Castriotta and Andrea Bassi for controlling the Polimi shutter,
sending HIGH and LOW signal to the RTS line of the USB port. The shutter is implemented 
for working in ScopeFoundry (http://www.scopefoundry.org/).

11-10-2018, Milan

This script create the device class for the shutter, and all related functions.
"""


import serial #the shutter communicates with serial protocol
import time

class ShutterDevice(object):
    """
    Define the ShutterDevice class, including the attributes of the shutter,
    and all the functions needed for manage it (open, close, ecc...)
    """
    
    
    def __init__(self,port,debug=False,dummy=False): 
        """
        Every time a new object of the class ShutterDevice is created,
        the function __init__ is called. Here we define some attributes
        of the device. The arguments of the __init__ function
        are the arguments to give to the new ShutterDevice object created.
        """
        
        #debug, dummy and port are attributes of the ShutterDevice object
        self.debug=debug 
        self.dummy=dummy
        self.port=port #define the port to which the shutter is connected
        
        if not self.dummy: #if we are not in dummy session:
            
            self.ser = ser = serial.Serial(port=self.port , baudrate=19200 ,bytesize=8  #define another attribute named ser, 
                                           ,parity='N', stopbits=1, xonxoff=True)       #that define the parameters for the
            ser.flush()                                                                 #serial communications  
            ser.flush()
            
    
    def open_shutter(self):
        #open the shutter (put the rts line on false)
        self.ser.rts = False 
        
    def close_shutter(self):   
        #close the shutter (put the rts line on true)   
        self.ser.rts = True
    
    def close(self):
        #close the serial communication
        self.ser.close()
    
    def change_shutter(self,state):
        #Impose the rts line in a certain state
        self.ser.rts = state
    
    def sequential_shutter(self):
        #open, wait 5s, and close the shutter
        self.open_shutter()
        time.sleep(5)
        self.close_shutter()
        time.sleep(5)
        
if __name__ == '__main__':
    shutter = ShutterDevice(port = 'COM5', debug=False)
    #the calling of ShutterDevice automatically open the communication
    try:    
        shutter.sequential_shutter()
        shutter.sequential_shutter()
            
    except Exception as err:
        print(err)
        
    finally:
        shutter.close()
        
   
    
    
    