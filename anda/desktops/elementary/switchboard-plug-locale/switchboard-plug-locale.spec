%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-locale

%global plug_type personal
%global plug_name locale
%global plug_rdnn io.elementary.switchboard.locale

Name:           switchboard-plug-locale
Summary:        Switchboard Locale Plug
Version:        2.5.9
Release:        2%?dist
License:        LGPL-3.0-or-later

URL:            https://github.com/elementary/%name
Source0:        %url/archive/%version/%srcname-%version.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46.1
BuildRequires:  vala
BuildRequires:  fdupes

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  polkit-devel
BuildRequires:  switchboard-devel

Requires:       switchboard%?_isa
Supplements:    switchboard%?_isa

%description
%summary.

%prep
%autosetup -n %srcname-%version -p1


%build
%meson
%meson_build


%install
%meson_install
%fdupes %buildroot%_datadir/locale/
%find_lang %plug_name-plug


%check
appstream-util validate-relax --nonet \
    %buildroot/%_datadir/metainfo/%plug_rdnn.appdata.xml


%files -f %plug_name-plug.lang
%doc README.md
%license COPYING

%_libdir/switchboard/%plug_type/lib%plug_name-plug.so
%_libdir/switchboard/personal/pantheon-locale/languagelist
%_libdir/switchboard/personal/pantheon-locale/packages_blacklist
%_datadir/glib-2.0/schemas/%plug_rdnn.gschema.xml
%_datadir/polkit-1/actions/%plug_rdnn.policy

%_datadir/metainfo/%plug_rdnn.appdata.xml

%changelog
* Tue Jun 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.5.9-1
- Initial package.
