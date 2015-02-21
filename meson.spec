%global __python %{__python3}

Name:           meson
Version:        0.22.0
Release:        2%{?dist}
Summary:        High productivity build system

License:        ASL 2.0
URL:            https://jpakkane.github.io/meson/
Source0:        https://github.com/jpakkane/meson/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel ninja-build
# Test deps
#BuildRequires:  boost-devel protobuf-devel gobject-introspection-devel
#BuildRequires:  gettext-devel
Requires:       python3-qt5

%description
Meson is a build system designed to optimize programmer
productivity. It aims to do this by providing simple, out-of-the-box
support for modern software development tools and practices, such as
unit tests, coverage reports, Valgrind, CCache and the like.

%prep
%setup -q

%build
# Nothing to build

%install
./install_meson.py --prefix=%{_prefix} --destdir=%{buildroot}
sed -i '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{_datadir}/%{name}/dependencies.py
sed -i '1{\@^#!/usr/bin/python@d}' %{buildroot}%{_datadir}/%{name}/mparser.py
chmod +x %{buildroot}%{_bindir}/meson*

%check
# Disable now, because not all deps in repo
#./run_tests.py

%files
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*.1.*

%changelog
* Thu Jan 22 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-2
- fix shebang in python files

* Wed Jan 21 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-1
- Initial package
