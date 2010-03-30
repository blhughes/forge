from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, relation, backref
import forge.models

metadata = forge.models.metadata
machines_table = Table('machines', metadata,
        Column('ip',String, primary_key=True),
        Column('profile', String),
        Column('arch', String),
	Column('group',Integer, ForeignKey('groups.id')),
)


class Machine(object):
        def __init__(self,ip,profile,arch):
                self.ip = ip
		self.profile = profile
		self.arch = arch
        
        def __repr__(self):
                return "<Machine('%s','%s','%s')>" %(self.name,self.profile,self.arch)


mapper(Machine, machines_table)


def init(engine):
        metadata.create_all(engine)


