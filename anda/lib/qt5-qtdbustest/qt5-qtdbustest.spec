%global forgeurl https://gitlab.com/ubports/development/core/libqtdbustest
%global commit 58990d63f2327d285d6ead430d03b02558257291
%forgemeta

Name:       qt5-qtdbustest
Version:    0.3.0
Release:    %autorelease
Summary:    Library for testing DBus interactions using Qt5
License:    LGPL-3.0
URL:        https://gitlab.com/ubports/development/core/libqtdbustest
Source0:    %url/-/archive/%commit/libqtdbustest-%commit.tar.gz

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: gcc-c++
BuildRequires: gcovr
BuildRequires: lcov
BuildRequires: qt5-qtbase-devel
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(gtest)

%description
A simple library for testing Qt based DBus services and clients.
This package contains the shared libraries.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n libqtdbustest-%commit

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license COPYING
%{_bindir}/qdbus-simple-test-runner
%{_libdir}/libqtdbustest.so.*
%dir %{_libexecdir}/libqtdbustest
%{_libexecdir}/libqtdbustest/watchdog
%dir %{_datadir}/libqtdbustest
%{_datadir}/libqtdbustest/*.conf

%files devel
%dir %{_includedir}/libqtdbustest-1
%dir %{_includedir}/libqtdbustest-1/libqtdbustest
%{_includedir}/libqtdbustest-1/libqtdbustest/*.h
%{_libdir}/libqtdbustest.so
%{_libdir}/pkgconfig/libqtdbustest-1.pc

%changelog
%autochangelog
