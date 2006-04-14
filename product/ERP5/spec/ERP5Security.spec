%define product ERP5Security
%define version 0.11
%define release 6

%define zope_home %{_prefix}/lib/zope
%define software_home %{zope_home}/lib/python

Summary:   A collection of plugins for Pluggable Auth Service to manage ERP5 security
Name:      zope-%{product}
Version:   %{version}
Release:   %mkrel %{release}
License:   GPL
Group:     System/Servers
URL:       http://www.erp5.org
Source0:   %{product}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-rootdir
BuildArch: noarch
Conflicts: ERP5Security
Requires:  erp5-zope zope-PluggableAuthService

#----------------------------------------------------------------------
%description
This zope product is a plugin to Pluggable Auth Service, to manage roles,
groups and users in ERP5. It also add fine security management features to
ERP5.

#----------------------------------------------------------------------
%prep
%setup -c

%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
  service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
  service zope restart
fi

%files
%defattr(0644, zope, zope, 0755)
%doc %{product}/VERSION.txt
%{software_home}/Products/*

#----------------------------------------------------------------------
%changelog
* Tue Apr 04 2006 Kevin Deldycke <kevin@nexedi.com> 0.11-6mdk
- New build from the SVN repository

* Wed Feb 01 2006 Kevin Deldycke <kevin@nexedi.com> 0.11-5mdk
- Give ownership to zope
- New build from the CVS

* Wed Feb 01 2006 Kevin Deldycke <kevin@nexedi.com> 0.11-4mdk
- Give ownership to zope
- New build from the CVS

* Mon Jan 30 2006 Kevin Deldycke <kevin@nexedi.com> 0.11-3mdk
- New build from the CVS

* Fri Jan 27 2006 Kevin Deldycke <kevin@nexedi.com> 0.11-2mdk
- New build from the CVS

* Thu Jan 26 2006 Kevin Deldycke <kevin@nexedi.com> 0.11-1mdk
- Update to version 0.11

* Wed Jan 18 2006 Kevin Deldycke <kevin@nexedi.com> 0.10-1mdk
- Update to version 0.10

* Mon Jan 16 2006 Kevin Deldycke <kevin@nexedi.com> 0.1.20060116-1mdk
- New build from the CVS

* Tue Jan 10 2006 Kevin Deldycke <kevin@nexedi.com> 0.1.20060110-1mdk
- Initial release
