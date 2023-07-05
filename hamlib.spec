#
# Conditional build:
%bcond_without	static_libs	# static library
%bcond_without	indi		# INDI rigctl/rotctl support
%bcond_without	usrp		# USRP backend
%bcond_without	lua		# Lua binding
%bcond_without	perl		# Perl binding
%bcond_without	python		# Python binding
%bcond_without	tcl		# Tcl binding

Summary:	Library to control radio transceivers and receivers
Summary(pl.UTF-8):	Biblioteka do sterowania nadajnikami i odbiornikami radiowymi
Name:		hamlib
Version:	4.5.5
Release:	2
License:	LGPL v2.1+ (library), GPL v2+ (programs)
Group:		Libraries
#Source0Download: https://github.com/Hamlib/Hamlib/releases
Source0:	https://github.com/Hamlib/Hamlib/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9996f507ae570be50d09df1157f140e0
Patch0:		%{name}-perl_install.patch
Patch1:		%{name}-usrp.patch
URL:		http://hamlib.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	gd-devel
%{?with_indi:BuildRequires:	libindi-devel}
BuildRequires:	libltdl-devel >= 2:2.2.6b
%{?with_indi:BuildRequires:	libnova-devel}
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2.2.6b
%{?with_usrp:BuildRequires:	libusrp-devel >= 0.8}
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	libxml2-devel >= 2.0
%{?with_lua:BuildRequires:	lua52-devel >= 5.2}
%{?with_perl:BuildRequires:	perl-devel}
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel >= 2.1}
BuildRequires:	readline-devel
BuildRequires:	source-highlight
%{?with_perl:BuildRequires:	swig-perl >= 1.3.22}
%{?with_python:BuildRequires:	swig-python >= 1.3.22}
%{?with_tcl:BuildRequires:	swig-tcl >= 1.3.22}
%{?with_tcl:BuildRequires:	tcl-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		tcl_libdir	%{_libdir}/tcl%{tcl_version}

%description
Hamlib provides a standardized programming interface that applications
can use to send the appropriate commands to a radio.

Also included in the package is a simple radio control program
'rigctl', which lets one control a radio transceiver or receiver,
either from command line interface or in a text-oriented interactive
interface.

%description -l pl.UTF-8
Hamlib zapewnia ustandaryzowany interfejs programistyczny, który może
być używany przez aplikacje do wysyłania odpowiednich poleceń do
radia.

W pakiecie dołączony jest także prosty program do sterowania radiem
"rigctl", który pozwala sterować nadajnikiem lub odbiornikiem radiowym
z poziomu linii poleceń lub interaktywnego interfejsu tekstowego.

%package devel
Summary:	Header files for Hamlib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Hamlib
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libusb-devel >= 1.0

%description devel
Development headers for building C applications with Hamlib radio
control library.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji w C z użyciem biblioteki
sterującej radiem Hamlib.

%package static
Summary:	Static Hamlib library
Summary(pl.UTF-8):	Statyczna biblioteka Hamlib
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Hamlib library.

%description static -l pl.UTF-8
Statyczna biblioteka Hamlib.

%package doc
Summary:	Documentation for the Hamlib radio control library
Summary(pl.UTF-8):	Dokumentacja do biblioteki sterującej radiem Hamlib
License:	LGPL v2.1+
Group:		Documentation
BuildArch:	noarch

%description doc
This package provides the developers documentation for the Hamlib
radio control library API.

%description doc -l pl.UTF-8
Ten pakiet zawiera dokumentację programistyczną API biblioteki
sterującej radiem Hamlib.

%package c++
Summary:	Hamlib radio control library C++ binding
Summary(pl.UTF-8):	Wiązanie C++ do biblioteki sterującej radiem Hamlib
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
Hamlib radio control library C++ language binding.

%description c++ -l pl.UTF-8
Wiązanie C++ do biblioteki sterującej radiem Hamlib.

%package c++-devel
Summary:	Header files for Hamlib radio control library C++ binding
Summary(pl.UTF-8):	Pliki nagłówkowe wiązania C++ do biblioteki sterującej radiem Hamblib
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7

%description c++-devel
Development headers for building C++ applications with Hamlib radio
control library.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji w C++ z użyciem biblioteki
sterującej radiem Hamlib.

%package c++-static
Summary:	Static Hamlib C++ library
Summary(pl.UTF-8):	Statyczna biblioteka C++ Hamlib
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static Hamlib C++ library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka C++ Hamlib.

%package -n lua-%{name}
Summary:	Hamlib radio control library Lua binding
Summary(pl.UTF-8):	Wiązanie języka Lua do biblioteki sterującej radiem Hamlib
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	lua52-libs >= 5.2

%description -n lua-%{name}
Hamlib Lua language bindings to allow radio control from Perl
scripts.

%description -n lua-%{name} -l pl.UTF-8
Wiązania języka Lua do biblioteki Hamlib, umożliwiające sterowanie
radiem z poziomu skryptów Lua.

%package -n perl-%{name}
Summary:	Hamlib radio control library Perl binding
Summary(pl.UTF-8):	Wiązanie Perla do biblioteki sterującej radiem Hamlib
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-%{name}
Hamlib Perl language bindings to allow radio control from Perl
scripts.

%description -n perl-%{name} -l pl.UTF-8
Wiązania języka Perl do biblioteki Hamlib, umożliwiające sterowanie
radiem z poziomu skryptów Perla.

%package -n python-%{name}
Summary:	Hamlib radio control library Python binding
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki sterującej radiem Hamlib
Group:		Libraries/Perl
Requires:	%{name} = %{version}-%{release}

%description -n python-%{name}
Hamlib Python language bindings to allow radio control from Python
scripts.

%description -n python-%{name} -l pl.UTF-8
Wiązania języka Python do biblioteki Hamlib, umożliwiające sterowanie
radiem z poziomu skryptów Pythona.

%package -n tcl-%{name}
Summary:	Hamlib radio control library Tcl binding
Summary(pl.UTF-8):	Wiązanie Tcl-a do biblioteki sterującej radiem Hamlib
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
  
%description -n tcl-%{name}
Hamlib Tcl Language bindings to allow radio control from Tcl scripts.

%description -n tcl-%{name} -l pl.UTF-8
Wiązania języka Tcl do biblioteki Hamlib, umożliwiające sterowanie
radiem z poziomu skryptów Tcl-a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	LUA=/usr/bin/lua5.2 \
	TCL_VERSION=%{tcl_version} \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	%{?with_usrp:--enable-usrp} \
	%{!?with_indi:--without-indi} \
	%{?with_lua:--with-lua-binding} \
	%{?with_perl:--with-perl-binding} \
	%{?with_python:--with-python-binding} \
	%{?with_tcl:--with-tcl-binding}

%{__make}

%{__make} -C doc doc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libhamlib*.la

%if %{with lua}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lua/5.*/Hamliblua.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{_libdir}/lua/5.*/Hamliblua.a}
%endif

%if %{with perl}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/perltest.pl
%{__rm} -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Hamlib/.packlist
%endif

%if %{with python}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/_Hamlib.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{py_sitedir}/_Hamlib.a}
%py_postclean
%endif

%if %{with tcl}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/tcl*/Hamlib/hamlibtcl.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{_libdir}/tcl*/Hamlib/hamlibtcl.a}
%endif

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/hamlib

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS PLAN README README.freqranges README.multicast THANKS
%attr(755,root,root) %{_bindir}/ampctl
%attr(755,root,root) %{_bindir}/ampctld
%attr(755,root,root) %{_bindir}/rigctl
%attr(755,root,root) %{_bindir}/rigctlcom
%attr(755,root,root) %{_bindir}/rigctld
%attr(755,root,root) %{_bindir}/rigmem
%attr(755,root,root) %{_bindir}/rigsmtr
%attr(755,root,root) %{_bindir}/rigswr
%attr(755,root,root) %{_bindir}/rigtestlibusb
%attr(755,root,root) %{_bindir}/rotctl
%attr(755,root,root) %{_bindir}/rotctld
%attr(755,root,root) %{_libdir}/libhamlib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhamlib.so.4
%{_mandir}/man1/ampctl.1*
%{_mandir}/man1/ampctld.1*
%{_mandir}/man1/rigctl.1*
%{_mandir}/man1/rigctlcom.1*
%{_mandir}/man1/rigctld.1*
%{_mandir}/man1/rigmem.1*
%{_mandir}/man1/rigsmtr.1*
%{_mandir}/man1/rigswr.1*
%{_mandir}/man1/rotctl.1*
%{_mandir}/man1/rotctld.1*
%{_mandir}/man7/hamlib.7*
%{_mandir}/man7/hamlib-primer.7*
%{_mandir}/man7/hamlib-utilities.7*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhamlib.so
%dir %{_includedir}/hamlib
%{_includedir}/hamlib/ampclass.h
%{_includedir}/hamlib/amplifier.h
%{_includedir}/hamlib/amplist.h
%{_includedir}/hamlib/config.h
%{_includedir}/hamlib/rig.h
%{_includedir}/hamlib/rig_dll.h
%{_includedir}/hamlib/riglist.h
%{_includedir}/hamlib/rotator.h
%{_includedir}/hamlib/rotlist.h
%{_pkgconfigdir}/hamlib.pc
%{_aclocaldir}/hamlib.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libhamlib.a
%endif

%files doc
%defattr(644,root,root,755)
%doc doc/html/{search,*.css,*.html,*.js,*.png}

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhamlib++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhamlib++.so.4

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhamlib++.so
%{_includedir}/hamlib/rigclass.h
%{_includedir}/hamlib/rotclass.h

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libhamlib++.a
%endif

%if %{with lua}
%files -n lua-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lua/5.*/Hamliblua.so
%endif

%if %{with perl}
%files -n perl-%{name}
%defattr(644,root,root,755)
%{perl_vendorarch}/Hamlib.pm
%dir %{perl_vendorarch}/auto/Hamlib
%attr(755,root,root) %{perl_vendorarch}/auto/Hamlib/Hamlib.so
%endif

%if %{with python}
%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_Hamlib.so
%{py_sitedir}/Hamlib.py[co]
%endif

%if %{with tcl}
%files -n tcl-%{name}
%defattr(644,root,root,755)
%dir %{tcl_libdir}/Hamlib
%attr(755,root,root) %{tcl_libdir}/Hamlib/hamlibtcl*.so
%{tcl_libdir}/Hamlib/pkgIndex.tcl
%endif
