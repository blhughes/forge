
import os,sys
import os.path
import json
import ConfigParser
import sqlalchemy
import traceback

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
	def __init__(self,command):
		self.command = command
	def __str__(self):
		return repr(self.command)
	def message(self):
		return "Command %s is invalid" % self.command
	def backtrace(self):
		exc_type, exc_value, exc_traceback = sys.exc_info()
		tb =  " ".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
		return " ".join(tb.split("\n"))
class Commands:
	def find(self,command,subcommand):
		if not command:
			raise CommandNotFound(command)
		if command not in dir(forge.commands):
			raise CommandNotFound(command)


def invoke(command,subcommand,json):
	Commands().find(command,subcommand)

