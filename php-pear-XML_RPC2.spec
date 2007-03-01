%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	RPC2
%define		_status		stable
%define		_pearname	XML_RPC2

Summary:	%{_pearname} - XML-RPC client/server library
Summary(pl.UTF-8):	%{_pearname} - biblioteka XML-RPC typu klient-serwer
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e5ee37c07d45e1eb9df3a119af6d95da
URL:		http://pear.php.net/package/XML_RPC2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(curl)
Requires:	php-common >= 3:5.0.0
Requires:	php-pear
Requires:	php-pear-Cache_Lite >= 1.6.0
Requires:	php-pear-PEAR-core >= 1:1.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_RPC2 is a pear package providing XML_RPC client and server
services.

XML-RPC is a simple remote procedure call protocol built using HTTP as
transport and XML as encoding.

As a client library, XML_RPC2 is capable of creating a proxy class
which exposes the methods exported by the server. As a server library,
XML_RPC2 is capable of exposing methods from a class or object
instance, seamlessly exporting local methods as remotely callable
procedures.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
XML_RPC2 to pakiet pear dostarczający usług typu klient-serwer.

XML-RPC to prosty protokół zdalnego wykonywania procedur (Remote
Procedure Call, RPC) stworzony przy użyciu HTTP jako transportu i XML
jako nośnika danych.

Jako biblioteka kliencka, XML_RPC2 potrafi stworzyć klasę
pośredniczącą która ujawni metody eksportowane przez serwer. Jako
biblioteka serwera, XML_RPC2 może eksportować lokalne metody do
zdalnie wykonywanych procedur.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/RPC2

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/XML_RPC2
