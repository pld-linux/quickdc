Summary:	QuickDC - QT Direct Connect client
Summary(pl):	QuickDC - klient Direct Connecta oparty o QT
Name:		quickdc
Version:	0.0.5
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}-alpha-src.tar.bz2
URL:		http://quickdc.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
QT Direct Connect client.

%description -l pl
Klient Direct Connecta u¿ywaj±cy biblioteki QT.

%prep
%setup -q -n %{name}

%build
#cp -f /usr/share/automake/config.* .
#%{__make} -f Makefile.dist
%configure2_13 

%{__make} \
	MOC=%{_bindir}/moc \
	UIC=%{_bindir}/uic \
	all_includes="-I%{_includedir}/qt -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/

%{__make} DESTDIR=$RPM_BUILD_ROOT install

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
