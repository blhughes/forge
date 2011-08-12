import forge
from forge.models.overlays import Overlay
from forge.models.groups import Group

class Add(object):
	def __init__(self,json_args,session):
                if type(json_args) != type({}):
                        raise TypeError("JSON Arg must be dict type")
                if 'name' and 'priority' and 'group' and 'distro' not in json_args.keys():
                        raise forge.ArgumentError()     
                self.name = json_args['name']
                self.priority = json_args['priority']
                self.group = json_args['group']
                self.distro = json_args['distro']
                self.session = session

	def call(self):
		group = self.session.query(Group).filter(Group.name == self.group).first()
		if not group:
			raise LookupError("No Group: %s - %s"%self.group,self.distro)
		overlay = Overlay(self.name,self.priority)
		group.overlays.append(overlay)
                self.session.add(overlay)
                self.session.commit()
                return {'name':self.name,'priority':self.priority,'group':self.group,'distro':self.distro}
