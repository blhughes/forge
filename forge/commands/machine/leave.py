import forge
from forge.models.machines import Machine
from forge.models.groups import Group

class Leave(object):
	def __init__(self,json_args,session):
                if type(json_args) != type({}):
                        raise TypeError("JSON Arg must be dict type")
                if 'ip' and 'group' and 'distribution' not in json_args.keys():
                        raise forge.ArgumentError()     
                self.ip = json_args['ip']
                self.group = json_args['group']
                self.distribution = json_args['distribution']
                self.session = session

	def call(self):
		machine = self.session.query(Machine).filter(Machine.ip == self.ip).first()
                if not machine:
                        raise LookupError("No machine: %s"%self.ip)
		group = self.session.query(Group).filter(Group.name == self.group).filter(Group.distribution == self.distribution).first()
                if not group:
                        raise LookupError("No group: %s"%self.group)
		if not group in machine.groups:
			raise LookupError("Machine not in group: %s"%self.group)

		group.machines.remove(machine)
                self.session.commit()
                return {'ip':self.ip}

