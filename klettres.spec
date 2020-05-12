%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Language learning program
Name:		klettres
Version:	20.04.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/klettres
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Emoticons)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Phonon4Qt5)

%description
KLettres aims to help to learn the alphabet and then to read some syllables
in different languages. It is meant to help learning the very first sounds
of a new language, for children or for adults.

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/klettres.categories
%doc COPYING COPYING.DOC COPYING.LIB AUTHORS TODO                                                      
%{_datadir}/applications/org.kde.klettres.desktop                                                                                                                                    
%{_bindir}/klettres                                                                                    
%{_sysconfdir}/xdg/klettres.knsrc   
%{_datadir}/kxmlgui5/klettres/klettresui.rc
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
%{_datadir}/klettres/data/sounds.xml
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
%lang(it) %{_datadir}/klettres/it
%lang(lt) %{_datadir}/klettres/lt
%lang(lt) %{_datadir}/klettres/lt.txt
%lang(ml) %{_datadir}/klettres/ml
%lang(nb) %{_datadir}/klettres/nb
%lang(nds) %{_datadir}/klettres/nds
%lang(nds) %{_datadir}/klettres/nds.txt
%lang(nl) %{_datadir}/klettres/nl
%lang(pt_BR) %{_datadir}/klettres/pt_BR
%lang(ru) %{_datadir}/klettres/ru
%lang(sk) %{_datadir}/klettres/sk.txt
%lang(uk) %{_datadir}/klettres/uk

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build
%find_lang klettres --with-html
