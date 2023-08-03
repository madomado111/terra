%global forgeurl https://gitlab.com/ubports/development/core/lomiri-schemas
%global commit fed68d63df86c0b39654b66c31e02be25018f5f1
%forgemeta

Name:       lomiri-schemas
Version:    0.1.3
Release:    %autorelease
Summary:    Configuration schemas for lomiri
License:    LGPL-2.0-or-later
URL:        https://gitlab.com/ubports/development/core/lomiri-schemas
Source0:    %url/-/archive/%commit/lomiri-schemas-%commit.tar.gz
Patch0:     https://gitlab.com/cat-master21/lomiri-schemas/-/commit/a2608b71af114abb69982fba25d439ffed255f56.patch
BuildArch:  noarch

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: glib2-devel
BuildRequires: gettext
BuildRequires: intltool

%description
Configuration schemas for lomiri desktop enviroment.

%prep
%autosetup -n %{name}-%commit -p1

%build
%cmake -DCMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT=true
%cmake_build

%install
%cmake_install

%files
%{_datadir}/accountsservice/interfaces/*.xml
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pkgconfig/lomiri-schemas.pc
%{_datadir}/polkit-1/actions/com.lomiri.AccountsService.policy
%{_sharedstatedir}/polkit-1/localauthority/10-vendor.d/50-com.lomiri.AccountsService.pkla

%changelog
%autochangelog
