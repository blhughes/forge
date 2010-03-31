import forge
from forge.models.machines import Machine

class Edit(object):
	def __init__(self,json_args,session):
                if type(json_args) != type({}):
                        raise TypeError("JSON Arg must be dict type")
                if 'ip' not in json_args.keys():
                        raise forge.ArgumentError()     
                self.ip = json_args['ip']
		self.profile = None
		self.arch = None
		if json_args.has_key("profile"):
			self.profile = json_args["profile"]
		if json_args.has_key("arch"):
			self.arch = json_args["arch"]
                self.session = session

	def call(self):
		machine = self.session.query(Machine).filter(Machine.ip == self.ip).first()
                if not machine:
                        raise LookupError("No machine: %s"%self.ip)
		if self.profile:
			machine.profile = self.profile
		if self.arch:
			machine.arch = self.arch

                self.session.commit()
                return {'ip':machine.ip, 'profile':machine.profile, 'arch':machine.arch}

