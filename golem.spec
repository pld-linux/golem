#
# TODO:
# - add desktop file.
#
Name:		golem
Summary:	X11 window manager
Summary(pl):	Menad¿er okien dla X11
Version:	0.0.4
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://telia.dl.sourceforge.net/sourceforge/golem/%{name}-%{version}.tar.gz
URL:		http://golem.sf.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/

%description
Golem is a litle X11 window manager.

%description -l pl
Golem jest ma³ym i prostym menad¿erem okien dla X11.

%prep
%setup -q

%build
aclocal
%{__autoconf}
cp -f /usr/share/automake/config.* .
%configure \
	--enable-sound \
	--enable-xinerama
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/golem/plugins} \
	$RPM_BUILD_ROOT{%{_mandir}/man1,%{_datadir}/golem}

install build-bin/* $RPM_BUILD_ROOT%{_bindir}
install build-plugin/* $RPM_BUILD_ROOT%{_libdir}/golem/plugins
install doc/golem.1.gz $RPM_BUILD_ROOT%{_mandir}/man1

cp -r sample.golem/* $RPM_BUILD_ROOT%{_datadir}/golem
cp sample.golem/golemrc $RPM_BUILD_ROOT%{_datadir}/golem

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PLUGINS README THEMES TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_mandir}/man1/golem.1*
%{_datadir}/golem
