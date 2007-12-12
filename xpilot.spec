Summary:	An X Window System based multiplayer aerial combat game
Name:		xpilot
Version:	4.5.4
Release:	%mkrel 4
License:	GPL
Group:		Games/Arcade
BuildRequires:	XFree86-devel

URL:		http://www.xpilot.org
Source0:	ftp://ftp.xpilot.org/pub/xpilot/xpilot-%version.tar.bz2
# Source1:	%{name}-menu
Source2:	%{name}-16.png
Source3:	%{name}-32.png
Source4:	%{name}-48.png
Patch0:		%{name}-4.5.3-config.patch.bz2

BuildRequires:  xorg-x11

BuildRoot:	%{_tmppath}/%{name}-root

%description
Xpilot is an X Window System based multiplayer game of aerial combat.

The object of the game is to shoot each other down, or you can use the race 
mode to just fly around.

Xpilot resembles the Commodore 64 Thrust game, which is similar to Atari's
Gravitar and Asteriods (note: this is not misspelled).

Unless you already have an xpilot server on your network, you'll need to set up
the server on one machine, and then set up xpilot clients on all of the 
players' machines.

%prep

%setup -q
%patch0 -p0 

%build
xmkmf
%make Makefiles
%make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std install.man INSTBINDIR=%{_gamesbindir}

install -m644 %SOURCE2 -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %SOURCE3 -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %SOURCE4 -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,6}

# scheesh. cvs files.
find doc -name '.cvs*' | xargs rm -f {} \;

(cd $RPM_BUILD_ROOT
mkdir -p ./%{_menudir}
cat > ./%{_menudir}/%{name} <<EOF
?package(%{name}):\
	needs="text"\
	section="Amusement/Arcade"\
	title="Xpilot server"\
	longtitle="Fly/shoot arcade game"\
	command="%{_gamesbindir}/xpilots"\
	icon="%{name}.png"
?package(%{name}):\
  	needs="%{name}"\
	section="Amusement/Arcade"\
	title="Xpilot - Requires server"\
	longtitle="Fly/shoot arcade game"\
	command="%{_gamesbindir}/xpilot -join"\
	icon="%{name}.png"
EOF
)

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt LICENSE README.txt.msub 
%doc doc
%{_gamesbindir}/*
%{_libdir}/xpilot
%{_mandir}/man?/*
%{_menudir}/*
%{_miconsdir}/*
%{_liconsdir}/*
%{_iconsdir}/%{name}.png
%_prefix/X11R6/lib/X11/doc/html/*

