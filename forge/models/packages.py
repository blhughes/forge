from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, relation, backref
import forge.models

metadata = forge.models.metadata
packages_table = Table('packages', metadata,
        Column('id',Integer, primary_key=True),
        Column('name', String),
	Column('group',Integer, ForeignKey('groups.id')),
)


class Package(object):
        def __init__(self,name):
                self.name = name
        
        def __repr__(self):
                return "<Package('%s')>" %(self.name)


mapper(Package, packages_table)


def init(engine):
        metadata.create_all(engine)


