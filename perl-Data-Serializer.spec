#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	Serializer
Summary:	Modules that serialize data structures
Summary(pl):	Modu³y do serializacji struktur danych
Name:		perl-%{pdir}-%{pnam}
Version:	0.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c09874b1892e3b70ac11f2900e7a9a4e
URL:		http://search.cpan.org/dist/Data-Serializer/
BuildRequires:	perl-Data-Dumper >= 2.08
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-IO-File
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a unified interface to the various serializing modules
currently available. Adds the functionality of both compression and
encryption.

%description -l pl
Dostarcza zunifikowany interfejs do ró¿nych modu³ów serializacji danych.
Posiada wsparcie zarówno dla kompresji jak i szyfrowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/Serializer.pm
%{perl_vendorlib}/Data/Serializer/
%{_mandir}/man3/*
