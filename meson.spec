%global __python %{__python3}
%global commit c6dbf98a055bb0fe1d36fc9f4f757b67ca613f01
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           meson
Version:        0.22.0
Release:        5.git%{shortcommit}%{?dist}
Summary:        High productivity build system

License:        ASL 2.0
URL:            https://jpakkane.github.io/meson/
#Source0:        https://github.com/jpakkane/meson/archive/%{version}/%{name}-%{version}.tar.gz
Source0:        https://github.com/jpakkane/meson/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel ninja-build
# Test deps
#BuildRequires:  boost-devel protobuf-devel gobject-introspection-devel
#BuildRequires:  gettext-devel
Requires:       ninja-build
Requires:       python3-qt5

%description
Meson is a build system designed to optimize programmer
productivity. It aims to do this by providing simple, out-of-the-box
support for modern software development tools and practices, such as
unit tests, coverage reports, Valgrind, CCache and the like.

%prep
%setup -qn %{name}-%{commit}

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
* Thu Feb 26 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-5.gitc6dbf98
- Fix packaging style
- Make package noarch

* Mon Feb 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-4.git.c6dbf98
- Use development version

* Sat Feb 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.22.0-3
- Add ninja-build to requires

* Thu Jan 22 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-2
- fix shebang in python files

* Wed Jan 21 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-1
- Initial package
