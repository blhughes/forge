
import forge
from forge.models.passwords import Password


class Get(object):
	def __init__(self,json_args,session):
		if type(json_args) != type({}):
			raise TypeError("JSON Arg must be dict type")
		if 'account' not in json_args.keys():
			raise forge.ArgumentError()	
		self.account = json_args['account']
		self.session = session

	def call(self):	
		password = self.session.query(Password).filter(Password.account == self.account).first()
		if not password:
			raise LookupError("No account: %s"%self.account)
		return {'account':password.account, 'hash':password.hash}
