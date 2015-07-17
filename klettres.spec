Summary:	Language learning program
Name:		klettres
Version:	15.04.3
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

%description
KLettres aims to help to learn the alphabet and then to read some syllables
in different languages. It is meant to help learning the very first sounds
of a new language, for children or for adults.

%files
%doc COPYING COPYING.DOC COPYING.LIB AUTHORS TODO                                                      
%doc %{_docdir}/HTML/en/klettres                                                                       
%{_datadir}/applications/kde4/klettres.desktop                                                         
%{_datadir}/apps/klettres                                                                              
%{_bindir}/klettres                                                                                    
%{_datadir}/config/klettres.knsrc                                                                      
%{_datadir}/appdata/klettres.appdata.xml                                                               
%{_datadir}/config.kcfg/klettres.kcfg                                                                  
%{_iconsdir}/*/*/apps/klettres.* 

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build

