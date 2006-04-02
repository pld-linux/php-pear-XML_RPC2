%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	RPC2
%define		_status		alpha
%define		_pearname	XML_RPC2

Summary:	%{_pearname} - XML-RPC client/server library
Summary(pl):	%{_pearname} - biblioteka XML-RPC typu klient-serwer
Name:		php-pear-%{_pearname}
Version:	0.0.7
Release:	1
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	793672d64b01d4ab83469cdb42ae0a2d
URL:		http://pear.php.net/package/XML_RPC2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
XML_RPC2 to pakiet pear dostarczaj±cy us³ug typu klient-serwer.

XML-RPC to prosty protokó³ zdalnego wykonywania procedur (Remote
Procedure Call, RPC) stworzony przy u¿yciu HTTP jako transportu i XML
jako no¶nika danych.

Jako biblioteka kliencka, XML_RPC2 potrafi stworzyæ klasê
po¶rednicz±c± która ujawni metody eksportowane przez serwer. Jako
biblioteka serwera, XML_RPC2 mo¿e eksportowaæ lokalne metody do
zdalnie wykonywanych procedur.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
