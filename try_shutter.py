"""
Code written by Michele Castriotta and Andrea Bassi for controlling the Polimi shutter,
sending HIGH and LOW signal to the RTS line of the USB port. The shutter is implemented 
for working in ScopeFoundry (http://www.scopefoundry.org/).

11-10-2018, Milan

This script setup the ScopeFoundry applications, and try the shutter. 
Run it if you want to try the shutter, otherwise is useless.
"""

from ScopeFoundry import BaseMicroscopeApp

class TryShutter(BaseMicroscopeApp):

    # this is the name of the microscope that ScopeFoundry uses 
    # when storing data
    name = 'try_shutter'
    
    # You must define a setup function that adds all the 
    #capablities of the microscope and sets default settings
    def setup(self):
        
        #Add App wide settings
        
        #Add hardware components
        from shutter_hw import ShutterHW
        self.add_hardware(ShutterHW(self))
               
        #Add Hardware components
        from ScopeFoundryHW.virtual_function_gen.vfunc_gen_hw import VirtualFunctionGenHW
        self.add_hardware(VirtualFunctionGenHW(self))

        #Add Measurement components
        from ScopeFoundryHW.virtual_function_gen.sine_wave_measure import SineWavePlotMeasure
        self.add_measurement(SineWavePlotMeasure(self))
                        
        print("Create Measurement objects")
        
        # Connect to custom gui
        # load side panel UI
        # show ui
        self.ui.show()
        self.ui.activateWindow()


if __name__ == '__main__':
    
    import sys
    app = TryShutter(sys.argv)
    sys.exit(app.exec_())