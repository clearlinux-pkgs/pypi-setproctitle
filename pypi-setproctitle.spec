#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6013BD3AFCF957DE (daniele.varrazzo@gmail.com)
#
Name     : pypi-setproctitle
Version  : 1.2.3
Release  : 47
URL      : https://files.pythonhosted.org/packages/78/9a/cf6bf4c472b59aef3f3c0184233eeea8938d3366bcdd93d525261b1b9e0a/setproctitle-1.2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/78/9a/cf6bf4c472b59aef3f3c0184233eeea8938d3366bcdd93d525261b1b9e0a/setproctitle-1.2.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/78/9a/cf6bf4c472b59aef3f3c0184233eeea8938d3366bcdd93d525261b1b9e0a/setproctitle-1.2.3.tar.gz.asc
Summary  : A Python module to customize the process title
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-setproctitle-filemap = %{version}-%{release}
Requires: pypi-setproctitle-lib = %{version}-%{release}
Requires: pypi-setproctitle-license = %{version}-%{release}
Requires: pypi-setproctitle-python = %{version}-%{release}
Requires: pypi-setproctitle-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
==============================================

%package filemap
Summary: filemap components for the pypi-setproctitle package.
Group: Default

%description filemap
filemap components for the pypi-setproctitle package.


%package lib
Summary: lib components for the pypi-setproctitle package.
Group: Libraries
Requires: pypi-setproctitle-license = %{version}-%{release}
Requires: pypi-setproctitle-filemap = %{version}-%{release}

%description lib
lib components for the pypi-setproctitle package.


%package license
Summary: license components for the pypi-setproctitle package.
Group: Default

%description license
license components for the pypi-setproctitle package.


%package python
Summary: python components for the pypi-setproctitle package.
Group: Default
Requires: pypi-setproctitle-python3 = %{version}-%{release}

%description python
python components for the pypi-setproctitle package.


%package python3
Summary: python3 components for the pypi-setproctitle package.
Group: Default
Requires: pypi-setproctitle-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(setproctitle)

%description python3
python3 components for the pypi-setproctitle package.


%prep
%setup -q -n setproctitle-1.2.3
cd %{_builddir}/setproctitle-1.2.3
pushd ..
cp -a setproctitle-1.2.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656373687
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-setproctitle
cp %{_builddir}/setproctitle-1.2.3/COPYRIGHT %{buildroot}/usr/share/package-licenses/pypi-setproctitle/99eb8f40e1bd013ba90a0898094b02d9fb2eadec
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-setproctitle

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-setproctitle/99eb8f40e1bd013ba90a0898094b02d9fb2eadec

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
