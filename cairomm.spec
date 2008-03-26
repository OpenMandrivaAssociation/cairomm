%define name cairomm
%define version 1.4.6
%define release %mkrel 2
%define api 1.0
%define major       1
%define libname        %mklibname %name %{api}_%{major}
%define libnamedev     %mklibname -d %name %{api}

Summary: C++ API for the cairo multi-platform 2D graphics library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://cairographics.org/releases/%{name}-%{version}.tar.gz
#gw: fix for a small cairo API change
Patch: cairomm-1.4.6-new-cairo.patch
License: LGPL
Group: System/Libraries
Url: http://cairographics.org/cairomm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cairo-devel
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
Requires:	%{libname} = %version
Provides:	%{name}-devel = %version-%release
Provides:	lib%{name}-devel = %version-%release
Provides:	lib%{name}%api-devel = %version-%release
Obsoletes:      %mklibname -d %name 1.0_1

%description -n %libnamedev
This is a C++ API for the Cairo graphics library.

Cairo provides anti-aliased vector-based rendering for X. Paths
consist of line segments and cubic splines and can be rendered at any
width with various join and cap styles. All colors may be specified
with optional translucence (opacity/alpha) and combined using the
extended Porter/Duff compositing algebra as found in the X Render
Extension.

%prep
%setup -q
%patch -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%makeinstall_std
mv %buildroot%_datadir/doc/libcairomm-1.0/* installed-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n %{libname} -p /sbin/ldconfig
%postun	-n %{libname} -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%_libdir/libcairomm-%{api}.so.%{major}*

%files -n %libnamedev
%defattr(644,root,root,755)
%doc installed-docs/*
%_libdir/lib*.so
%_libdir/lib*.a
%attr(644,root,root) %_libdir/lib*.la
%_includedir/*
%_libdir/pkgconfig/*.pc
