%define upstream_name	 Catalyst-Plugin-ConfigLoader
%define upstream_version 0.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Load config files of various types
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.300.0-2mdv2011.0
+ Revision: 680730
- mass rebuild

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2011.0
+ Revision: 572218
- update to 0.30

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 554159
- update to 0.28

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.0
+ Revision: 418404
- update to 0.27

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.0
+ Revision: 415034
- update to 0.26

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2010.0
+ Revision: 406261
- rebuild using %%perl_convert_version

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2010.0
+ Revision: 392786
- update to new version 0.24

* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2010.0
+ Revision: 378111
- update to new version 0.23

* Thu Jan 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2009.1
+ Revision: 327131
- update to new version 0.22

* Tue Aug 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2009.0
+ Revision: 271051
- update to new version 0.21

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2009.0
+ Revision: 202327
- update to new version 0.20

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2008.1
+ Revision: 111153
- update to new version 0.19

* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2008.1
+ Revision: 105900
- update to new version 0.18
- update to new version 0.18

* Wed Aug 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2008.0
+ Revision: 74301
- update build dependencies
- update to new version 0.17

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2008.0
+ Revision: 69204
- update to new version 0.15

* Mon Apr 30 2007 Olivier Thauvin <nanardon@mandriva.org> 0.14-1mdv2008.0
+ Revision: 19689
- fix build

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    -New version


* Fri Aug 25 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-25 12:52:46 (58083)
- Version 0.13

* Sat Aug 05 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-05 21:49:07 (53371)
import perl-Catalyst-Plugin-ConfigLoader-0.12-1mdv2007.0

* Thu Aug 03 2006 Scott Karns <scottk@mandriva.org> 0.12-1mdv2007.0
- Version 0.12

* Fri Jul 14 2006 Scott Karns <scottk@mandriva.org> 0.11-1mdv2007.0
- Version 0.11

* Thu Jun 29 2006 Scott Karns <scott@karnstech.com> 0.09-1mdv2007.0
- Initial Mandriva RPM

