Name:		golem
Summary:	X11 window manager
Summary(pl):	Window menad¿er dla X11
Version:	0.0.4
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://telia.dl.sourceforge.net/sourceforge/golem/%{name}-%{version}.tar.gz
URL:		http://golem.sf.net/
BuildRequires:	XFree86-devel
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define			_prefix		/usr/X11R6/

%description
Golem is a litle X11 window manager

%description -l pl
Golem jest ma³ym i prostym menad¿erem okien dla X11

%prep
%setup -q

%build
%configure2_13 --enable-sound --enable-xinerama
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/golem/plugins/
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_datadir}/golem
install build-bin/* $RPM_BUILD_ROOT%{_bindir}/
install build-plugin/* $RPM_BUILD_ROOT%{_libdir}/golem/plugins/
install doc/golem.1.gz $RPM_BUILD_ROOT%{_mandir}/man1
cp -r sample.golem/* $RPM_BUILD_ROOT%{_datadir}/golem
cp sample.golem/golemrc $RPM_BUILD_ROOT%{_datadir}/golem

gzip -9nf PLUGINS README THEMES TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_mandir}/man1/golem.1.gz
%{_datadir}/golem/*/*/*/
%{_datadir}/golem/golemrc
