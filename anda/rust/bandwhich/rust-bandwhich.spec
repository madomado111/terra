# Generated by rust2rpm 23
%global crate bandwhich

Name:           rust-bandwhich
Version:        0.20.0
Release:        %autorelease
Summary:        Show network utilization by process/connection/hostname/IP
License:        MIT
URL:            https://crates.io/crates/bandwhich
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          bandwhich-fix-metadata-auto.diff

BuildRequires:  anda-srpm-macros rust-packaging >= 21

%global _description %{expand:
Display current network utilization by process, connection and remote
IP/hostname.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.md
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/bandwhich

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install
rm %{buildroot}/.cargo -rf

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
