# Macro definitions
%define ver    0.1.0
%define rel    1 
%define prefix /usr

Name:      encompass
Version:   %{ver}
Release:   %{rel}
Copyright: GPL
Packager:  Rodney Dawes <dobez@fnmail.com>
URL:       http://zephyr.webhop.net/encompass.html
Source:	   http://zephyr.webhop.net/encompass-%{ver}.tar.gz
Group:     Gnome/Internet
Requires:  gnome-libs >= 1.2.0
Summary:   Encompass Gnome Web Browser

%description 
A Web Browser for Gnome using GtkHTML.

%prep

%setup

%files
%{prefix}/share/gnome/help/encompass
%{prefix}/share/pixmaps/encompass
%{prefix}/share/sounds/encompass
/etc/sound/events/encompass.soundlist
%{prefix}/share/gnome/apps/Internet/encompass.desktop
%{prefix}/bin/encompass

%changelog
