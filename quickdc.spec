Summary:	QuickDC - Qt Direct Connect client
Summary(pl.UTF-8):	QuickDC - klient Direct Connecta oparty o Qt
Name:		quickdc
Version:	0.0.6
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/quickdc/%{name}-%{version}-alpha-src.tar.bz2
# Source0-md5:	91d9186034b3944f0de6c20ec69a4014
URL:		http://quickdc.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Direct Connect client.

%description -l pl.UTF-8
Klient Direct Connecta używający biblioteki Qt.

%prep
%setup -q -n %{name}-%{version}-alpha-src

%build
#cp -f /usr/share/automake/config.* .
%{__make} -f Makefile.dist
%configure

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
