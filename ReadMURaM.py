'''
Kai Yang
Institute for Astronomy, University of Hawaii at Manoa
Maui, HI
yangkai@hawaii.edu
'''
import os
import numpy as np

class readmuram_3d():
    def __init__ (self,Path=None,NumIn=None,Dim=None):
        if Dim is None:
            self.Dim = [1536,1536,128]
        else:
            self.Dim = Dim
            
#         set the 3D var file name.
        if Path is not None:
            self.rhof=os.path.join(Path,"subdomain_0."+NumIn)
            self.vxf=os.path.join(Path,"subdomain_1."+NumIn)
            self.vyf=os.path.join(Path,"subdomain_2."+NumIn)
            self.vzf=os.path.join(Path,"subdomain_3."+NumIn)
            self.eintf=os.path.join(Path,"subdomain_4."+NumIn)
            self.bxf=os.path.join(Path,"subdomain_5."+NumIn)
            self.byf=os.path.join(Path,"subdomain_6."+NumIn)
            self.bzf=os.path.join(Path,"subdomain_7."+NumIn)
            self.temf=os.path.join(Path,"subdomain_8."+NumIn)
            self.pref=os.path.join(Path,"subdomain_9."+NumIn)
            self.nef=os.path.join(Path,"subdomain_10."+NumIn)
            self.tauf=os.path.join(Path,"subdomain_11."+NumIn)
    def load_subfield(self,FileIn):
# Load a subfield from the SPIN4D project: subdomain_Y.XXXXXX.dat
# INPUT
# -----
# :mfile: extracted subfield from the SPIN4D project containing a single simulation variable.  Array shape is [128,1536,1536].  First for numbers are number of fields, ylen, zlen, and time.    
# OUTPUT
# ------
# :dat: loaded data aray
        tmp = np.fromfile(FileIn,dtype=np.float32).reshape(self.Dim)
        tmp = tmp.transpose(2,0,1)
        return(tmp)  
    def read_rho(self):
        return self.load_subfield(self.rhof)
    def read_vx(self):
        return self.load_subfield(self.vxf)
    def read_vy(self):
        return self.load_subfield(self.vyf)
    def read_vz(self):
        return self.load_subfield(self.vzf)
    def read_eint(self):
        return self.load_subfield(self.eintf)
    def read_bx(self):
        return self.load_subfield(self.bxf)
    def read_by(self):
        return self.load_subfield(self.byf)
    def read_bz(self):
        return self.load_subfield(self.bzf)
    def read_pressure(self):
        return self.load_subfield(self.pref)
    def read_temperature(self):
        return self.load_subfield(self.temf)
    def read_ne(self):
        return self.load_subfield(self.nef)
    def read_tau(self):
        return self.load_subfield(self.tauf)
        
class readmuram_2d():
    def __init__ (self,Path=None,NumIn=None):
#         set the 2D var file name.
        if Path is not None:
            self.rhof=os.path.join(Path,"subdomain_0."+NumIn)
            self.vxf=os.path.join(Path,"subdomain_1."+NumIn)
            self.vyf=os.path.join(Path,"subdomain_2."+NumIn)
            self.vzf=os.path.join(Path,"subdomain_3."+NumIn)
            self.eintf=os.path.join(Path,"subdomain_4."+NumIn)
            self.bxf=os.path.join(Path,"subdomain_5."+NumIn)
            self.byf=os.path.join(Path,"subdomain_6."+NumIn)
            self.bzf=os.path.join(Path,"subdomain_7."+NumIn)
            self.temf=os.path.join(Path,"subdomain_8."+NumIn)
            self.pref=os.path.join(Path,"subdomain_9."+NumIn)
            self.nef=os.path.join(Path,"subdomain_10."+NumIn)
            self.tauf=os.path.join(Path,"subdomain_11."+NumIn)
def load_muram_2dslice(mfile):
# Load one of the yz or xy-slice files from the 2D/ directory
# INPUT
# -----
# :mfile: Emergent intensity for the SPIN4D project.  Array shape is [1536,1536]. 
# OUTPUT
# ------
# :dat: loaded data aray

    dat = np.fromfile(mfile,dtype=np.float32)
    n1 = int(dat[0])
    n2 = int(dat[1])
    n3 = int(dat[2])
    return(np.squeeze(dat[4:].reshape((n1,n3,n2))))

def load_muram_general(mfile):
# Load a subfield from the SPIN4D project
# INPUT
# -----
# :mfile: Emergent intensity for the SPIN4D project.  Array shape is [1536,1536].
# OUTPUT
# ------
# :dat: loaded data aray

    dat = np.fromfile(mfile,dtype=np.float32)
          
    n1 = int(dat[0])
    nz = ny = 1536
    return(np.squeeze(dat[4:].reshape((n1,ny,nz))))

def load_muram_intensityslice(mfile):
# Load a 2D intensity file from the SPIN4D project (I_out.XXXXXX)
# INPUT
# -----
# :mfile: Emergent intensity for the SPIN4D project.  Array shape is [1536,1536].
# OUTPUT
# ------
# :dat: loaded data aray

    nz = ny = 1536
    return(np.fromfile(mfile,dtype=np.float32)[4:].reshape((nz,ny)))

