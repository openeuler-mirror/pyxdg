Name:           pyxdg
Version:        0.26
Release:        2
Summary:        Python library to access freedesktop APIs
License:        LGPLv2
URL:            http://freedesktop.org/Software/pyxdg
Source0:        https://pypi.io/packages/source/P/PyXDG/pyxdg-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  hicolor-icon-theme shared-mime-info

%description
PyXDG package provides a library to invoke APIs that conform to freedesktop.org standards.

%package        -n python2-pyxdg
Summary:        Python2 library to access freedesktop APIs
BuildRequires:  python2-devel python2-nose
%{?python_provide:%python_provide python2-pyxdg}
Provides:       pyxdg = %{version}-%{release}
Obsoletes:      pyxdg < 0.25-10

%description    -n python2-pyxdg
This package contains a Python 2 version of PyXDG.

%package        -n python3-pyxdg
Summary:        Python3 library to access freedesktop APIs
BuildRequires:  python3-devel python3-nose
%{?python_provide:%python_provide python3-pyxdg}

%description    -n python3-pyxdg
This package contains a Python 3 version of PyXDG.

%prep
%autosetup -p1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
nosetests-%{python2_version} || :
nosetests-%{python3_version} || :

%files          -n python2-pyxdg
%{python2_sitelib}/xdg
%{python2_sitelib}/pyxdg-*.egg-info
%license COPYING
%doc AUTHORS ChangeLog README TODO

%files          -n python3-pyxdg
%{python3_sitelib}/xdg
%{python3_sitelib}/pyxdg-*.egg-info
%license COPYING
%doc AUTHORS ChangeLog README TODO

%changelog
* Thu Nov 28 2019 lihao <lihao129@huawei.com> - 0.26-2
- Package Init

