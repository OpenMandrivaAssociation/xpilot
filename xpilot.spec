Summary:	An X Window System based multiplayer aerial combat game
Name:		xpilot
Version:	4.5.4
Release:	%mkrel 7
License:	GPL
Group:		Games/Arcade
BuildRequires:	X11-devel

URL:		http://www.xpilot.org
Source0:	ftp://ftp.xpilot.org/pub/xpilot/xpilot-%version.tar.bz2
# Source1:	%{name}-menu
Source2:	%{name}-16.png
Source3:	%{name}-32.png
Source4:	%{name}-48.png
Patch0:		%{name}-4.5.3-config.patch.bz2

BuildRequires:  xorg-x11 imake

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

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}-server.desktop
[Desktop Entry]
Type=Application
Categories=Game;ArcadeGame;
Name=Xpilot server
Comment=Fly/shoot arcade game
Exec=%{_gamesbindir}/xpilots
Icon=%{name}
EOF

cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Categories=Game;ArcadeGame;
Name=Xpilot - Requires server
Comment=Fly/shoot arcade game
Exec=%{_gamesbindir}/xpilot -join
Icon=%{name}
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt LICENSE README.txt.msub 
%doc doc
%{_gamesbindir}/*
/usr/lib/xpilot
%{_mandir}/man?/*
%{_datadir}/applications/mandriva-*.desktop
%{_miconsdir}/*
%{_liconsdir}/*
%{_iconsdir}/%{name}.png

