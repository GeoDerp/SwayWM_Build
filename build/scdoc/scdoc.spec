Name:     scdoc
Version:  1.8.1
Release:  1%{?dist}
Summary:  Tool for generating roff manual pages

License:  MIT
URL:      https://git.sr.ht/~sircmpwn/%{name}
Source0:  %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: sed

%description
scdoc is a tool designed to make the process of writing man pages more
friendly. It reads scdoc syntax from stdin and writes roff to stdout, suitable
for reading with man.

%prep
%setup -q

# Disable static linking
sed -i '/-static/d' Makefile

# Fix 'harcoded' installation path
sed -i 's/DESTDIR=/DESTDIR?=/g' Makefile
sed -i 's/PREFIX=/PREFIX?=/g' Makefile

# Fix 'hardcoded' CFLAGS
sed -i 's/CFLAGS=/CFLAGS+=/g' Makefile

# Use INSTALL provided by the make_install macro
sed -i 's/\tinstall/\t$(INSTALL)/g' Makefile

%build
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%check
make check

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.5*

%changelog
* Sun Jan 20 2019 Timothée Floure <fnux@fedoraproject.org> - 1.6.1-1
- New upstream release

* Wed Jan 16 2019 Timothée Floure <fnux@fedoraproject.org> - 1.6.0-1
- New upstream release

* Mon Oct 22 2018 Timothée Floure <fnux@fedoraproject.org> - 1.5.2-1
- New upstream release
- Fix broken source URL

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4

* Sat May 26 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.3-1
- Let there be package
