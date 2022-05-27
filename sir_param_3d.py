from configobj import ConfigObj
class sir_param_3d():
	def __init__(self):
		self.config=ConfigObj({'general': {'stokes output': 'filename.h5', 'interpolated model output': 'None', 'eos': 'SIR','clip_tau':'True','clip_tau_max':'2','clip_tau_min':'-5'}, 'spectral regions': {'region 1': {'name': '6301-6302', 'wavelength range': ['6300.8521', '6303.3119'], 'n. wavelengths': '276', 'spectral lines': ['200', '201']}}, 'atmosphere': {'type': 'MURAM', 'xyz': ['1', '0', '2'], 'dimensions': ['1536', '1536', '128'], 'deltaz': '12e5', 'maximum tau': '2.0', 'density': 'subdomain_0', 'vx': 'subdomain_2', 'vy': 'subdomain_3', 'vz': 'subdomain_1', 'eint': 'subdomain_4', 'bx': 'subdomain_6', 'by': 'subdomain_7', 'bz': 'subdomain_5', 'temperature': 'subdomain_8', 'pressure': 'subdomain_9', 'ne': 'subdomain_10', 'tau500': 'subdomain_11', 'multipliers': {'bx': '3.5449077018110318', 'by': '3.5449077018110318', 'bz': '3.5449077018110318', 'vz': '-1.0'}}})

	def write(self,filename=None):
		if filename==None:
			print('filename is needed for write a config file')
		self.config.filename=filename
		self.config.write()
