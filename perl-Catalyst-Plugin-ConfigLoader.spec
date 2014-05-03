%define upstream_name	 Catalyst-Plugin-ConfigLoader
%define upstream_version 0.34

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Load config files of various types

License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Config::Any) >= 0.08
BuildRequires:	perl(Data::Visitor) >= 0.02
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Mouse)
BuildArch:	noarch

%description
This module will attempt to load find and load a configuration file of
various types. Currently it supports YAML, JSON, XML, INI and Perl
formats.

To support the distinction between development and production
environments, this module will also attemp to load a local config
(e.g. myapp_local.yaml) which will override any duplicate settings.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}
sed -i.DOS -e 's/\r//g' Changes
sed -i.DOS -e 's/\r//g' README

%build
perl Makefile.PL installdirs=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst



