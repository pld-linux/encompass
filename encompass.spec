Summary:	Encompass GNOME Web Browser
Summary(pl.UTF-8):	Przeglądarka WWW dla GNOME
Name:		encompass
Version:	0.5.99.3
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://encompass.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	a042bf72f1ecbe33ac9b219250e428c6
Patch0:		%{name}-neon-update.patch
URL:		http://encompass.sourceforge.net/
BuildRequires:	gal-devel >= 1.99
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	gtkhtml-devel >= 3.0
BuildRequires:	libelysium >= 0.99.8.1
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libxml2-devel
# 0.21.0 in vanilla version, about 0.24.0 with patch
BuildRequires:	neon-devel >= 0.24.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Web Browser for GNOME using GtkHTML.

%description -l pl.UTF-8
Przeglądarka WWW dla GNOME korzystająca z GtkHTML.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/encompass
%{_libdir}/bonobo/servers/*.server
%{_datadir}/sounds/encompass
%{_sysconfdir}/sound/events/encompass.soundlist
%{_pixmapsdir}/encompass
%{_pixmapsdir}/encompass.png
%{_desktopdir}/encompass.desktop
