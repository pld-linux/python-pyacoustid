Summary:	Python bindings for Chromaprint acoustic finterprinting and the Acoustid API
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki odcisków akustycznych Chromaprint i API Acoustid
# Name must match the python module/package name (as in 'import' statement)
Name:		python-pyacoustid
Version:	0.7
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	https://github.com/lalinsky/pyacoustid/tarball/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cc1a6a21d4483d068f086737e8f58295
URL:		http://www.acoustid.org/chromaprint/
# remove BR: python-devel for 'noarch' packages.
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	libchromaprint >= 0.7
Requires:	python-modules
Provides:	python-chromaprint = %{version}
Obsoletes:	python-chromaprint < 0.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Chromaprint acoustic finterprinting and the
Acoustid API.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki odcisków akustycznych Chromaprint i API
Acoustid.

%prep
%setup -q -n lalinsky-pyacoustid-4701d2b

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

#py_ocomp $RPM_BUILD_ROOT%{py_sitesdir}
#py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/acoustid.py[co]
%{py_sitescriptdir}/chromaprint.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pyacoustid-%{version}-py*.egg-info
%endif
