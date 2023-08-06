%define api 1.0
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name
%define girname	%mklibname %{name}-gir %{api}

Name:           gitg
Version:        44
Release:        1
Summary:        GTK+ graphical interface for the git revision control system

Group:          Graphical desktop/GNOME
License:        GPLv2+
URL:            http://trac.novowork.com/gitg
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
#Patch0:         gitg-fix-build-with-libgit2.patch

BuildRequires:  dbus-devel
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libdazzle-1.0)
BuildRequires:	pkgconfig(libgit2-glib-1.0)
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(gtkspell3-3.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(webkit2gtk-4.0)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	pkgconfig(gcr-base-3)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  intltool
BuildRequires:  meson
Requires:       git
Requires:	gsettings-desktop-schemas
Requires:	typelib(Peas)
Requires:	typelib(PeasGtk)
Requires: %libname = %version-%release

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
Requires:	%{girname} = %{version}-%{release}
Provides: libgitg-devel = %version-%release

%description -n %develname
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires: %libname = %version-%release

%description -n %{girname}
GObject Introspection interface description for %{name}.


%prep
%setup -q
#patch0 -p0


%build
# For some reason (unknown to me) gitg crashing at launch without any details. 
# Is not possible to run package compiled with Clang 8 or 9. Only GCC fix it (angry)
export CC=gcc
export CXX=g++
%meson
%meson_build

%install
%meson_install
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS NEWS README.md

%{_bindir}/gitg
%_datadir/icons/hicolor/*/apps/*
%{_datadir}/gitg
%{_libdir}/gitg
%_datadir/glib-2.0/schemas/org.gnome.gitg.gschema.xml
%{_mandir}/man1/gitg.1*
%{_datadir}/metainfo/org.gnome.gitg.appdata.xml
%{python3_sitelib}/gi/overrides/*

%{_datadir}/applications/org.gnome.gitg.desktop

%files -n %libname
%_libdir/libgitg-%api.so.%{major}*
%_libdir/libgitg-ext-%api.so.%{major}*

%files -n %develname
%doc ChangeLog
%{_includedir}/libgitg-%api/*/*
%{_includedir}/libgitg-ext-%api/*/*
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/libgitg-ext-%{api}.so
%_libdir/pkgconfig/libgitg*-%api.pc
%_datadir/gir-1.0/*.gir
%_datadir/vala/vapi/*.vapi
%{_datadir}/glade/catalogs/gitg-glade.xml

%files -n %{girname}
%{_libdir}/girepository-1.0/*.typelib
