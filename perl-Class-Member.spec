%define upstream_name    Class-Member
%define upstream_version 1.6

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Class::Member - A set of modules to make the module developement easier
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/O/OP/OPI/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Class::Member - A set of modules to make the module developement
easier.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/Class/Member
%{perl_vendorlib}/Class/Member.pm
%{perl_vendorlib}/Class/Member/*.pm
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.600.0-2mdv2011.0
+ Revision: 680824
- mass rebuild

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.600.0-1mdv2011.0
+ Revision: 505430
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.6-2mdv2010.0
+ Revision: 430331
- rebuild

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.6-1mdv2009.0
+ Revision: 270344
- update to new version 1.6

* Thu Jun 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdv2009.0
+ Revision: 229223
- update to new version 1.5

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-2mdv2008.0
+ Revision: 86150
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdv2007.0
- rebuild

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdk
- initial Mandriva package

