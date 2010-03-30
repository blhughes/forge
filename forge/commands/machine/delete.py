import forge
from forge.models.machines import Machine

class Delete(object):
	def __init__(self,json_args,session):
                if type(json_args) != type({}):
                        raise TypeError("JSON Arg must be dict type")
                if 'ip'  not in json_args.keys():
                        raise forge.ArgumentError()     
                self.ip = json_args['ip']
                self.session = session

	def call(self):
		machine = self.session.query(Machine).filter(Machine.ip == self.ip).first()
                if not machine:
                        raise LookupError("No machine: %s"%self.ip)
                self.session.delete(machine)      
                self.session.commit()
                return {'ip':self.ip}

