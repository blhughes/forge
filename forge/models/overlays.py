from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, relation, backref
import forge.models

metadata = forge.models.metadata
overlays_table = Table('overlays', metadata,
        Column('id',Integer, primary_key=True),
        Column('name', String),
        Column('priority', Integer),
	Column('group',Integer, ForeignKey('groups.id')),
)


class Overlay(object):
        def __init__(self,name,priority):
                self.name = name
		self.priority = priority
        
        def __repr__(self):
                return "<Overlay('%s','%d')>" %(self.name,self.priority)


mapper(Overlay, overlays_table)


def init(engine):
        metadata.create_all(engine)


