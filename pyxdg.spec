Name:           pyxdg
Version:        0.28
Release:        1
Summary:        Python library to access freedesktop APIs
License:        LGPLv2
URL:            http://freedesktop.org/Software/pyxdg
Source0:        https://pypi.io/packages/source/P/PyXDG/pyxdg-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  hicolor-icon-theme shared-mime-info

%description
PyXDG package provides a library to invoke APIs that conform to freedesktop.org standards.

%package        -n python3-pyxdg
Summary:        Python3 library to access freedesktop APIs
BuildRequires:  python%{python3_pkgversion}-devel
%if %{with check}

BuildRequires:  python%{python3_pkgversion}-nose
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-pyxdg}

%description    -n python%{python3_pkgversion}-pyxdg
This package contains a Python 3 version of PyXDG.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
nosetests-%{python3_version} || :
%endif

%files          -n python%{python3_pkgversion}-pyxdg
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{python3_sitelib}/xdg
%{python3_sitelib}/pyxdg-*.egg-info

%changelog
* Wed Aug 17 2022 YukariChiba <i@0x7f.cc> - 0.28-1
- Upgrade version to 0.28 to solve python version dependency

* Wed Oct 21 2020 zhangpeng <zhangpeng228@huawei.com> - 0.26-3
- disable python2

* Thu Nov 28 2019 lihao <lihao129@huawei.com> - 0.26-2
- Package Init

