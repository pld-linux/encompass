Summary:	Encompass Gnome Web Browser
Name:		encompass
Version:	0.1.0
Release:	1
License:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	http://zephyr.webhop.net/%{name}-%{version}.tar.gz
URL:		http://zephyr.webhop.net/encompass.html
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description 
A Web Browser for Gnome using GtkHTML.

%prep
%setup -q

%build

%install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/encompass
%{_datadir}/gnome/help/encompass
%{_datadir}/pixmaps/encompass
%{_datadir}/sounds/encompass
%{_sysconfdir}/sound/events/encompass.soundlist
%{_applnkdir}/Network/WWW/encompass.desktop
