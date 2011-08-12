import forge
from forge.models.overlays import Overlay
from forge.models.groups import Group

class List(object):
	def __init__(self,json_args,session):
                if type(json_args) != type({}):
                        raise TypeError("JSON Arg must be dict type")
                if 'group' and 'distro' not in json_args.keys():
                        raise forge.ArgumentError()     
                self.group = json_args['group']
                self.distro = json_args['distro']
                self.session = session

	def call(self):
		group = self.session.query(Group).filter(Group.name == self.group).first()
		if not group:
			raise LookupError("No Group: %s - %s"%self.group,self.distro)
		results = []
		overlays= group.overlays
		for overlay in overlays:
			results.append({'name':overlay.name,'priority':overlay.priority,'group':self.group,'distro':self.distro})
		results.sort(key=lambda olay: olay['priority'],reverse=True)
		return results
