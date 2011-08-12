
import forge
from forge.models.passwords import Password


class Set(object):
	def __init__(self,json_args,session):
		if type(json_args) != type({}):
			raise TypeError("JSON Arg must be dict type")
		if 'account' and 'hash' not in json_args.keys():
			raise forge.ArgumentError()	
		self.account = json_args['account']
		self.hash = json_args['hash']
		self.session = session

	def call(self):	
		password = self.session.query(Password).filter(Password.account == self.account).first()
                if not password:
			password = Password(self.account,self.hash)
		password.hash = self.hash
		self.session.add(password)
		self.session.commit()
		return {'account':password.account, 'hash':password.hash}
