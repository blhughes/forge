from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, relation, backref, clear_mappers
import forge.models
import forge.models.overlays
import forge.models.machines
import forge.models.packages

metadata = forge.models.metadata

groups_table = Table('groups', metadata,
        Column('id',Integer, primary_key=True),
        Column('name', String),
        Column('distribution', String),
)

machine_groups_table = Table('machine_groups', metadata,
	Column('group',Integer, ForeignKey('groups.id')),
	Column('machine',Integer, ForeignKey('machines.ip')),
)
	
package_groups_table = Table('package_groups', metadata,
	Column('group',Integer, ForeignKey('groups.id')),
	Column('package',Integer, ForeignKey('packages.id')),
)


class Group(object):
        def __init__(self,name,distribution):
                self.name = name
                self.distribution = distribution
        
        def __repr__(self):
                return "<Group('%s','%s')>" %(self.name, self.distribution)


mapper(Group, groups_table, properties={
	'overlays': relation(forge.models.overlays.Overlay, backref='groups', cascade="all, delete, delete-orphan"),
	'machines': relation(forge.models.machines.Machine, secondary=machine_groups_table, backref='groups', cascade="all, delete"),
	'packages': relation(forge.models.packages.Package, secondary=package_groups_table, backref='groups', cascade="all, delete"),
	
})


def init(engine):
        metadata.create_all(engine)
