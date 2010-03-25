

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper

metadata = MetaData()

passwords_table = Table('passwords', metadata,
	Column('account', String,primary_key=True),
	Column('hash', String),
)


class Password(object):
	def __init__(self,account,hash):
		self.account = account
		self.hash = hash
	
	def __repr__(self):
		return "<Password('%s','%s')>" %(self.account, self.hash)


mapper(Password, passwords_table)


def init(engine):
	metadata.create_all(engine) 
