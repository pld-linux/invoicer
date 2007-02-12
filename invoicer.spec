Summary:	Freeware invoicing application
Summary(pl.UTF-8):	Darmowy system finansowo-księgowy
Name:		invoicer
Version:	3
Release:	1
License:	Freeware
Group:		X11/Applications
Source0:	http://www.madar.com.pl/demo/%{name}.tar.gz
# Source0-md5:	61843b1243aeff6b28870dbc99b10931
URL:		http://www.emadar.com/
Requires:	desktop-file-utils
Requires:	gdk-pixbuf >= 0.7
Requires:	gtk+ >= 1.2
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freeware financial application for making invoice.

%description -l pl.UTF-8
Program pozwalający na wystawianie faktur VAT skierowany do małych
firm, które nie prowadzą gospodarki magazynowej.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install opt/madar/invoicer.bin $RPM_BUILD_ROOT%{_bindir}/invoicer
install usr/share/applications/invoicer.desktop  $RPM_BUILD_ROOT%{_desktopdir}/invoicer.desktop
install usr/share/pixmaps/invoicer_ico.png $RPM_BUILD_ROOT%{_pixmapsdir}/invoicer_ico.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/invoicer.desktop
%{_pixmapsdir}/invoicer_ico.png
