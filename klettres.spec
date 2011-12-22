Name: klettres
Summary: Language learning program
Version: 4.7.95
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 LGPLv2 GFDL
URL: http://edu.kde.org/klettres
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}

%description
KLettres aims to help to learn the alphabet and then to read some syllables
in different languages. It is meant to help learning the very first sounds
of a new language, for children or for adults.

%files
%_kde_appsdir/klettres
%_kde_bindir/klettres
%_kde_iconsdir/*/*/apps/klettres.*
%_kde_datadir/applications/kde4/klettres.desktop
%_kde_datadir/config.kcfg/klettres.kcfg
%_kde_datadir/config/klettres.knsrc
%doc COPYING COPYING.DOC COPYING.LIB AUTHORS TODO
%doc %_kde_docdir/HTML/en/klettres

#----------------------------------------------------------------------

%prep
%setup -q
%apply_patches


%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

