Summary:	Encompass Gnome Web Browser
Summary(pl):	Przeglądarka WWW dla Gnome
Name:		encompass
Version:	0.4.2
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://prdownloads.sourceforge.net/encompass/%{name}-%{version}.tar.gz
URL:		http://dobey.free.fr/encompass/
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description 
A Web Browser for Gnome using GtkHTML.

%description -l pl
Przeglądarka WWW dla Gnome korzystająca z GtkHTML.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/encompass
%{_datadir}/gnome/help/encompass
%{_pixmapsdir}/encompass
%{_datadir}/sounds/encompass
%{_sysconfdir}/sound/events/encompass.soundlist
%{_applnkdir}/Network/WWW/encompass.desktop
