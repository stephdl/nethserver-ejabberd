# Original work of Jean-Paul Leclère
Summary: NethServer ejabberd Jabber service
Name: nethserver-ejabberd
Version: 1.0.4
Release: 1
License: GPL
Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: nethserver-devtools >= 1.0.0
Requires: ejabberd >= 2.0.1
Requires: nethserver-directory >= 1.1.1-5
Requires: nethserver-httpd >= 1.0.1-2
AutoReq: no


%description
NethServer implementation of ejabberd XMPP server


%preun

%post

%prep
%setup

%build
%{makedocs}
perl createlinks
mkdir -p root/var/log/ejabberd.run
mkdir -p root/var/log/ejabberd


%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir '/var/log/ejabberd' 'attr(0750,ejabberd,ejabberd)' \
     > %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}-%{version}-%{release}-filelist 
%defattr(-,root,root)

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
