Summary:	Encompass Gnome Web Browser
Summary(pl):	Przegl±darka WWW dla Gnome
Name:		encompass
Version:	0.4.4
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://encompass.sourceforge.net/%{name}-%{version}.tar.gz
URL:		http://encompass.sourceforge.net/
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	neon-devel >= 0.15.0
BuildRequires:	gnome-print-devel >= 0.24
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gal-devel >= 0.7
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A Web Browser for Gnome using GtkHTML.

%description -l pl
Przegl±darka WWW dla Gnome korzystaj±ca z GtkHTML.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/encompass
%{_datadir}/gnome/help/encompass
%{_pixmapsdir}/encompass
%{_datadir}/sounds/encompass
%{_sysconfdir}/sound/events/encompass.soundlist
%{_applnkdir}/Network/WWW/encompass.desktop
