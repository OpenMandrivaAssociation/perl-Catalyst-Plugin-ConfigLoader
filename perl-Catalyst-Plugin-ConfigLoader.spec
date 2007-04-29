%define module	Catalyst-Plugin-ConfigLoader
%define name	perl-%{module}
%define	modprefix Catalyst

%define version	0.14
%define	rel	1
%define release	%mkrel %{rel}

Summary:	Load config files of various types
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Config::Any) >= 0.04
BuildRequires:	perl(Data::Visitor) >= 0.02
BuildRequires:  perl(Module::Build)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
This module will attempt to load find and load a configuration file of
various types. Currently it supports YAML, JSON, XML, INI and Perl
formats.

To support the distinction between development and production
environments, this module will also attemp to load a local config
(e.g. myapp_local.yaml) which will override any duplicate settings.


%prep
%setup -q -n %{module}-%{version}
sed -i.DOS -e 's/\r//g' Changes
sed -i.DOS -e 's/\r//g' README

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

%clean
rm -rf %{buildroot}
