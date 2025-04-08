%define module executing
%bcond_without test

Name:		python-executing
Version:	2.2.0
Release:	1
Summary:	Get the currently executing AST node of a frame, and other information
URL:		https://pypi.org/project/executing/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/e/executing/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with test}
BuildRequires:	ipython
BuildRequires:	python%{pyver}dist(asttokens) >= 2.1.0
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(coverage)
BuildRequires:	python%{pyver}dist(littleutils)
BuildRequires:	python%{pyver}dist(rich)
%endif

%description
Get information about what a Python frame is currently doing,
particularly the AST node being executed.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py3_install

%if %{with test}
%check
# test_global_tester_calls requires a python module named coverage_enable_subprocess
# which is a python module that has no licence or readme file making that
# module unpackagable, disable the test requiring it.
pytest -v tests/ -k "not test_global_tester_calls"
%endif

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}*.*-info
%license LICENSE.txt
%doc README.md
