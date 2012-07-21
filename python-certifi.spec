%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%global pkgname certifi


Name:           python-certifi
Version:        0.0.8
Release:        3%{?dist}
Summary:        Mozilla's SSL Certs

License:        ISC and GPLv2 and MPLv1.1 and LGPLv2+
URL:            http://pypi.python.org/pypi/%{pkgname}
Source0:        http://pypi.python.org/packages/source/c/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel

%description
This package contains Mozilla's CA bundle for SSL.


%prep
%setup -q -n %{pkgname}-%{version}
sed -i 's|#!/usr/bin/env python||' certifi/core.py

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc README.rst LICENSE
%{python_sitelib}/*


%changelog
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 03 2012 Arun S A G <sagarun@gmail.com> - 0.0.8-2
- Fix rpmlint issues
- Add License file
- Remove sitelib and other comments
- Do not clean buildroot in install section

* Mon Apr 02 2012 Arun S A G <sagarun@gmail.com> - 0.0.8-1
- Initial package
