import forge
from forge.models.packages import Package
from forge.models.groups import Group

class Add(object):
	def __init__(self,json_args,session):
                if type(json_args) != type({}):
                        raise TypeError("JSON Arg must be dict type")
                if 'name' and 'group' and 'distro' not in json_args.keys():
                        raise forge.ArgumentError()     
                self.name = json_args['name']
                self.group = json_args['group']
                self.distro = json_args['distro']
                self.session = session

	def call(self):
		group = self.session.query(Group).filter(Group.name == self.group).first()
		if not group:
			raise LookupError("No Group: %s - %s"%self.group,self.distro)
		package = Package(self.name) 
		group.packages.append(package)
                self.session.add(package)
                self.session.commit()
                return {'name':self.name,'group':self.group,'distro':self.distro}
