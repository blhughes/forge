VERSION		= $(shell echo `awk '{ print $$1 }' version`)
RELEASE		= $(shell echo `awk '{ print $$2 }' version`)
NEWRELEASE	= $(shell echo $$(($(RELEASE) + 1)))

MESSAGESPOT=po/messages.pot

TOPDIR = $(shell pwd)
DIRS	= forge docs forgec
PYDIRS	= forge forgec
all: rpms


bumprelease:	
	-echo "$(VERSION) $(NEWRELEASE)" > version

setversion: 
	-echo "$(VERSION) $(RELEASE)" > version

build: clean
	python setup.py build -f

clean:
	-rm -f  MANIFEST
	-rm -rf dist/ build/
	-rm -rf *~
	-rm -rf rpm-build/
#	-rm -rf docs/*.gz
#	-for d in $(DIRS); do ($(MAKE) -C $$d clean ); done

clean_hard:
	-rm -rf $(shell python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")/func 

clean_harder:
	-rm -rf /etc/pki/func
	-rm -rf /etc/func
	-rm -rf /var/lib/func

clean_hardest: clean_rpms


install: build manpage
	python setup.py install -f

install_hard: clean_hard install

install_harder: clean_harder install

install_hardest: clean_harder clean_rpms rpms install_rpm restart

install_rpm:
	-rpm -Uvh rpm-build/func-$(VERSION)-$(RELEASE)$(shell rpm -E "%{?dist}").noarch.rpm

clean_rpms:
	-rpm -e func

sdist: 
	python setup.py sdist

new-rpms: bumprelease rpms

pychecker:
	-for d in $(PYDIRS); do ($(MAKE) -C $$d pychecker ); done   
pyflakes:
	-for d in $(PYDIRS); do ($(MAKE) -C $$d pyflakes ); done	

money: clean
	-sloccount --addlang "makefile" $(TOPDIR) $(PYDIRS) $(EXAMPLEDIR) $(INITDIR) 

testit: clean
	-cd test; sh test-it.sh

unittest:
	-nosetests -v -w test/unittest

rpms: build sdist
	mkdir -p rpm-build
	cp dist/*.gz rpm-build/
	cp version rpm-build/
	rpmbuild --define "_topdir %(pwd)/rpm-build" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %{_topdir}" \
	--define "_srcrpmdir %{_topdir}" \
	--define '_rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm' \
	--define "_specdir %{_topdir}" \
	--define "_sourcedir  %{_topdir}" \
	-ba forge.spec
