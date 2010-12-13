%define abiquo_basedir /opt/abiquo

Name:     abiquo-remote-repository-setup
Version:  1.6
Release:  1
Summary:  Abiquo Remote Repository setup metapkg
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  %{name}-%{version}.tar.gz
Source1:  README
Source2:  ovfindex.xml
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: httpd jdk

%description
Next Generation Cloud Management Solution

This package installs Abiquo Remote Repository.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/tools
mkdir -p $RPM_BUILD_ROOT/var/www/html
cp -r $RPM_BUILD_DIR/%{name}-%{version}/indexgenerator-0.1 $RPM_BUILD_ROOT/%{abiquo_basedir}/tools/ovfindex-gen
cp -r $RPM_BUILD_DIR/%{name}-%{version}/indexgenerator-0.1/ovfindex-gen $RPM_BUILD_ROOT/%{_bindir}/ovfindex-gen
cp %{SOURCE2} $RPM_BUILD_ROOT/var/www/html/

cp %{SOURCE1} $RPM_BUILD_ROOT/%{_docdir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig httpd on

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/README
%{abiquo_basedir}/tools/ovfindex-gen
%{_bindir}/ovfindex-gen
/var/www/html/ovfindex.xml

%changelog
* Fri Oct 22 2010 Sergio Rubio srubio@abiquo.com 1.6-1
- Initial Release
