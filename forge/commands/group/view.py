import forge
from forge.models.groups import Group

class View(object):
	def __init__(self,json_args,session):
                if type(json_args) != type({}):
                        raise TypeError("JSON Arg must be dict type")
                if 'name' and 'distribution' not in json_args.keys():
                        raise forge.ArgumentError()     
                self.name = json_args['name']
                self.distribution = json_args['distribution']
                self.session = session

	def call(self):
		group = self.session.query(Group).filter(Group.name == self.name).filter(Group.distribution == self.distribution).first()
		if not group:
			raise LookupError("No group: %s"%self.name)
		return {'name':group.name, 
			'distribution':group.distribution, 
			'machines':[{'ip':x.ip} for x in group.machines], 
			'packages':[{'name':x.name} for x in group.packages], 
			'overlays':[{'name':x.name} for x in group.overlays],
			}

