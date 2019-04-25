#
# spec file for package wlroots
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without  libcap
%bcond_without  systemd
%bcond_with     elogind
%bcond_without  x11_backend
%bcond_without  xwayland
%bcond_without  xcb_errors

#if 0%{?suse_version}
#%cond_without  xcb_errors
#else
#%bcond_without      xcb_errors
#endif
Name:           wlroots
Version:        @SERVICE@
Release:        0
Summary:        Modular Wayland compositor library
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/swaywm/wlroots
Source:        %{name}-%{version}.tar.xz
##Patch0:         0001-Remove-unwanted-libinput-include.patch
##Patch1:         0002-Remove-rendundant-redeclaration-warning.patch
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm) >= 2.4.95
BuildRequires:  pkgconfig(libinput) >= 1.7.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.16
BuildRequires:  pkgconfig(wayland-server) >= 1.16
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  cmake
%if %{with libcap}
BuildRequires:  pkgconfig(libcap)
%endif
%if %{with systemd}
BuildRequires:  pkgconfig(libsystemd)
%endif
%if %{with elogind}
BuildRequires:  pkgconfig(libelogind)
%endif
%if %{with x11_backend} || %{with xwayland}
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xkb)
%if %{with xcb_errors}
BuildRequires:  pkgconfig(xcb-errors)
%endif
%endif

%description
Pluggable, composable modules for building a Wayland compositor.

%package devel
Summary:        Modular Wayland compositor library
Group:          Development/Libraries/C and C++
Requires:       libwlroots2 = %{version}

%description devel
Pluggable, composable modules for building a Wayland compositor.

%package -n libwlroots2
Summary:        Modular Wayland compositor library
Group:          System/Libraries

%description -n libwlroots2
Pluggable, composable modules for building a Wayland compositor.

%prep
%autosetup -n %{name}-%{version} -p1
#%{_bindir}/find %{_builddir}/%{name}-%{version} -name '.gitignore' -delete

%build
%if 0%{?suse_version}
export CFLAGS="%{optflags} -I/usr/include/wayland -Wno-redundant-decls"
%endif

%meson \
  %{?with_libcap:-Dlibcap=enabled} \
%if %{with systemd} || %{with elogind}
  -Dlogind=enabled \
  %{?with_systemd:-Dlogind-provider=systemd} \
  %{?with_elogind:-Dlogind-provider=elogind} \
%endif
%if %{with xcb_error}
  -Dxcb_error=enabled \
  %{?with_xcb_error:-Dxcb_error=xcb_error} \
%else  
  %{?with_xcb_errors:-Dxcb_errors=enabled} \
%endif 
%if %{with x11_backend} || %{with xwayland}
  %{?with_x11_backend:-Dx11_backend=enabled} \
  %{?with_xwayland:-Dxwayland=enabled} \
  -Dxcb-xkb=enabled \
  -Dxcb-icccm=enabled \
%endif
  -Drootston=false \
  -Dexamples=false
%meson_build

%install
%meson_install

%post   -n libwlroots2 -p /sbin/ldconfig
%postun -n libwlroots2 -p /sbin/ldconfig

%files devel
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_includedir}/wlr/
%{_libdir}/pkgconfig/wlroots.pc
%{_libdir}/libwlroots.so

%files -n libwlroots2
%{_libdir}/libwlroots.so.*

%changelog

