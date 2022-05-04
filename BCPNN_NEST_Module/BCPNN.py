import nest
import os
def InstallBCPNN(on_milner = False, on_beskow=False):
    '''
    This function installs the BCPNN Synapse by Phil Tully.
    The optional parameter passed, indicate whether this is on Supercomputer Milner (True) or Beskow
    or my local machine (False)
    '''
    if ('milner' in os.getcwd()):
        on_milner=True
    if ('klemming' in os.getcwd()):
        on_beskow=True
    if (not 'bcpnn_synapse' in nest.Models('synapses')):
        if on_beskow:
            nest.sr('(/cfs/klemming/nobackup/usr/Beskow_BCPNN/share/nest/sli) addpath')  # usr-> u/usr
            nest.Install('/cfs/klemming/nobackup/usr/Beskow_BCPNN/lib/nest/pt_module')   # usr-> u/usr
        elif on_milner:
	        nest.sr('(/cfs/milner/scratch/usr/Beskow_BCPNNMilner_BCPNN/share/nest/sli) addpath')   # usr-> u/usr
	        nest.Install('/cfs/milner/scratch/usr/Beskow_BCPNNMilner_BCPNN/lib/nest/pt_module')    # usr-> u/usr
        else:
	        try:
	            nest.Install('pt_module')
	        except:
	            nest.Install('pt_module')
