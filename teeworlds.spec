Name:           teeworlds
Version:        0.5.2
Release:        %mkrel 2
Summary:        Online multi-player platform 2D shooter

Group:          Games/Arcade
License:        Teeworlds
URL:            http://www.teeworlds.com/
Source0:        http://www.teeworlds.com/files/%{name}-%{version}-src.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
Patch1:         %{name}-0.5.0-extlibs.patch
Patch2:         %{name}-0.5.0-optflags.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  mesaglut-devel
BuildRequires:  bam >= 0.2.0
BuildRequires:  python-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  zlib-devel
BuildRequires:  libwavpack-devel
BuildRequires:  pnglite-devel
BuildRequires:  SDL-devel
BuildRequires:  desktop-file-utils
Requires:       %{name}-data
   
%description
The game features cartoon-themed graphics and physics, 
and relies heavily on classic shooter weaponry and gameplay. 
The controls are heavily inspired by the FPS genre of computer games. 

%package        server
Summary:        Server for %{name}
Group:          Games/Arcade
Requires:       %{name}-data

%description    server
Data for %{name}, an online multi-player platform 2D shooter. 

%package        data
Summary:        Data-files for %{name}
Group:          Games/Arcade

%description    data
Data-files for %{name}, an online multi-player platform 2D shooter.

%prep
%setup -q -n %{name}-%{version}-src
rm -rf src/engine/external

%patch1 -p1 -b .extlibs
%patch2 -p1 -b .optflags

iconv -f iso-8859-1 -t utf-8 readme.txt |sed 's|\r||g' > readme.txt.utf8
touch -c -r readme.txt readme.txt.utf8
mv readme.txt.utf8 readme.txt

%build
CFLAGS="%{optflags}" bam -v release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}/data
mkdir -p %{buildroot}%{_datadir}/pixmaps

install -D -m 0755 %{name} \
        %{buildroot}%{_bindir}/%{name}

install -D -m 0755 %{name}_srv \
        %{buildroot}%{_bindir}/%{name}-srv

cp -pr data/* \
   %{buildroot}%{_datadir}/%{name}

install -p -m 0644 %{SOURCE1} \
        %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
     --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
     %{SOURCE2}

%clean
rm -rf %{buildroot}

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

