%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define packagename PEAK-Rules
%define devrev  2582

%define docs README.txt AST-Builder.txt Code-Generation.txt Criteria.txt DESIGN.txt Indexing.txt Predicates.txt Syntax-Matching.txt

Name:           python-peak-rules
Version:        0.5a1.dev
# At earliest opportunity, move all non-numeric information to release.
# This would be proper:
# Version: 0.5
# Release:0.3.a1.dev%{devrev}%{?dist}
# But we can't do that yet because it breaks the upgrade path.
# When version hits 0.5.1 or 0.6 we can correct this.
Release:        9.%{devrev}.1%{?dist}
Summary:        Generic functions and business rules support systems

Group:          Development/Languages
License:        Python or ZPLv2.1
URL:            http://pypi.python.org/pypi/PEAK-Rules
Source0:        http://peak.telecommunity.com/snapshots/%{packagename}-%{version}-r%{devrev}.tar.gz
Patch0:         %{name}-setup.patch
Patch1:         %{name}-doctest.patch
Patch2:         %{name}-x86_64-doctest.patch
Patch3:         %{name}-py26-deprecation.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel
BuildRequires:       python-peak-util-assembler >= 0.3
BuildRequires:       python-peak-util-addons >= 0.6
BuildRequires:       python-peak-util-extremes >= 1.1
BuildRequires:       python-decoratortools >= 1.7

Requires:       python-peak-util-assembler >= 0.3
Requires:       python-peak-util-addons >= 0.6
Requires:       python-peak-util-extremes >= 1.1
Requires:       python-decoratortools >= 1.7

%description
PEAK-Rules is a highly-extensible framework for creating and using generic
functions, from the very simple to the very complex.  Out of the box, it
supports multiple-dispatch on positional arguments using tuples of types,
full predicate dispatch using strings containing Python expressions, and
CLOS-like method combining.  (But the framework allows you to mix and match
dispatch engines and custom method combinations, if you need or want to.)

%prep
%setup -q -n %{packagename}-%{version}-r%{devrev}
%patch0 -b .setup
%patch1 -p1 -b .test
%patch2 -p0 -b .x86_64
%patch3 -p1
%{__chmod} -x %{docs}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%check
# Disable checks on s390x for now, see bugzilla #495874 
%ifnarch s390x
%{__python} setup.py test
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{docs}
%{python_sitelib}/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.5a1.dev-9.2582.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5a1.dev-9.2582
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Kyle VanderBeek <kylev@kylev.com> - 0.5a1.dev-8.2582
- SVN r2600 to fix python 2.6 deprecation warnings from BitmapIndex

* Wed Jun 03 2009 Luke Macken <lmacken@redhat.com> 0.5a1.dev-7.2582
- Add a patch to get the doctests to work on x86_64

* Wed Apr 15 2009 Karsten Hopp <karsten@redhat.com> 0.5a1.dev-6.2582
- Disable checks on s390x for now, see bugzilla #495874 

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5a1.dev-5.2582
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 2 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5a1.dev-4.2582
- Update patch for some more doctest fixing under py2.6.

* Tue Dec 2 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5a1.dev-3.2582
- Update to latest development snapshot
- Enable test suite
- Patch so doctests pass

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5a1.dev-2.2581
- Rebuild for Python 2.6

* Tue Oct 14 2008 Luke Macken <lmacken@redhat.com> - 0.5a1.dev-1.2581
- Revision bump to fix upgrade path

* Sat Oct 11 2008 Luke Macken <lmacken@redhat.com> - 0.5a1.dev-0.1.2581
- Update to the latest 0.5a1 development snapshot
- Fix the description

* Sun Aug  3 2008 Luke Macken <lmacken@redhat.com> - 0.5a1.dev-0.2569
- Initial package for Fedora
