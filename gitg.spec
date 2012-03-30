%define api 1.0
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name

Name:           gitg
Version:        0.2.5
Release:        %mkrel 1
Summary:        GTK+ graphical interface for the git revision control system

Group:          Graphical desktop/GNOME
License:        GPLv2+
URL:            http://trac.novowork.com/gitg
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  dbus-devel
BuildRequires:  libGConf2-devel
BuildRequires:  glib2-devel >= 1:2.26
BuildRequires:  gtk+3-devel
BuildRequires:  gtksourceview3-devel >= 3.1.3
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  intltool
Requires:       git
Requires:	%libname >= %version-%release

%description
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

%package -n %libname
Group: System/Libraries
Summary: Shared library parts of %name

%description -n %libname
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

%package -n %develname
Group: Development/C
Summary: Development library parts of %name
Requires: %libname = %version-%release
Provides: libgitg-devel = %version-%release

%description -n %develname
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

%prep
%setup -q


%build
%configure2_5x --disable-static --disable-maintainer-mode
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS NEWS README

%{_bindir}/gitg
%_datadir/icons/hicolor/*/apps/gitg*
%{_datadir}/gitg
%_datadir/glib-2.0/schemas/org.gnome.gitg.gschema.xml
%{_mandir}/man1/gitg.1*

%{_datadir}/applications/gitg.desktop

%files -n %libname
%defattr(-,root,root,-)
%_libdir/libgitg-%api.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%doc ChangeLog
%_includedir/libgitg-%api
%_libdir/libgitg-%api.so
%_libdir/pkgconfig/libgitg-%api.pc
