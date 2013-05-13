%define name	wmlaptop
%define version	1.4
%define release %mkrel 8

Name: 	 	%{name}
Summary: 	Laptop info docklet for WindowMaker
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://wmlaptop.sourceforge.net/
License:	GPL
Group:		Graphical desktop/WindowMaker
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	imagemagick

%description
wmlaptop is a WindowMaker dockapp able to satisfy any requirements of a linux
user with a laptop. The smartest should have easily guessed that wmlaptop
includes an advanced battery information interface, including an indicator
which estimates the remaining battery autonomy. Anyway this is only one of the
useful functions provided:

* Battery estimated time remaining
* Multi Batteries support
* Battery remaining charge (visual and percent)
* Auto-Frequency Scaling
* Manual Frequency Scaling
* 0-100 Cpu Load indicator
* APM and ACPI support
* sysfs and /proc filesystems support
* Kernel 2.6 series fully compatible
* Visual support for multiple batteries
* "Visual and audio" alarm on Low-Battery
* Auto shutdown on Low-Battery
* Easy screen saver starter
* Console executable

%prep
%setup -q
chmod 644 README*

%build
%make CFLAGS="$RPM_OPT_FLAGS"
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
install -m 4755 src/%name $RPM_BUILD_ROOT/%_bindir/

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=WMLaptop
Comment=Laptop status docklet
Categories=System;Monitor;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 img/screenshot_1.jpeg $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 img/screenshot_1.jpeg $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 img/screenshot_1.jpeg $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS BUGS CHANGELOG README* THANKS
%{_bindir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.4-8mdv2011.0
+ Revision: 634818
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.4-7mdv2010.0
+ Revision: 434873
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.4-6mdv2009.0
+ Revision: 262056
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.4-5mdv2009.0
+ Revision: 256202
- rebuild
- fix no-buildroot-tag

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 1.4-3mdv2008.1
+ Revision: 135790
- auto-convert XDG menu entry
- fix xpm-devel BR on x86_64
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- use %%mkrel
- import wmlaptop


* Fri Apr 14 2006 Udo Rader <udo.rader@bestsolution.at> 1.4-2mdk
- added libxpm* as buildreq in order to hopefully fix x86_64 build 
  problems

* Wed Apr 05 2005 Udo Rader <udo.rader@bestsolution.at> 1.4-1mdk
- new upstream version
- made it suid root in order to allow writing to /sys/... files

* Mon Jun 7 2004 Austin Acton <austin@mandrake.org> 1.3-1mdk
- initial package
