#
# spec file for package waybar
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           waybar
Version:        @SERVICE@
Release:        0
Summary:        Customizable Wayland bar for Sway and Wlroots based compositors
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/Alexays/Waybar
Source:        	%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  libinput-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  wlroots-devel
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(gdkmm-3.0)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(libmpdclient)
# optional: tray module
BuildRequires:  libdbusmenu-gtk3-devel
# optional: network
BuildRequires:  libnl3-devel
# optional: sway integration
Recommends:     sway


%description
Customizable Wayland bar for Sway and Wlroots based compositors.

%prep
%setup -q 

%build
%meson
%meson_build

%install
%meson_install

%files
%{_sysconfdir}/xdg/waybar/
%{_bindir}/waybar

%changelog
