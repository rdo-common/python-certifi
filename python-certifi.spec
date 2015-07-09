%if %{?fedora}
%global with_python3 1
%else
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

%global pypi_name certifi

Name:           python-%{pypi_name}
Version:        2015.04.28
Release:        5%{?dist}
Summary:        Python package for providing Mozilla's CA Bundle

License:        MPLv2.0
#https://www.mozilla.org/MPL/2.0/
URL:            http://certifi.io/en/latest/
Source0:        https://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch1:         certifi-2015.04.28-remove-bundle-cert.patch

BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
Requires:       ca-certificates

%if 0%{?with_python3}
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
Requires:       python3
Requires:       ca-certificates
%endif # if with_python3

%description
Certifi is a carefully curated collection of Root Certificates for
 validating the trustworthiness of SSL certificates while verifying 
the identity of TLS hosts. It has been extracted from the Requests project.


Please note that this Fedora package links to the bundle certificates 
of ca-certificates. For Python 3 support install python3-certifi
%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Python 3 package for providing Mozilla's CA Bundle
Group:          Development/Libraries

%description -n python3-%{pypi_name}
Python 3 Certifi is a carefully curated collection of Root Certificates for
 validating the trustworthiness of SSL certificates while verifying 
the identity of TLS hosts. It has been extracted from the Requests project.

Please note that this Fedora package links to the bundle certificates 
of ca-certificates.
%endif # if with_python3

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
rm -rf certifi/*.pem
%patch1

#drop shebangs from python_sitearch
find %{_builddir}/%{pypi_name}-%{version} -name '*.py' \
    -exec sed -i '1{\@^#!/usr/bin/env python@d}' {} \;

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root=%{buildroot}
popd
%endif # with_python3

%files
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py?.?.egg-info
%endif # with_python3

%changelog
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
