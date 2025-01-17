%define		oname s3cmd

Name:		python-%{oname}
Version:	1.0.1
Release:	2
Summary:	Command line tool for managing Amazon S3 and CloudFront services
Group:		Networking/File transfer
License:	GPLv2
URL:		https://s3tools.org/s3cmd
Source:		http://prdownloads.sourceforge.net/s3tools/s3cmd-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-devel
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
%{__python} setup.py install --root=%{buildroot} --prefix=%{_prefix}
rm -fr %{buildroot}%{_prefix}/lib*/python*/site-packages/*.egg-info

%files
%{_bindir}/*
%{python_sitelib}/S3
%doc README PKG-INFO NEWS



%changelog
* Thu Feb 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.1-1
+ Revision: 770737
- version update 1.0.1

* Mon Dec 21 2009 Sander Lepik <sander85@mandriva.org> 0.9.9.91-1mdv2011.0
+ Revision: 480868
- BuildRequires: python -> BuildRequires: libpython-devel
- import python-s3cmd

