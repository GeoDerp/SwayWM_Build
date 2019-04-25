#
# spec file for package termite
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           scdoc
Version:        1.9.4
Release:        0
License:        MIT
Summary:        scdoc is a simple man page generator written for POSIX systems written in C99.
Url:            https://git.sr.ht/~sircmpwn/scdoc/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  glibc-devel-static
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
scdoc is a simple man page generator written for POSIX systems written in C99.

%prep
%setup -q

%build
%make_build %{name}

%install
%define pcdir %{buildroot}%{_libdir}/pkgconfig
%make_install PREFIX=%{_prefix} PCDIR=%{pcdir} %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc README.md COPYING
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/%{name}
%{_mandir}/man?/%{name}*

%changelog
