Summary:	An X Window System based multiplayer aerial combat game
Name:		xpilot
Version:	4.5.5
Release:	%mkrel 1
License:	GPL
Group:		Games/Arcade
URL:		http://www.xpilot.org
Source0:	http://downloads.sourceforge.net/xpilotgame/xpilot-%version.tar.bz2
# Source1:	%{name}-menu
Source2:	%{name}-16.png
Source3:	%{name}-32.png
Source4:	%{name}-48.png
Patch0:		%{name}-4.5.3-config.patch
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:  imake

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
%make CDEBUGFLAGS="%optflags" EXTRA_LDOPTIONS="%ldflags"

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



%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 4.5.5-1mdv2011.0
+ Revision: 657735
- new version 4.5.5

* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 4.5.4-9
+ Revision: 634909
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 4.5.4-8mdv2010.0
+ Revision: 435257
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 4.5.4-7mdv2009.0
+ Revision: 262686
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 4.5.4-6mdv2009.0
+ Revision: 257672
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 4.5.4-4mdv2008.1
+ Revision: 132655
- adjust file list
- fix file list for x86_64
- BR imaek
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import xpilot


* Fri Jul 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 4.5.4-4mdk
- Fix BuildRequires

* Tue Dec 07 2004 Lenny Cartier <lenny@mandrakesoft.com> 4.5.4-3mdk
- rebuild

* Tue Aug 05 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.5.4-2mdk
- rebuild
- bunzip2 icons
- move binary to %%{_gamesbindir}
- no, Buffy is more beatiful than Willow!

* Sun Jan 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 4.5.4-1mdk
- 4.5.4
- Willow is really more beautiful than Buffy, you're right Sebd.

* Mon Jun 03 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.5.3-1mdk
- 4.5.3
- update %%patch0
- png icons
- menu in spefile
- cleanup

* Wed Apr 03 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.5.0-1mdk
- 4.5.0-1mdk for general consumption.

* Sun Nov 11 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.4.3-1mdk
- 4.4.3 for general consumption.

* Thu Aug 23 2001 David BAUDENS <baudens@mandrakesoft.com> 4.3.2-2mdk
- Used new icons
- Added missing file

* Tue May  8 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 4.3.2-1mdk
- version 4.3.2

* Sat Apr 28 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.3.1-2mdk
- Compile with RPM_OPT_FLAGS.
- Install the menu with a filename called xpilot, not xpilot-menu.

* Sat Apr 28 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.3.1-1mdk
- Bump version 4.3.1 into cooker.

* Wed Mar 14 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.0-9mdk
- Explicitly include time.h in src/server/netserver.c.

* Tue Nov 28 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.0-8mdk
- use optflags.

* Fri Sep 15 2000 David BAUDENS <baudens@mandrakesoft.com> 4.2.0-7mdk
- Fix Title in Menu entry
- Complete macros

* Wed Aug 30 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.0-6mdk
- rebuild to use the new macros.

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.2.0-5mdk
- automatically added BuildRequires

* Wed May 03 2000 dam's <damien@mandrakesoft.com> 4.2.0-4mdk
- Corrected menu entry.

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 4.2.0-3mdk
- Convert gif icon to xpm.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 4.2.0-2mdk
- Added menu entry.

* Wed Mar 22 2000 dam's <damien@mandrakesoft.com> 4.2.0-1mdk
- updade to 4.2.0

* Fri Nov 5 1999 dam's <damien@mandrakesoft.com>
- Mandrake adaptation

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 4.1.0

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- add sparc
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Nov  3 1997 Otto Hammersmith <otto@redhat.com>
- made exlusivearch to i386

* Thu Oct 23 1997 Marc Ewing <marc@redhat.com>
- new version
- wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
