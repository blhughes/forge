
import os,sys
import ConfigParser
import sqlalchemy
import os.path


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
