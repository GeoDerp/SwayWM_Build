#
# spec file for package swayidle
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


Name:           swayidle
Version:        @SERVICE@
Release:        0
Summary:        Idle management daemon for Wayland
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/swaywm/swayidle
Source:         %{name}-%{version}.tar.xz
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)
Suggests:       %{name}-bash-completion
Suggests:       %{name}-fish-completion
Suggests:       %{name}-zsh-completion

%description
sway's idle management daemon. It is compatible with any Wayland compositor which implements the KDE idle protocol.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -I/usr/include/wayland"
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/swayidle
#%{_mandir}/man1/swayidle.1%{?ext_man}
%{_mandir}/man1/swayidle.1.gz

%files bash-completion
%{_datadir}/bash-completion/completions/

%files fish-completion
%dir %{_datadir}/fish/
%{_datadir}/fish/completions/

%files zsh-completion
%{_datadir}/zsh/site-functions/

%changelog