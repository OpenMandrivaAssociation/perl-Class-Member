%define real_name Class-Member

Summary:	Class::Member - A set of modules to make the module developement easier
Name:		perl-%{real_name}
Version:	1.5
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/O/OP/OPI/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Class::Member - A set of modules to make the module developement
easier.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/Class/Member
%{perl_vendorlib}/Class/Member.pm
%{perl_vendorlib}/Class/Member/*.pm
%{_mandir}/*/*

