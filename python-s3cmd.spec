%define		version 0.9.9.91
%define		rel 1
%define		release %mkrel %rel
%define		oname s3cmd

Name:		python-%{oname}
Version:	%{version}
Release:	%{release}
Summary:	Command line tool for managing Amazon S3 and CloudFront services

Group:		Networking/File transfer
License:	GPLv2
URL:		http://s3tools.org/s3cmd
Source:		http://prdownloads.sourceforge.net/s3tools/s3cmd-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildArch:	noarch

BuildRequires:	python
Requires:	python

%description
S3cmd lets you copy files from/to Amazon S3
(Simple Storage Service) using a simple to use
command line client. Supports rsync-like backup,
GPG encryption, and more. Also supports management
of Amazon's CloudFront content delivery network.

%prep
%setup -q -n %{oname}-%{version}

%build
export S3CMD_PACKAGING=1
%{__python} setup.py build

%install
export S3CMD_PACKAGING=1
%{__python} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix}
rm -fr %{buildroot}%{_prefix}/lib*/python*/site-packages/*.egg-info

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{python_sitelib}/S3
%doc README PKG-INFO NEWS

