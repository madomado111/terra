%global forgeurl https://gitlab.com/ubports/development/core/geonames
%global commit 73c5dfca7d5a8935f7a9f8fe2656d24f8f8fe00a
%forgemeta

Name:       geonames
Version:    0.3.0
Release:    2%?dist
Summary:    Parse and query the geonames database
License:    GPL-3.0
URL:        https://gitlab.com/ubports/development/core/geonames
Source0:    %{url}/-/archive/%commit/geonames-%commit.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: gettext
BuildRequires: fdupes

%description
A library for parsing and querying a local copy of the geonames.org database.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
The %{name}-doc package contains documenation for %{name}.

%prep
%autosetup -n geonames-%commit

%build
%cmake
%cmake_build

%install
%cmake_install
%fdupes %buildroot%_datadir/locale
%find_lang %{name}

%files -f %{name}.lang
%doc doc/reference/geonames-docs.xml.in
%license COPYING COPYING.data
%{_libdir}/libgeonames.so.*

%files devel
%dir %{_includedir}/geonames
%{_includedir}/geonames/geonames.h
%{_libdir}/libgeonames.so
%{_libdir}/pkgconfig/geonames.pc

%files doc
%dir %{_datadir}/gtk-doc/html/geonames
%{_datadir}/gtk-doc/html/geonames/*.html
%{_datadir}/gtk-doc/html/geonames/*.png
%{_datadir}/gtk-doc/html/geonames/style.css
%{_datadir}/gtk-doc/html/geonames/geonames.devhelp2

%changelog
%autochangelog
