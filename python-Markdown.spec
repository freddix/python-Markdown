%define		module Markdown

Summary:	Python implementation of Markdown
Name:		python-%{module}
Version:	2.3.1
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/M/Markdown/%{module}-%{version}.tar.gz
# Source0-md5:	82f6828ec2292dda52fc38b743776bc6
URL:		http://packages.python.org/Markdown/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python implementation of John Gruber's Markdown.
It is almost completely compliant with the reference implementation,
though there are a few known issues. See Features for information on
what exactly is supported and what is not. Additional features are
supported by the Available Extensions.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%attr(755,root,root) %{_bindir}/markdown_py
%{py_sitescriptdir}/markdown
%{py_sitescriptdir}/*.egg-info

