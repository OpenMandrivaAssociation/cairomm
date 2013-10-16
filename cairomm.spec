%define api	1.0
%define major	1
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname -d %{name} %{api}

Summary:	C++ API for the cairo multi-platform 2D graphics library
Name:		cairomm
Version:	1.10.0
Release:	5
License:	LGPLv2+
Group:		System/Libraries
Url:		http://cairographics.org/cairomm
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.gz

BuildRequires:	doxygen
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(sigc++-2.0)

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
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libcairomm-%{api}.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/doc/cairomm-%{api}
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/%{name}-%{api}/
%dir %{_libdir}/%{name}-%{api}/include/
%{_libdir}/%{name}-%{api}/include/*.h
%doc %{_datadir}/devhelp/books/%{name}-%{api}/

