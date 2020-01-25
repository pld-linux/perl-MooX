#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MooX
Summary:	MooX - Using Moo and MooX:: packages the most lazy way
Name:		perl-MooX
Version:	0.101
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooX/%{pdir}-%{version}.tar.gz
# Source0-md5:	c35d73fc38aceb7edec1b5560abe4e2d
URL:		http://search.cpan.org/dist/MooX/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Data-OptList >= 0.107
BuildRequires:	perl-Import-Into >= 1.000003
BuildRequires:	perl-Module-Runtime >= 0.013
BuildRequires:	perl-Moo >= 0.091004
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Using Moo and MooX:: packages the most lazy way

=encoding utf8

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}//*.pm
%{perl_vendorlib}/MooX/
%{_mandir}/man3/*
