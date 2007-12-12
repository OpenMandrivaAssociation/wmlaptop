%define name	wmlaptop
%define version	1.4
%define release 2mdk

Name: 	 	%{name}
Summary: 	Laptop info docklet for WindowMaker
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://wmlaptop.sourceforge.net/
License:	GPL
Group:		Graphical desktop/WindowMaker
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	XFree86-devel ImageMagick libxpm-devel libxpm4

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
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="WMLaptop" longtitle="Laptop status docklet" section="System/Monitoring"
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

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc AUTHORS BUGS CHANGELOG README* THANKS
%{_bindir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
