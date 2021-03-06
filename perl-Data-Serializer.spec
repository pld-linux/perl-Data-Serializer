#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Data
%define		pnam	Serializer
Summary:	Modules that serialize data structures
Summary(pl.UTF-8):	Moduły do serializacji struktur danych
Name:		perl-Data-Serializer
Version:	0.49
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31a8c3f5ab573a840b4314d327bc534a
URL:		http://search.cpan.org/dist/Data-Serializer/
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Config-General
BuildRequires:	perl-Data-Denter
#BuildRequires:	perl-Data-Taxi
BuildRequires:	perl-Digest-SHA
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-PHP-Serialization
BuildRequires:	perl-XML-Dumper
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-YAML
BuildRequires:	perl-YAML-Syck
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a unified interface to the various serializing modules
currently available. Adds the functionality of both compression and
encryption.

%description -l pl.UTF-8
Dostarcza zunifikowany interfejs do różnych modułów serializacji
danych. Posiada wsparcie zarówno dla kompresji jak i szyfrowania.

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
%dir %{perl_vendorlib}/Data/Serializer/
%{perl_vendorlib}/Data/Serializer/*.pm
%dir %{perl_vendorlib}/Data/Serializer/Config
%{perl_vendorlib}/Data/Serializer/Config/General.pm
%dir %{perl_vendorlib}/Data/Serializer/Data
%{perl_vendorlib}/Data/Serializer/Data/*.pm
%dir %{perl_vendorlib}/Data/Serializer/JSON
%{perl_vendorlib}/Data/Serializer/JSON/*.pm
%dir %{perl_vendorlib}/Data/Serializer/PHP
%{perl_vendorlib}/Data/Serializer/PHP/*.pm
%dir %{perl_vendorlib}/Data/Serializer/XML
%{perl_vendorlib}/Data/Serializer/XML/*.pm
%dir %{perl_vendorlib}/Data/Serializer/YAML
%{perl_vendorlib}/Data/Serializer/YAML/*.pm

%{_mandir}/man3/*
