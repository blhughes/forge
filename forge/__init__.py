
import os,sys
import os.path
import ConfigParser
import sqlalchemy
from sqlite3 import dbapi2 as sqlite
import imp

import forge
import forge.util
import forge.commands
import forge.commands.machine
import forge.commands.package
import forge.commands.overlay
import forge.commands.password
import forge.commands.group
import forge.commands.kerberos

import forge.models
import forge.models.passwords
import forge.models.groups
import forge.models.packages
import forge.models.overlays


#Get forge configuration
config = ConfigParser.ConfigParser()
config.read(['/etc/forge.conf',os.path.expanduser('~/.forge.conf')])
dsn = config.get("database","dsn")

#Setup Database Connection
engine=sqlalchemy.create_engine(dsn,module=sqlite)
forge.models.passwords.init(engine)
forge.models.groups.init(engine)
forge.models.packages.init(engine)
forge.models.overlays.init(engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

sys.path.append(os.path.abspath(os.path.join("..",os.path.dirname(__file__))))

class CommandNotFound(Exception):
	def __init__(self,command,subcommand):
		self.args=(command,subcommand)
		self.command = command
		self.subcommand = subcommand
	def __str__(self):
		return self.__unicode__()
	def __unicode__(self):
		return "Command not found: %s:%s" % (self.command, self.subcommand)


class ArgumentError(Exception):
	def __str__(self):
		return self.__unicode__()
	def __unicode__(self):	
		return "JSON object required as final argument"

class Commands(object):
	def find(self,command,subcommand):
		"""Search through packages and modules in commands trying to match the command subcommand pair. command should be a subpackage
		of forge.commands, subcommand should be a module in the command package.
		There should be a class of Capitalized subcommand in the subcommanand module.
		The Subcommand class should have a method "call". 
		If any of these tests fail then CommandNotFound is raised.
		"""
		if not (command and subcommand):
			raise CommandNotFound(command,subcommand)
		if command not in forge.commands.__dict__.keys():
			raise CommandNotFound(command,subcommand)
		module = eval("forge.commands.%s"%command)
		if '__package__' not in module.__dict__.keys():
			raise CommandNotFound(command,subcommand)
		try:
			(file, pathname, description)=imp.find_module(subcommand,module.__path__)	
			module=imp.load_module(subcommand,file,pathname,description)
		except:
			raise CommandNotFound(command,subcommand)
		if subcommand.capitalize() not in module.__dict__.keys():
			raise CommandNotFound(command,subcommand)
		classobj = module.__dict__[subcommand.capitalize()]
		if "call" not in classobj.__dict__.keys():
			raise CommandNotFound(command,subcommand)
		return classobj

def invoke(command,subcommand,json_args):
	cmd=Commands().find(command.lower(),subcommand.lower())
	return cmd(json_args,session).call()
