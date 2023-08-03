%global srcname switchboard
%global appname io.elementary.switchboard

Name:           switchboard
Summary:        Modular Desktop Settings Hub
Version:        6.0.2
Release:        2%{?dist}
License:        LGPL-2.0-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1) >= 0.83.0
BuildRequires:  fdupes

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Requires:       hicolor-icon-theme

%description
Extensible System Settings application.


%package        libs
Summary:        Modular Desktop Settings Hub (shared library)

%description    libs
Extensible System Settings application.

This package contains the shared library.


%package        devel
Summary:        Modular Desktop Settings Hub (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Extensible System Settings application.

This package contains the files required for developing plugs for
switchboard.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# create plug directories
mkdir -p %{buildroot}/%{_libdir}/%{name}

mkdir -p %{buildroot}/%{_libdir}/%{name}/hardware
mkdir -p %{buildroot}/%{_libdir}/%{name}/network
mkdir -p %{buildroot}/%{_libdir}/%{name}/personal
mkdir -p %{buildroot}/%{_libdir}/%{name}/system

%fdupes %buildroot%_datadir/locale/
%fdupes %buildroot%_datadir/icons/hicolor/


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING
%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml

%files libs
%doc README.md
%license COPYING

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/*

%{_libdir}/lib%{name}-2.0.so.0
%{_libdir}/lib%{name}-2.0.so.2.0

%files devel
%{_includedir}/%{name}-2.0/

%{_libdir}/lib%{name}-2.0.so
%{_libdir}/pkgconfig/%{name}-2.0.pc

%{_datadir}/vala/vapi/%{name}-2.0.deps
%{_datadir}/vala/vapi/%{name}-2.0.vapi


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com> - 6.0.2-1
- Repackaged for Terra
