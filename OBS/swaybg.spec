Name:           swaybg
Version:        @SERVICE@
Release:        0
Summary:        Idle management daemon for Wayland
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/swaywm/swaybg
Source:         %{name}-%{version}.tar.xz
BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  systemd-devel
BuildRequires:  git
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(cairo) 
%if 0%{?suse_version}
BuildRequires:  gdk-pixbuf-devel
%else 
BuildRequires: 	gdk-pixbuf2-devel
%endif 
Suggests:       %{name}-bash-completion
Suggests:       %{name}-fish-completion
Suggests:       %{name}-zsh-completion

%description
swaybg is a wallpaper utility for Wayland compositors. It is compatible with any Wayland compositor which implements the following Wayland protocols:
wlr-layer-shell
xdg-output
xdg-shell

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
%license LICENSE
%doc README.md
%{_bindir}/swaybg
%{_mandir}/man1/%{name}*

%changelog
