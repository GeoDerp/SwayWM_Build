#
# spec file for package wayland
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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



%if 0%{?fedora_version}
%define lname	libwayland
%define client libwayland-client
%define cursor libwayland-cursor
%define server libwayland-server
%define egl libwayland-egl
%else 
%define lname	libwayland0
%define client libwayland-client0
%define cursor libwayland-cursor0
%define server libwayland-server0
%define egl libwayland-egl1
%endif

Name:           wayland
Version:        @SERVICE@
Release:        0
Summary:        Wayland Compositor Infrastructure
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/wayland-project/wayland

#Git-Clone:	git://anongit.freedesktop.org/wayland/wayland
#Git-Web:	http://cgit.freedesktop.org/wayland/wayland/
Source0:        %{name}-%{version}.tar.xz
Source4:        baselibs.conf
BuildRequires:  autoconf >= 2.64
BuildRequires:  automake >= 1.11
BuildRequires:  libtool >= 2.2
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libxml-2.0)
%define with_doc 0
%if 0%with_doc
BuildRequires:  doxygen
BuildRequires:  graphviz-gnome
BuildRequires:  xmlto
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

%package -n %{client}
Summary:        Wayland core client library
Group:          System/Libraries

%description -n %{client}
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

%package -n %{cursor}
Summary:        Wayland cursor library
Group:          System/Libraries

%description -n %{cursor}
The purpose of this library is to be the equivalent of libXcursor in
the X world. This library is compatible with X cursor themes and
loads them directly into an shm pool making it easy for the clients
to get buffer for each cursor image.

%package -n %{egl}
Summary:        Additional egl functions for wayland
Group:          System/Libraries
Version:        @SERVICE@

%description -n %{egl}
This package provides additional functions for EGL-using programs
that run within the Wayland framework. This allows for applications
that need not run full-screen and cooperate with a compositor.

%package -n %{server}
Summary:        Wayland core server library
Group:          System/Libraries

%description -n %{server}
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

%package devel
Summary:        Development files for the Wayland Compositor Infrastructure
Group:          Development/Libraries/C and C++
Requires:       %{client} = %version
Requires:       %{cursor} = %version
Requires:       %{egl} = %version
Requires:       %{server} = %version
%if 0%{?suse_version} >= 1500
%if 0%{?suse_version} >= 1550
Provides:       %{egl}-devel = 18.1.5
Obsoletes:      %{egl}-devel < 18.1.5 
%else
Provides:       %{egl}-devel = 18.0.2
Obsoletes:      %{egl}-devel < 18.0.2
%endif
%endif

%description devel
Wayland is a protocol for a compositor to talk to its clients as well
as a C library implementation of that protocol. The compositor can be
a standalone display server running on Linux kernel modesetting and
evdev input devices, an X application, or a wayland client itself.
The clients can be traditional applications, X servers (rootless or
fullscreen) or other display servers.

This package contains all necessary include files and libraries needed
to develop applications that require these.

%package doc
Summary:        Wayland development documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This subpackage contains the documentation to Wayland.

%prep
%setup -q
sed -i 's/<eglversion>/%version/' "%_sourcedir/baselibs.conf"

%build
echo hashudhauauisdhasiuh %WthVersionNo
if [ ! -e configure ]; then
	autoreconf -fi
fi
%configure --disable-static --includedir="%_includedir/%name" \
%if %with_doc
	--docdir="%_defaultdocdir/%name"
%else
	--disable-documentation
%endif
make %{?_smp_mflags}

%install
%make_install %{?_smp_mflags}
find "%buildroot" -type f -name "*.la" -delete -print

%check
%if !0%{?qemu_user_space_build}
mkdir -p xdg/wayland-tests
chmod a+x xdg xdg/wayland-tests
export XDG_RUNTIME_DIR="$PWD/xdg"
if ! make check V=1; then
	cat test-suite.log
	exit 1
fi
%endif

%post   -n %{client} -p /sbin/ldconfig
%postun -n %{client} -p /sbin/ldconfig
%post   -n %{cursor} -p /sbin/ldconfig
%postun -n %{cursor} -p /sbin/ldconfig
%post   -n %{egl} -p /sbin/ldconfig
%postun -n %{egl} -p /sbin/ldconfig
%post   -n %{server} -p /sbin/ldconfig
%postun -n %{server} -p /sbin/ldconfig

%files -n %{client}
%defattr(-,root,root)
%_libdir/libwayland-client.so.0*
%doc COPYING

%files -n %{cursor}
%defattr(-,root,root)
%_libdir/libwayland-cursor.so.0*

%files -n %{egl}
%defattr(-,root,root)
%_libdir/libwayland-egl.so.1*

%files -n %{server}
%defattr(-,root,root)
%_libdir/libwayland-server.so.0*

%files devel
%defattr(-,root,root)
%_bindir/wayland-scanner
%_includedir/%name/
%_libdir/libwayland-*.so
%_libdir/pkgconfig/wayland-*.pc
%_datadir/aclocal/
%_datadir/wayland/

%if %with_doc
%files doc
%defattr(-,root,root)
%_mandir/man3/wl*.3*
%_docdir/%name/
%endif

%changelog
