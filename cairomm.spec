%define name cairomm
%define version 1.9.2
%define release %mkrel 1
%define api 1.0
%define major       1
%define libname        %mklibname %name %{api}_%{major}
%define libnamedev     %mklibname -d %name %{api}

Summary: C++ API for the cairo multi-platform 2D graphics library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://cairographics.org/releases/%{name}-%{version}.tar.gz
License: LGPLv2+
Group: System/Libraries
Url: http://cairographics.org/cairomm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post	-n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun	-n %{libname} -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%_libdir/libcairomm-%{api}.so.%{major}*

%files -n %libnamedev
%defattr(644,root,root,755)
%doc %_datadir/doc/cairomm-%api
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*.la
%_includedir/*
%_libdir/pkgconfig/*.pc
%dir %_libdir/%name-%api/
%dir %_libdir/%name-%api/include
%_libdir/%name-%api/include/*.h
%_datadir/devhelp/books/%name-%api
