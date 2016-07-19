%global pypi_name certifi

Name:           python-%{pypi_name}
Version:        2015.04.28
Release:        9%{?dist}
Summary:        Python package for providing Mozilla's CA Bundle

License:        MPLv2.0
#https://www.mozilla.org/MPL/2.0/
URL:            http://certifi.io/en/latest/
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch1:         certifi-2015.04.28-remove-bundle-cert.patch

BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
Requires:       python3
Requires:       ca-certificates

%description
Certifi is a carefully curated collection of Root Certificates for
 validating the trustworthiness of SSL certificates while verifying 
the identity of TLS hosts. It has been extracted from the Requests project.

Please note that this Fedora package links to the bundle certificates 
of ca-certificates. For Python 3 support install python3-certifi

%package -n python2-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Certifi is a carefully curated collection of Root Certificates for
 validating the trustworthiness of SSL certificates while verifying
the identity of TLS hosts. It has been extracted from the Requests project.

Please note that this Fedora package links to the bundle certificates
of ca-certificates. For Python 3 support install python3-certifi


%package -n python3-%{pypi_name}
Summary:        Python 3 package for providing Mozilla's CA Bundle
Group:          Development/Libraries
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python 3 Certifi is a carefully curated collection of Root Certificates for
 validating the trustworthiness of SSL certificates while verifying 
the identity of TLS hosts. It has been extracted from the Requests project.

Please note that this Fedora package links to the bundle certificates 
of ca-certificates.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
rm -rf certifi/*.pem
%patch1

#drop shebangs from python_sitearch
find %{_builddir}/%{pypi_name}-%{version} -name '*.py' \
    -exec sed -i '1{\@^#!/usr/bin/env python@d}' {} \;

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{pypi_name}
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py?.?.egg-info

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.04.28-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.04.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.04.28-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 16 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 2015.04.28-6
- Update python macros
- Include subpackages for Python2 and Python3

* Thu Jul 09 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-5
- rebuilt

* Wed Jul 08 2015 William Moreno Reyes  <williamjmorenor at gmail.com> 
- 2015.04.28-4
- Initial Import of #1232433

* Mon Jul 06 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-3
- Remove shebang

* Thu Jul 02 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-2
- Remove bundle cacert.pem

* Tue Jun 16 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-1
- Initial packaging
