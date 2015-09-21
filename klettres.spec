Summary:	Language learning program
Name:		klettres
Version:	15.08.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/klettres
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
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

%files
%doc COPYING COPYING.DOC COPYING.LIB AUTHORS TODO                                                      
%doc %{_docdir}/HTML/en/klettres                                                                       
%{_datadir}/applications/org.kde.klettres.desktop                                                                                                                                    
%{_bindir}/klettres                                                                                    
%{_sysconfdir}/xdg/klettres.knsrc   
%{_datadir}/kxmlgui5/klettres/klettresui.rc
%{_datadir}/appdata/klettres.appdata.xml                                                               
%{_datadir}/config.kcfg/klettres.kcfg                                                                  
%{_iconsdir}/*/*/apps/klettres.* 
%{_datadir}/klettres/icons/hicolor/*/actions/klettres_* 
%{_datadir}/klettres/pics/*
%{_datadir}/klettres/sk.txt
%{_datadir}/klettres/hu.txt
%{_datadir}/klettres/es.txt
%{_datadir}/klettres/nds.txt
%{_datadir}/klettres/fr/syllab/ad-*
%{_datadir}/klettres/fr/sounds.xml
%{_datadir}/klettres/fr/alpha/a-*
%{_datadir}/klettres/en/syllab/*
%{_datadir}/klettres/en/sounds.xml
%{_datadir}/klettres/en/alpha/*
%{_datadir}/klettres/de.txt
%{_datadir}/klettres/data/sounds.xml
%{_datadir}/klettres/da.txt
%{_datadir}/klettres/cs.txt

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build

