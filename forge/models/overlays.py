from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, relation, backref
import forge.models

metadata = forge.models.metadata
overlays_table = Table('overlays', metadata,
        Column('id',Integer, primary_key=True),
        Column('name', String),
        Column('order', Integer),
	Column('group',Integer, ForeignKey('groups.id')),
)


class Overlay(object):
        def __init__(self,name,order):
                self.name = name
		self.order = order
        
        def __repr__(self):
                return "<Password('%s','%d')>" %(self.name,self.order)


mapper(Overlay, overlays_table)


def init(engine):
        metadata.create_all(engine)


