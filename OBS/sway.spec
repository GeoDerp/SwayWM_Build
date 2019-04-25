#
# spec file for package sway
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

%bcond_without      systemd
%bcond_with         elogind
%bcond_without      xwayland

Name:               sway
Version:       	    @SERVICE@
Release:            0
Summary:            An i3-compatible Wayland compositor.
License:            MIT
Group:              System/GUI/Other
Url:                https://github.com/swaywm/sway
Source0:            %{name}-%{version}.tar.xz
##Patch0:             0001-Fix-size_t-temporary-underflow-in-log_loaded_themes.patch
BuildRequires:      git
BuildRequires:      meson >= 0.48.0
BuildRequires:      scdoc >= 1.9.4
BuildRequires:   	gcc

BuildRequires:      pkgconfig
BuildRequires:      pkgconfig(cairo)
BuildRequires:      pkgconfig(dbus-1) >= 1.10
BuildRequires:      pkgconfig(gdk-pixbuf-2.0)
BuildRequires:      pkgconfig(json-c) >= 0.13
BuildRequires:      pkgconfig(libcap)
BuildRequires:      pkgconfig(libevdev)
BuildRequires:      pkgconfig(libinput) >= 1.6.0
BuildRequires:      pkgconfig(libpcre)
BuildRequires:      pkgconfig(pango)
BuildRequires:      pkgconfig(pangocairo)
BuildRequires:      pkgconfig(pixman-1)
BuildRequires:      pkgconfig(wayland-client)
BuildRequires:      pkgconfig(wayland-cursor)
BuildRequires:      pkgconfig(wayland-egl)
BuildRequires:      pkgconfig(wayland-protocols) >= 1.14
BuildRequires:      pkgconfig(wayland-server)
BuildRequires:      pkgconfig(wlroots)
BuildRequires:      pkgconfig(xkbcommon)
%if %{with xwayland}
BuildRequires:      pkgconfig(xcb)
%endif
%if %{with systemd}
BuildRequires:      pkgconfig(libsystemd) >= 239
%endif
%if %{with elogind}
BuildRequires:      pkgconfig(libelogind) >= 239
%endif

Requires:           ImageMagick
#Requires:           ffmpeg
%if 0%{?suse_version}
Recommends:         xorg-x11-server-wayland
%endif
Recommends:         swaylock
Recommends:         swayidle

Suggests:           %{name}-bash-completion
Suggests:           %{name}-fish-completion
Suggests:           %{name}-zsh-completion

%description
sway is an i3-compatible Wayland compositor.

%package bash-completion
Summary:            Bash completion for %{name}
Group:              System/Shells
Requires:           %{name} = %{version}
BuildArch:          noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:            Fish completion for %{name}
Group:              System/Shells
Requires:           %{name} = %{version}
BuildArch:          noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:            Zsh completion for %{name}
Group:              System/Shells
Requires:           %{name} = %{version}
BuildArch:          noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
export CFLAGS="%{optflags} -I/usr/include/wayland"
%meson \
  %{?with_xwayland:-Dxwayland=enabled} \
  -Dtray=enabled \
  -Dgdk-pixbuf=enabled \
  -Dman-pages=enabled
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}*
%dir %{_sysconfdir}/sway
%dir %{_sysconfdir}/sway/security.d
%config(noreplace) %{_sysconfdir}/sway/config
%config(noreplace) %{_sysconfdir}/sway/security.d/00-defaults
%dir %{_datadir}/wayland-sessions/
%{_datadir}/wayland-sessions/sway.desktop
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/sway
%{_mandir}/man?/%{name}*

%files bash-completion
%{_datadir}/bash-completion/completions/

%files fish-completion
%dir %{_datadir}/fish/
%{_datadir}/fish/completions/

%files zsh-completion
%{_datadir}/zsh/site-functions/

%changelog
