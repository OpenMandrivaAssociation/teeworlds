Name:		teeworlds
Version:	0.6.1
Release:	%mkrel 1
Summary:	Online multi-player platform 2D shooter
Group:		Games/Arcade
License:	Teeworlds
URL:		http://www.teeworlds.com/
Source0:	http://www.teeworlds.com/files/%{name}-%{version}-source.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
Patch1:		%{name}-0.6.1-extlibs.patch
BuildRequires:	SDL-devel
BuildRequires:	bam >= 0.4.0
BuildRequires:	desktop-file-utils
BuildRequires:	libwavpack-devel
BuildRequires:	mesaglu-devel
BuildRequires:	pnglite-devel
BuildRequires:	python-devel
BuildRequires:	zlib-devel
BuildRequires:	freetype2-devel
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
%__rm -rf src/engine/external

%patch1 -p1 -b .extlibs

iconv -f iso-8859-1 -t utf-8 readme.txt |sed 's|\r||g' > readme.txt.utf8
touch -c -r readme.txt readme.txt.utf8
%__mv readme.txt.utf8 readme.txt

%build
CFLAGS="%{optflags}" bam -v release

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/%{name}/data
%__mkdir -p %{buildroot}%{_datadir}/pixmaps
%__install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
%__install -D -m 0755 %{name}_srv %{buildroot}%{_bindir}/%{name}-srv
%__cp -pr data/* %{buildroot}%{_datadir}/%{name}/data
%__install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
     --dir=%{buildroot}%{_datadir}/applications \
     %{SOURCE2}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc readme.txt license.txt
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files data
%defattr(-,root,root,-)
%{_datadir}/%{name}/

%files server
%defattr(-,root,root,-)
%doc readme.txt license.txt
%{_bindir}/%{name}-srv


