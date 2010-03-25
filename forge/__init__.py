
import os,sys
import os.path
import ConfigParser
import sqlalchemy
import imp

#Get forge configuration
config = ConfigParser.ConfigParser()
config.read(['/etc/forge.conf',os.path.expanduser('~/.forge.conf')])

sys.path.append(os.path.abspath(os.path.join("..",os.path.dirname(__file__))))


import forge
import forge.util
import forge.commands
import forge.commands.packages
import forge.commands.config
import forge.commands.password
import forge.commands.kerberos



class CommandNotFound(Exception):
	def __init__(self,command,subcommand):
		self.args=(command,subcommand)
		self.command = command
		self.subcommand = subcommand
	def __str__(self):
		return self.__unicode__()
	def __unicode__(self):
		return "Command not found: %s:%s" % (self.command, self.subcommand)
class Commands:
	def find(self,command,subcommand):
		if not (command and subcommand):
			raise CommandNotFound(command,subcommand)
		if command not in dir(forge.commands):
			raise CommandNotFound(command,subcommand)
		module = eval("forge.commands.%s"%command)
		if '__package__' not in dir(module):
			raise CommandNotFound(command,subcommand)
		try:
			(file, pathname, description)=imp.find_module(subcommand,module.__path__)	
			module=imp.load_module(subcommand,file,pathname,description)
		except:
			raise CommandNotFound(command,subcommand)
	
		if subcommand.capitalize() not in dir(module):
			raise CommandNotFound(command,subcommand)
		classobj = module.__dict__[subcommand.capitalize()]
		if "call" not in dir(classobj):
			raise CommandNotFound(command,subcommand)

		return classobj	

def invoke(command,subcommand,json_args):
	cmd=Commands().find(command,subcommand)
	
	return cmd(json_args).call()
