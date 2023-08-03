%global nodev 16.17.0
%global npmv 8.11.0
%global ver 0.14.7
%define debug_package %nil

Name:			voicevox
Version:		%ver
Release:		1%?dist
Summary:		Free Japanese text-to-speech editor
License:		LGPL-3.0
URL:			https://voicevox.hiroshiba.jp
Source0:		https://github.com/VOICEVOX/voicevox/archive/refs/tags/%version.tar.gz
# requires specific node and npm version
%ifarch x86_64
%global a x64
%elifarch aarch64
%global a arm64
%endif
Source1:		https://nodejs.org/download/release/v%nodev/node-v%nodev-linux-%a.tar.xz
Patch0:			0001-feat-add-repository-entry-in-package.json.patch

%description
VOICEVOX is a free Japanese text-to-speech software with medium output quality.

%package doc
Summary: Documentation files for voicevox (Japanese)

%description doc
%summary.

%prep
%autosetup -p1
tar xf %SOURCE1
PATH="$PATH:$PWD/node-v%nodev-linux-%a/bin/"
npx npm@%npmv i

%build
PATH="$PATH:$PWD/node-v%nodev-linux-%a/bin/"
npx browserslist@latest --update-db
PATH="$PATH:$PWD/node-v%nodev-linux-%a/bin/"
npm run electron:build

%install
rm dist_electron/linux-unpacked/README.txt # dummy
mkdir -p %buildroot%_datadir/%name %buildroot%_bindir %buildroot%_docdir/%name/res
mv dist_electron/linux-unpacked/* %buildroot%_datadir/%name/
ln -s %_datadir/%name/%name %buildroot%_bindir/%name
install -Dm644 docs/*.md %buildroot%_docdir/%name/
install -Dm644 docs/res/* %buildroot%_docdir/%name/res/

%files
%doc README.md
%license LICENSE LGPL_LICENSE
%_bindir/%name
%_datadir/%name/

%files doc
%doc %_docdir/%name/

%changelog
%autochangelog
