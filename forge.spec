
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define is_suse %(test -e /etc/SuSE-release && echo 1 || echo 0)

Summary: Secure Fedora Workstation Management
Name: forge
Source1: version
Version: %(echo `awk '{ print $1 }' %{SOURCE1}`)
Release: %(echo `awk '{ print $2 }' %{SOURCE1}`)%{?dist}
Source0: %{name}-%{version}.tar.gz
License: GPLv2+
Group: Applications/System
Requires: python >= 2.4
Requires: pyOpenSSL
BuildRequires: python-devel
%if %is_suse
BuildRequires: gettext-devel
%else
%if 0%{?fedora} >= 8
BuildRequires: python-setuptools-devel
%else
BuildRequires: python-setuptools
%endif
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://infohost.nmt.edu/tcc/

%description

Forge is a secure Fedora workstation management system.

%prep
%setup -q

%build
%{__python} setup.py build

%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --prefix=/usr --root=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%if 0%{?fedora} > 8
%{python_sitelib}/forge*.egg-info
%endif
%{_bindir}/forgec
%{_sbindir}/forge-init
%{_sbindir}/forge-keytab
%{_sbindir}/kscomplete
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/pki/%{name}
%config(noreplace) /etc/forge.conf
%config(noreplace) /etc/logrotate.d/forge_rotate
%dir %{python_sitelib}/forge
%dir %{python_sitelib}/forge/ssl
%{python_sitelib}/forge/ssl/*.py*
%{python_sitelib}/forge/*.py*
%dir /var/log/forge
%doc AUTHORS README LICENSE
%{_mandir}/man8/forgec.8.gz
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
/etc/cron.d/forge.cron


%changelog
* Tue Sep 1  2009 Bryan Hughes <khan@nmt.edu> - 0.5-22
- Changed grub to chainload hd0,0 for linuxonly
* Thu Aug 13 2009 Bryan Hughes <khan@nmt.edu> - 0.5-21
- Removed unlocked menu
* Fri Jul 31 2009 Bryan Hughes <khan@nmt.edu> - 0.5-20
- Added kickstart complete
* Fri Jan 30 2009 Bryan Hughes <khan@nmt.edu> - 0.5-19
- Grub module fix for skipping no profiled comps
* Wed Jan 28 2009 Bryan Hughes <khan@nmt.edu> - 0.5-18
- Added dustin's lvm patch to hardware
* Mon Jan 05 2009 Bryan Hughes <khan@nmt.edu> - 0.5-17
- Only listing newest kernel in main grub menu
* Wed Dec 17 2008 Bryan Hughes <khan@nmt.edu> - 0.5-16
- Added dustin's multidisk patch to hardware
* Tue Dec 16 2008 Bryan Hughes <khan@nmt.edu> - 0.5-15
-Added iclicker to forge.hardware
* Mon Sep 29 2008 Bryan Hughes <khan@nmt.edu> - 0.5-13
-Fixed permission problem
* Thu Sep 25 2008 Bryan Hughes <khan@nmt.edu> - 0.5-12
-Added monitor to hardware devices list in hardware module
* Mon Sep 22 2008 Bryan Hughes <khan@nmt.edu> - 0.5-12
-Hardware oscheck multidisk support
* Wed Sep 17 2008 Bryan Hughes <khan@nmt.edu> - 0.5-11
-Added Dustin's grub integ patch
* Wed Sep 17 2008 Bryan Hughes <khan@nmt.edu> - 0.5-10
-New Support for Extra device attributes
-Reverse order of kernels in grub.conf
* Tue Sep 16 2008 Bryan Hughes <khan@nmt.edu> - 0.5-9
-New Support for bios version
* Tue Sep 16 2008 Bryan Hughes <khan@nmt.edu> - 0.5-8
-New hardware module
* Wed Aug 06 2008 Bryan Hughes <khan@nmt.edu> - 0.5-5
-Added Modules

* Wed Jun 25 2008 Bryan Hughes <khan@nmt.edu> - 0.5
- Initial Build
