Name:		teeworlds
Version:	0.6.1
Release:	3
Summary:	Online multi-player platform 2D shooter
Group:		Games/Arcade
License:	Teeworlds
URL:		https://www.teeworlds.com/
Source0:	http://www.teeworlds.com/files/%{name}-%{version}-source.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
Patch1:		%{name}-0.6.1-extlibs.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	bam >= 0.4.0
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pnglite-devel
BuildRequires:	python-devel
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(freetype2)
Requires:	%{name}-data

%description
The game features cartoon-themed graphics and physics,
and relies heavily on classic shooter weaponry and gameplay.
The controls are heavily inspired by the FPS genre of computer games.

%package server
Summary:	Server for %{name}
Group:		Games/Arcade
Requires:	%{name}-data

%description	server
The server daemon for %{name}, an online multi-player platform 2D shooter,
which allows you to host online %{name} games.

%package	data
Summary:	Data-files for %{name}
Group:		Games/Arcade
Requires:	%{name}

%description    data
Data-files for %{name}, an online multi-player platform 2D shooter.

%prep
%setup -q -n teeworlds-b177-r50edfd37-source
rm -rf src/engine/external

%patch1 -p1 -b .extlibs

iconv -f iso-8859-1 -t utf-8 readme.txt |sed 's|\r||g' > readme.txt.utf8
touch -c -r readme.txt readme.txt.utf8
mv readme.txt.utf8 readme.txt

%build
CFLAGS="%{optflags}" bam -v release

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/data
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0755 %{name}_srv %{buildroot}%{_bindir}/%{name}-srv
cp -pr data/* %{buildroot}%{_datadir}/%{name}/data
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
     --dir=%{buildroot}%{_datadir}/applications \
     %{SOURCE2}

%files
%doc readme.txt license.txt
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files data
%{_datadir}/%{name}/

%files server
%doc readme.txt license.txt
%{_bindir}/%{name}-srv

%changelog
* Mon Jan 30 2012 Andrey Bondrov <abondrov@mandriva.org> 0.6.1-1
+ Revision: 769903
- New version 0.6.1, update patches and BuildRequires

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Mon Dec 21 2009 Samuel Verschelde <stormi@mandriva.org> 0.5.2-1mdv2010.1
+ Revision: 480956
- new version 0.5.2
- dropped 1 hunk from teeworlds-0.5.0-extlibs.patch (merged upstream)

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.5.1-2mdv2010.0
+ Revision: 445414
- rebuild

* Fri Mar 13 2009 trem <trem@mandriva.org> 0.5.1-1mdv2009.1
+ Revision: 354739
- update to 0.5.1
- remove patch teeworlds-0.5.0-segv.patch (added upstream)

* Thu Mar 12 2009 trem <trem@mandriva.org> 0.5.0-2mdv2009.1
+ Revision: 354358
+ rebuild (emptylog)

* Wed Jan 28 2009 Olivier Thauvin <nanardon@mandriva.org> 0.5.0-1mdv2009.1
+ Revision: 334979
- fix group
- don't use jpackage macros
- buildrequires
- initial mdv release

  + trem <trem@mandriva.org>
    - import teeworlds


* Fri Jan 02 2009 Simon Wesp <cassmodiah@fedoraproject.org> 0.4.3-5
- Remove requires from subpackage 'data'
- Correct description 

* Thu Jan 01 2009 Simon Wesp <cassmodiah@fedoraproject.org> 0.4.3-4
- Drop desktop-file and icon for subpackage 'server'
- Honor timestamp for converted file
- Add and correct Lubomir's changes
- Remove all comments
- Correct License-Tag (again)
- Add datadir patch

* Wed Dec 31 2008 Lubomir Rintel <lkundrak@v3.sk> 0.4.3-3
- Outsource the dependencies (extlib-patch)
- Use optflags

* Thu Sep 18 2008 Simon Wesp <cassmodiah@fedoraproject.org> 0.4.3-2
- Recheck and conform licensing and list it in a comment
- Correct BuildRequires

* Sat Sep 13 2008 Simon Wesp <cassmodiah@fedoraproject.org> 0.4.3-1
- Initial Release

