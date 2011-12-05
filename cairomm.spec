%define api 1.0
%define major       1
%define libname        %mklibname %name %{api}_%{major}
%define libnamedev     %mklibname -d %name %{api}

Summary: C++ API for the cairo multi-platform 2D graphics library
Name:		cairomm
Version:	1.10.2
Release:	2
Source0: http://cairographics.org/releases/%{name}-%{version}.tar.gz
License: LGPLv2+
Group: System/Libraries
Url: http://cairographics.org/cairomm
BuildRequires: cairo-devel
BuildRequires: sigc++2.0-devel
BuildRequires: doxygen

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

%package -n %{libnamedev}
Summary:	Development files for Cairomm library
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	lib%{name}%{api}-devel = %{version}-%{release}
Obsoletes:      %mklibname -d %{name} 1.0_1

%description -n %{libnamedev}
This is a C++ API for the Cairo graphics library.

Cairo provides anti-aliased vector-based rendering for X. Paths
consist of line segments and cubic splines and can be rendered at any
width with various join and cap styles. All colors may be specified
with optional translucence (opacity/alpha) and combined using the
extended Porter/Duff compositing algebra as found in the X Render
Extension.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name \*.la|xargs rm -f

%files -n %{libname}
%{_libdir}/libcairomm-%{api}.so.%{major}*

%files -n %libnamedev}
%doc %{_datadir}/doc/cairomm-%{api}
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/%{name}-%{api}/
%dir %{_libdir}/%{name}-%{api}/include/
%{_libdir}/%{name}-%{api}/include/*.h
%{_datadir}/devhelp/books/%{name}-%{api}/
