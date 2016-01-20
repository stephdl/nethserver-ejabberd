# Original work of Jean-Paul Leclère
Summary: NethServer ejabberd Jabber service
Name: nethserver-ejabberd
Version: 1.0.4
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: nethserver-devtools
Requires: ejabberd
Requires: nethserver-directory
Requires: nethserver-httpd

%description
NethServer implementation of ejabberd XMPP server

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist
mkdir -p %{buildroot}/%{_localstatedir}/log/ejabberd

%files -f %{name}-%{version}-%{release}-filelist 
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update
attr(0750,ejabberd,ejabberd) %dir %{_localstatedir}/log/ejabberd

%changelog
* Tue Jul 08 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.4-1.ns6
- DNS SRV record for XMPP protocol - Enhancement #2715
- Fix missing Italian translation - Bug #2706

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.3-1.ns6
- Move admin user in LDAP DB - Feature #2492 [NethServer]
- Lib: synchronize service status prop and chkconfig - Feature #2067 [NethServer]
- Update all inline help documentation - Task #1780 [NethServer]

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- Rebuild for automatic package handling. #1870
- Small fixes

* Tue Mar 19 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Add migration code

* Thu Jan 17 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First release
