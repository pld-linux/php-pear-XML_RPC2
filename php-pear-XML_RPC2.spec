%define		status		stable
%define		pearname	XML_RPC2
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - XML-RPC client/server library
Summary(pl.UTF-8):	%{pearname} - biblioteka XML-RPC typu klient-serwer
Name:		php-pear-%{pearname}
Version:	1.1.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	bc37d9b321cfeba56a5b62856e36f141
URL:		http://pear.php.net/package/XML_RPC2/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= 5.0.0
Requires:	php(curl)
Requires:	php-pear
Requires:	php-pear-Cache_Lite >= 1.6.0
Requires:	php-pear-HTTP_Request2 >= 2.0.0
Requires:	php-pear-PEAR-core >= 1:1.0-0.b1
Obsoletes:	php-pear-XML_RPC2-tests
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

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
XML_RPC2 to pakiet pear dostarczający usług typu klient-serwer.

XML-RPC to prosty protokół zdalnego wykonywania procedur (Remote
Procedure Call, RPC) stworzony przy użyciu HTTP jako transportu i XML
jako nośnika danych.

Jako biblioteka kliencka, XML_RPC2 potrafi stworzyć klasę
pośredniczącą która ujawni metody eksportowane przez serwer. Jako
biblioteka serwera, XML_RPC2 może eksportować lokalne metody do
zdalnie wykonywanych procedur.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/tests/XML_RPC2/tests .
mv docs/XML_RPC2/docs/* .

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
