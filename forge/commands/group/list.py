import forge
from forge.models.groups import Group

class List(object):
	def __init__(self,json_args,session):
                if type(json_args) != type({}):
                        raise TypeError("JSON Arg must be dict type")
                if 'distribution' not in json_args.keys():
                        raise forge.ArgumentError()     
                self.distribution = json_args['distribution']
                self.session = session

	def call(self):
		groups = self.session.query(Group).filter(Group.distribution == self.distribution)
		if not groups:
			raise LookupError("No groups found in distribution: %s"%self.distribution)
		results = []
		for group in groups:
			 results.append({'name':group.name, 
				'distribution':group.distribution, 
				'machines':[{'ip':x.ip} for x in group.machines], 
				'packages':[{'name':x.name} for x in group.packages], 
				'overlays':[{'name':x.name} for x in group.overlays],
				})
		return results

