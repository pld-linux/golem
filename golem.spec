#
# TODO:
# - add desktop file.
#
Summary:	X11 window manager
Summary(pl):	Zarz±dca okien dla X11
Name:		golem
Version:	0.0.5
Release:	2
License:	GPL
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/golem/%{name}-%{version}.tar.gz
# Source0-md5:	09f503f5c6e621e5029e845682a8c941
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-etc_dir.patch
URL:		http://golem.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Golem is a litle X11 window manager.

%description -l pl
Golem jest ma³ym i prostym zarz±dc± okien dla X11.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.* .
%configure \
	--enable-sound \
	--enable-xinerama
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/golem/plugins} \
	$RPM_BUILD_ROOT{%{_mandir}/man1,%{_datadir}/{golem,xsessions}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

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
%{_datadir}/golem
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/golem.1*
