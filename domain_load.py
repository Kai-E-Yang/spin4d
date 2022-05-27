'''
Kai Yang
Institute for Astronomy, University of Hawaii at Manoa
Maui, HI
yangkai@hawaii.edu
'''
import os
import numpy as np

class load_3d():
    def __init__ (self,file=None):
        if Dim is None:
            self.Dim = [128,1536,1536]
        else:
            self.Dim = Dim
        if file is not None:
            self.filename=file
        else:
    def load_subfield(FileIn):
# Load a subfield from the SPIN4D project: subdomain_Y.XXXXXX.dat
# INPUT
# -----
# :mfile: extracted subfield from the SPIN4D project containing a single simulation variable.  Array shape is [128,1536,1536].  First for numbers are number of fields, ylen, zlen, and time.    
# OUTPUT
# ------
# :dat: loaded data aray
        tmp = np.fromfile(mfile,dtype=np.float32).reshape(self.Dim)
        tmp = tmp.transpose(2,0,1)
        return(tmp)  
        