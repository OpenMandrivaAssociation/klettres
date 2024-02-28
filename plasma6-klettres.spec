#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Language learning program
Name:		plasma6-klettres
Version:	24.02.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/klettres
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/klettres/-/archive/%{gitbranch}/klettres-%{gitbranchd}.tar.bz2#/klettres-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/klettres-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  qt6-qtbase-theme-gtk3

%description
KLettres aims to help to learn the alphabet and then to read some syllables
in different languages. It is meant to help learning the very first sounds
of a new language, for children or for adults.

%files -f klettres.lang
%{_datadir}/qlogging-categories6/klettres.categories
%{_datadir}/applications/org.kde.klettres.desktop                                                                                                                                    
%{_bindir}/klettres                                                                                    
%{_datadir}/knsrcfiles/klettres.knsrc   
%{_datadir}/metainfo/org.kde.klettres.appdata.xml                                                               
%{_datadir}/config.kcfg/klettres.kcfg                                                                  
%{_iconsdir}/*/*/apps/klettres.* 
%{_datadir}/klettres/icons/hicolor/*/actions/klettres_* 
%{_datadir}/klettres/pics/*
%{_datadir}/klettres/fr/syllab/ad-*
%{_datadir}/klettres/fr/sounds.xml
%{_datadir}/klettres/fr/alpha/a-*
%{_datadir}/klettres/en/syllab/*
%{_datadir}/klettres/en/sounds.xml
%{_datadir}/klettres/en/alpha/*
%lang(ar) %{_datadir}/klettres/ar
%lang(cs) %{_datadir}/klettres/cs
%lang(cs) %{_datadir}/klettres/cs.txt
%lang(da) %{_datadir}/klettres/da
%lang(da) %{_datadir}/klettres/da.txt
%lang(de) %{_datadir}/klettres/de
%lang(de) %{_datadir}/klettres/de.txt
%lang(en_GB) %{_datadir}/klettres/en_GB
%lang(es) %{_datadir}/klettres/es
%lang(es) %{_datadir}/klettres/es.txt
%lang(he) %{_datadir}/klettres/he
%lang(hu) %{_datadir}/klettres/hu
%lang(hu) %{_datadir}/klettres/hu.txt
%lang(id) %{_datadir}/klettres/id
%lang(it) %{_datadir}/klettres/it
%lang(lt) %{_datadir}/klettres/lt
%lang(ml) %{_datadir}/klettres/ml
%lang(nb) %{_datadir}/klettres/nb
%lang(nds) %{_datadir}/klettres/nds
%lang(nds) %{_datadir}/klettres/nds.txt
%lang(nl) %{_datadir}/klettres/nl
%lang(nn) %{_datadir}/klettres/nn
%lang(pt_BR) %{_datadir}/klettres/pt_BR
%lang(ru) %{_datadir}/klettres/ru
%lang(sk) %{_datadir}/klettres/sk.txt
%lang(tn) %{_datadir}/klettres/tn
%lang(uk) %{_datadir}/klettres/uk

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n klettres-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build
%find_lang klettres --with-html
