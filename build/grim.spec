Name:           grim
Version:        1.3
Release:        1%{?dist}
Summary:        Grab images from a Wayland compositor

License:        MIT
URL:            https://github.com/emersion/grim
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  meson
BuildRequires:  wlroots-devel >= 0.3-1
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  scdoc
BuildRequires:  cairo
BuildRequires:  libjpeg-devel

Requires:       wlroots >= 0.3-1
Requires:       cairo
Requires:       gdk-pixbuf2


%description
swaylock is a screenshot utility for slurp and sway.


%prep
%autosetup


%build
%meson --auto-features=auto
%meson_build


%install
%meson_install


%check
%meson_test


%files
%{_bindir}/swaylock
%{_datadir}/bash-completion/completions/swaylock
%{_datadir}/fish/completions/swaylock.fish
%{_datadir}/zsh/site-functions/_swaylock

%{_mandir}/man1/swaylock.1.gz

%config %{_sysconfdir}/pam.d/swaylock

%license LICENSE
%doc README.*
