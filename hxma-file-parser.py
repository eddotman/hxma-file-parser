from numpy import *

class Parser:

	def __init__(self, f = None):
		try:
			self.f_raw = f
		except:
			print "Failed to load file: check filename."
		self.f_fmt = None
		print "HXMA file parser created."

	def parse_file(self):
		if not self.f_raw == None:
			try:
				self.f_fmt = loadtxt(self.f_raw, delimiter=",")
				print "File loaded."
			except:
				print "Failed to parse file: check formatting."
		else:
			print "No file loaded."

	def save_file(self, path):
		if not self.f_fmt == None:
			try:
				savetxt(path, self.f_fmt)
				print "File parsed."
			except:
				print "Failed to save file: check write permissions."
		else:
			print "No file parsed."

if __name__ == "__main__":
	p1 = Parser(f = "INPUT_FILE_NAME_HERE")
	p1.parse_file()
	p1.save_file("OUTPUT_FILE_NAME_HERE")


