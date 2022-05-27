class sir_param_1d():
	def __init__(self):
		datas={"Number of cycles          (*)":["0","(0=synthesis)"],
			"Observed profiles         (*)":["syn_0_0.per","magnetico.per"],
			"Stray light file             ":[" ","(none=no stray light contam)"],
			"PSF file                     ":[" ","(none=no convolution with PSF)"],
			"Wavelength grid file      (s)":["malla_inv_1.grid","(none=automatic selection)"],
			"Atomic parameters file       ":["LINES1","(none=DEFAULT LINES file)"],
			"Abundances file              ":["ASPLUND","(none=DEFAULT ABUNDANCES file)"],
			"Initial guess model 1     (*)":["muram_0_0.mod","in.mod"],
			"Initial guess model 2        ":[" "," "],
			"Weight for Stokes I          ":["1","(DEFAULT=1; 0=not inverted)"],
			"Weight for Stokes Q          ":["1","(DEFAULT=1; 0=not inverted)"],
			"Weight for Stokes U          ":["1","(DEFAULT=1; 0=not inverted)"],
			"Weight for Stokes V          ":["1","(DEFAULT=1; 0=not inverted)"],
			"AUTOMATIC SELECT. OF NODES?  ":[" ","(DEFAULT=0=no; 1=yes)"],
			"Nodes for temperature 1      ":[" "," "],
			"Nodes for electr. press. 1   ":[" "," "],
			"Nodes for microturb. 1       ":[" "," "],
			"Nodes for magnetic field 1   ":[" "," "],
			"Nodes for LOS velocity 1     ":[" "," "],
			"Nodes for gamma 1            ":[" "," "],
			"Nodes for phi 1              ":[" "," "],
			"Invert macroturbulence 1?    ":[" ","(0 or blank=no, 1=yes)"],
			"Nodes for temperature 2      ":[" "," "],
			"Nodes for electr. press. 2   ":[" "," "],
			"Nodes for microturb. 2       ":[" "," "],
			"Nodes for magnetic field 2   ":[" "," "],
			"Nodes for LOS velocity 2     ":[" "," "],
			"Nodes for gamma 2            ":[" "," "],
			"Nodes for phi 2              ":[" "," "],
			"Invert macroturbulence 2?    ":[" ","(0 or blank=no, 1=yes)"],
			"Invert filling factor?       ":[" ","(0 or blank=no, 1=yes)"],
			"Invert stray light factor?   ":[" ","(0 or blank=no, 1=yes)"],
			"mu=cos (theta)               ":[" ","(DEFAULT: mu=1. mu<0 => West)"],
			"Estimated S/N for I          ":["1000","(DEFAULT: 1000)"],
			"Continuum contrast           ":[" ","(DEFAULT: not used)"],
			"Tolerance for SVD            ":["1.e-8","(DEFAULT value: 1e-4)"],
			"Initial diagonal element     ":[" ","(DEFAULT value: 1.e-3)"],
			"Splines/Linear Interpolation ":[" ","(0 or blank=splines, 1=linear)"],
			"Gas pressure at surface 1    ":[" ","(0 or blank=Pe boundary cond."],
			"Gas pressure at surface 2    ":[" ","(0 or blank=Pe boundary cond."],
			"Magnetic pressure term?      ":[" ","(0 or blank=no, 1=yes"],
			"NLTE Departures filename     ":[" ","blanck= LTE (Ej. depart_6494.dat"]}
		self.param=datas
	def save_trol(self,savename):
		with open(savename, 'w') as file:
			for key,value in self.param.items():
				file.write('{}:{}!{}\n'.format(key,value[0],value[1]))
			file.close()
