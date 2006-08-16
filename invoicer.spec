
Summary:	Freeware invoicing application
Summary(pl):	Darmowy system finansowo-ksiêgowy
Name:		invoicer
Version:	3
Release:	0.1
License:	Freeware
Group:		Productivity/Office/Finance
Source0:	http://www.madar.com.pl/demo/%{name}.tar.gz
# Source0-md5:	61843b1243aeff6b28870dbc99b10931
URL:		http://www.emadar.com
Requires:	desktop-file-utils
Requires:	gdk-pixbuf
Requires:	gtk+
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freeware financial application for making invoice.

%description -l pl
Program pozwalaj±cy na wystawianie faktur VAT skierowany do ma³ych
firm, które nie prowadz± gospodarki magazynowej.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/,%{_pixmapsdir}}

mv opt/madar/invoicer.bin opt/madar/invoicer
install opt/madar/invoicer $RPM_BUILD_ROOT%{_bindir}
install usr/share/applications/invoicer.desktop  $RPM_BUILD_ROOT%{_desktopdir}/invoicer.desktop
install usr/share/pixmaps/invoicer_ico.png $RPM_BUILD_ROOT%{_pixmapsdir}/invoicer_ico.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/invoicer.desktop
%{_pixmapsdir}/invoicer_ico.png
