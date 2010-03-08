#!/usr/bin/python

from distutils.core import setup
#from setuptools import setup,find_packages

NAME = "forge"
VERSION = open("version", "r+").read().split()[0]
SHORT_DESC = "%s: Fedora Workstation Management" % NAME
LONG_DESC = """
%s: A secure Fedora workstation management system.
""" % NAME


if __name__ == "__main__":
 
        manpath    = "share/man/man8/"
        etcpath    = "/etc/" 
        etcmodpath = "/etc/%s/modules" % NAME
        initpath   = "/etc/init.d/"
        logpath    = "/var/log/%s/" % NAME
        pkipath    = "/etc/pki/%s" % NAME
        rotpath    = "/etc/logrotate.d"
	sbinpath   = "/usr/sbin"
	modpath    = "/usr/share/%s/modules" %NAME
	cronpath   = "/etc/cron.d/"
        setup(
                name="%s" % NAME,
                version = VERSION,
                author = "Bryan Hughes",
                author_email = "khan@nmt.edu",
                url = "http://infohost.nmt.edu/tcc",
                license = "GPL",
		scripts = [
                     "forgec/forgec",
                ],
		# package_data = { '' : ['*.*'] },
                package_dir = {"%s" % NAME: "%s" % NAME
                },
		packages = ["%s" % NAME,
	        	    "%s/ssl" % NAME,
                ],
                data_files = [
                              (etcpath,  ['etc/forge.conf']),
                              (etcmodpath, []),
                              (manpath,  ['docs/forgec.8.gz']),
			      (rotpath,  ['etc/forge_rotate']),
                              (logpath,  []),
			      (etcpath,  []),
			      (pkipath,  []),
			      (sbinpath, ["forgec/forge-keytab", "forgec/forge-init","forgec/kscomplete"]),
			      (modpath, ["modules/yumtransaction","modules/passwd","modules/hardware", "modules/grub"]),		
			      (cronpath, ["etc/forge.cron"]),
                ],
                description = SHORT_DESC,
                long_description = LONG_DESC
        )

