Name:			graalvm
Version:		22.3.1
Release:		1%{?dist}
URL:			https://www.graalvm.org/
%ifarch x86_64
Source0:		https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-%{version}/graalvm-ce-java11-linux-amd64-%{version}.tar.gz
%elifarch aarch64
Source0:		https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-%{version}/graalvm-ce-java11-linux-aarch64-%{version}.tar.gz
%endif