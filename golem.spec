#
# TODO:
# - add desktop file.
#
Summary:	X11 window manager
Summary(pl.UTF-8):	Zarządca okien dla X11
Name:		golem
Version:	0.0.6
Release:	1
License:	BSD-like
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/golem/%{name}-%{version}.tar.bz2
# Source0-md5:	cc43633d68f3b84ae4fafedab41e4945
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-etc_dir.patch
Patch1:		%{name}-asm_system.patch
URL:		http://golem.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	esound-devel
BuildRequires:	flex
BuildRequires:	libltdl-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXpm-devel
Requires:	libltdl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Golem is a litle X11 window manager.

%description -l pl.UTF-8
Golem jest małym i prostym zarządcą okien dla X11.

%prep
%setup -q
#%%patch0 -p1
%patch -P1 -p1

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

install src/golem $RPM_BUILD_ROOT%{_bindir}
install build-bin/* $RPM_BUILD_ROOT%{_bindir}
install build-plugin/* $RPM_BUILD_ROOT%{_libdir}/golem/plugins
install doc/golem.1.gz $RPM_BUILD_ROOT%{_mandir}/man1

cp -r sample.golem/* $RPM_BUILD_ROOT%{_datadir}/golem
cp sample.golem/golemrc $RPM_BUILD_ROOT%{_datadir}/golem

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README README.plugins README.themes TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/golem
%{_datadir}/golem
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/golem.1*
