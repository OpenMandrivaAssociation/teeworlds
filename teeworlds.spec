Name:           teeworlds
Version:        0.5.0
Release:        5%{?dist}
Summary:        Online multi-player platform 2D shooter

Group:          Amusements/Games
License:        Teeworlds
URL:            http://www.teeworlds.com/
Source0:        http://www.teeworlds.com/files/%{name}-%{version}-src.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
Patch0:         %{name}-datadir.patch
Patch1:         %{name}-extlibs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# BuildRequires:  mesa-libGLU-devel
# BuildRequires:  bam = 0.0.%{version}
BuildRequires:  python-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  zlib-devel
# BuildRequires:  libglfw-devel
# BuildRequires:  wavpack-devel
BuildRequires:  portaudio-devel
# BuildRequires:  pnglite-devel
Requires:       %{name}-data
   

%description
The game features cartoon-themed graphics and physics, 
and relies heavily on classic shooter weaponry and gameplay. 
The controls are heavily inspired by the FPS genre of computer games. 

%package        server
Summary:        Server for %{name}
Group:          Amusements/Games
Requires:       %{name}-data


%description    server
Data for %{name}, an online multi-player platform 2D shooter. 

%package        data
Summary:        Data-files for %{name}
Group:          Amusements/Games


%description    data
Data-files for %{name}, an online multi-player platform 2D shooter.


%prep
%setup -q -n %{name}-%{version}-src

#patch0 -p1 -b .datadir
#patch1 -p1 -b .extlibs
# rm -rf src/engine/external

iconv -f iso-8859-1 -t utf-8 readme.txt > readme.txt.utf8
sed -i 's|\r$||g' readme.txt.utf8
touch -c -r readme.txt readme.txt.utf8
mv readme.txt.utf8 readme.txt

%build
# sed 's|-D__OPTFLAGS__|%{optflags}|' -i default.bam
bam -v release


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
                     %if 0%{?rhel}
                     --vendor="" \
                     %endif
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


