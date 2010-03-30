import forge
from forge.models.groups import Group

class Delete(object):
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
		self.session.delete(group)	
		self.session.commit()
		return {'name':self.name, 'distribution':self.distribution}
