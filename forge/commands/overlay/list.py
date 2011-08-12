import forge
from forge.models.overlays import Overlay
from forge.models.groups import Group

class List(object):
	def __init__(self,json_args,session):
                if type(json_args) != type({}):
                        raise TypeError("JSON Arg must be dict type")
                if 'group' not in json_args:
                        raise forge.ArgumentError()

                self.group = json_args['group']

		if 'distro' in json_args:
			self.distro = json_args['distro']
		else:
			self.distro = None

                self.session = session

	def call(self):
		groups = self.session.query(Group).filter(Group.name == self.group)
		if not groups:
			raise LookupError("No Group: %s - %s"%self.group,self.distro)
		results = []
		for group in groups:
			overlays= group.overlays
			for overlay in overlays:
				results.append({'name':overlay.name,'priority':overlay.priority,'group':overlay.groups.name,'distro':overlay.groups.distribution})

		results.sort(key=lambda olay: olay['priority'],reverse=True)
		return results
