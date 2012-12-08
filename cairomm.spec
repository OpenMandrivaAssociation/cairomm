%define api 1.0
%define major       1
%define libname        %mklibname %{name} %{api}_%{major}
%define libnamedev     %mklibname -d %{name} %{api}

Summary: C++ API for the cairo multi-platform 2D graphics library
Name:		cairomm
Version:	1.10.0
Release:	3
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
%makeinstall_std

%files -n %{libname}
%{_libdir}/libcairomm-%{api}.so.%{major}*

%files -n %{libnamedev}
%doc %{_datadir}/doc/cairomm-%{api}
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/%{name}-%{api}/
%dir %{_libdir}/%{name}-%{api}/include/
%{_libdir}/%{name}-%{api}/include/*.h
%{_datadir}/devhelp/books/%{name}-%{api}/


%changelog
* Tue Dec 06 2011 Zé <ze@mandriva.org> 1.10.0-3
+ Revision: 738024
- fix file tyep (finally)
- fix version and release
- fix file type
- fix typo
- we need to set requires to release
- 1.10.2
- clean defattr, BR, clean section and mkrel
- clean .la files
- clean useless macros

* Mon Sep 19 2011 Götz Waschk <waschk@mandriva.org> 1.10.0-2
+ Revision: 700317
- rebuild

* Mon Aug 22 2011 Götz Waschk <waschk@mandriva.org> 1.10.0-1
+ Revision: 696079
- update to new version 1.10.0

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.8-2
+ Revision: 663353
- mass rebuild

* Sat Feb 05 2011 Götz Waschk <waschk@mandriva.org> 1.9.8-1
+ Revision: 636170
- update to new version 1.9.8

* Tue Oct 26 2010 Götz Waschk <waschk@mandriva.org> 1.9.6-1mdv2011.0
+ Revision: 589434
- update to new version 1.9.6

* Fri Oct 22 2010 Götz Waschk <waschk@mandriva.org> 1.9.4-1mdv2011.0
+ Revision: 587591
- update to new version 1.9.4

* Sat Oct 16 2010 Götz Waschk <waschk@mandriva.org> 1.9.2-1mdv2011.0
+ Revision: 586000
- update to new version 1.9.2

* Wed Jul 21 2010 Götz Waschk <waschk@mandriva.org> 1.9.1-1mdv2011.0
+ Revision: 556340
- update to new version 1.9.1

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 1.8.4-1mdv2010.1
+ Revision: 461000
- new version
- update file list

* Sat Jul 11 2009 Götz Waschk <waschk@mandriva.org> 1.8.2-1mdv2010.0
+ Revision: 394861
- update to new version 1.8.2

* Wed Jan 28 2009 Götz Waschk <waschk@mandriva.org> 1.8.0-1mdv2009.1
+ Revision: 334733
- update to new version 1.8.0

* Mon Dec 22 2008 Götz Waschk <waschk@mandriva.org> 1.7.2-1mdv2009.1
+ Revision: 317474
- update to new version 1.7.2

* Fri Nov 07 2008 Götz Waschk <waschk@mandriva.org> 1.7.0-2mdv2009.1
+ Revision: 300542
- rebuild for new libxcb

* Sun Oct 26 2008 Götz Waschk <waschk@mandriva.org> 1.7.0-1mdv2009.1
+ Revision: 297479
- fix build deps
- update to new version 1.7.0

* Tue Sep 16 2008 Götz Waschk <waschk@mandriva.org> 1.6.4-1mdv2009.0
+ Revision: 285131
- update to new version 1.6.4

* Sun Aug 31 2008 Götz Waschk <waschk@mandriva.org> 1.6.2-1mdv2009.0
+ Revision: 277788
- new version

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.6.0-2mdv2009.0
+ Revision: 264343
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Apr 21 2008 Götz Waschk <waschk@mandriva.org> 1.6.0-1mdv2009.0
+ Revision: 196132
- new version
- drop patch
- update license tag

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 1.5.0-1mdv2009.0
+ Revision: 192432
- new version

* Wed Mar 26 2008 Götz Waschk <waschk@mandriva.org> 1.4.6-2mdv2008.1
+ Revision: 190294
- fix for a small cairo API change

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 22 2007 Götz Waschk <waschk@mandriva.org> 1.4.6-1mdv2008.1
+ Revision: 111172
- new version

* Tue Aug 07 2007 Götz Waschk <waschk@mandriva.org> 1.4.4-1mdv2008.0
+ Revision: 59720
- new version
- new devel name

* Mon Jul 16 2007 Götz Waschk <waschk@mandriva.org> 1.4.2-1mdv2008.0
+ Revision: 52397
- new version

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 1.2.4-1mdv2007.1
+ Revision: 13551
- Import cairomm



* Tue Apr 10 2007 Götz Waschk <waschk@mandriva.org> 1.2.4-1mdv2007.1
- New version 1.2.4

* Tue Aug 22 2006 Götz Waschk <waschk@mandriva.org> 1.2.2-1mdv2007.0
- New release 1.2.2

* Mon Aug 21 2006 G�tz Waschk <waschk@mandriva.org> 1.2.0-1mdv2007.0
- new major
- drop patch
- New release 1.2.0

* Mon Jun 19 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-4mdv2007.0
- fix build

* Tue Jun 06 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2007.0
- Rebuild

* Fri May 12 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-2mdk
- fix buildrequires

* Fri May 12 2006 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdk
- initial package
