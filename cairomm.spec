%define api 1.16
%define major 1
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname -d %{name} %{api}
%define _disable_rebuild_configure 1

Summary:	C++ API for the cairo multi-platform 2D graphics library
Name:		cairomm
Version:	1.16.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://cairographics.org/cairomm
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:	doxygen
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(sigc++-3.0)

%description
This is a C++ API for the Cairo graphics library.

Cairo provides anti-aliased vector-based rendering for X. Paths
consist of line segments and cubic splines and can be rendered at any
width with various join and cap styles. All colors may be specified
with optional translucence (opacity/alpha) and combined using the
extended Porter/Duff compositing algebra as found in the X Render
Extension.

%package -n %{libname}
Summary:	Cairomm - multi-platform 2D graphics library
Group:		System/Libraries

%description -n %{libname}
This is a C++ API for the Cairo graphics library.

Cairo provides anti-aliased vector-based rendering for X. Paths
consist of line segments and cubic splines and can be rendered at any
width with various join and cap styles. All colors may be specified
with optional translucence (opacity/alpha) and combined using the
extended Porter/Duff compositing algebra as found in the X Render
Extension.

%package -n %{devname}
Summary:	Development files for Cairomm library
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This is the development package for %{name}.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libcairomm-%{api}.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/doc/cairomm-%{api}
%doc AUTHORS MAINTAINERS NEWS README
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/%{name}-%{api}/
%dir %{_libdir}/%{name}-%{api}/include/
%{_libdir}/%{name}-%{api}/include/*.h
%doc %{_datadir}/devhelp/books/%{name}-%{api}/

