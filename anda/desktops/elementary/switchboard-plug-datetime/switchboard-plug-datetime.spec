%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-datetime

%global plug_type system
%global plug_name datetime
%global plug_rdnn io.elementary.switchboard.datetime

Name:           switchboard-plug-datetime
Summary:        Switchboard Date & Time Plug
Version:        2.2.0
Release:        2%{?dist}
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/switchboard-plug-datetime
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  fdupes

BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  switchboard-devel

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
%summary.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%fdupes %buildroot%_datadir/locale/
%find_lang %{plug_name}-plug

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
* Tue Jun 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.2.0-1
- Initial package.
