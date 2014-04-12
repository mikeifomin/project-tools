class Conf(object):
	def __init__(self):
		try:
			self.conf_default = __import__('conf_default')
		except:
			self.conf_default = None
		try:
			self.conf = __import__('conf')
		except ImportError:
			self.conf = None
	def __getattr__(self, name):
		try:
			if hasattr(self.conf,name):
				return getattr(self.conf,name)
			else:
				return getattr(self.conf_default,name)
		except AttributeError:
			return None
conf = Conf()
