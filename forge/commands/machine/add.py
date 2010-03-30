import forge
from forge.models.machines import Machine

class Add(object):
	def __init__(self,json_args,session):
                if type(json_args) != type({}):
                        raise TypeError("JSON Arg must be dict type")
                if 'ip' and 'profile' and 'arch' not in json_args.keys():
                        raise forge.ArgumentError()     
                self.ip = json_args['ip']
                self.profile = json_args['profile']
                self.arch = json_args['arch']
                self.session = session

	def call(self):
		machine = Machine(self.ip,self.profile,self.arch) 
                self.session.add(machine)
                self.session.commit()
                return {'ip':self.ip, 'profile':self.profile, 'arch':self.arch}
