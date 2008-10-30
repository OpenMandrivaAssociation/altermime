%define	major 0
%define libname	%mklibname altermime %{major}
%define develname %mklibname -d altermime

Summary:	Allows you to modify mailpacks
Name:		altermime
Version:	0.3.9
Release:	%mkrel 1
License:	BSD
Group:		Networking/Mail
URL:		http://www.pldaniels.com/altermime/
Source0:	http://www.pldaniels.com/altermime/%{name}-%{version}.tar.gz
Patch0:		altermime-0.3.7-shared.diff
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
alterMIME is a small program which is used to alter your mime-encoded
emailpacks as typically received by Inflex, XaMime and AMaViS.
 
alterMIME will allow you to put in things like disclaimers in each email's
text body, and also permit you to nullify (make into a zero-byte) attachments.

%package -n	%{libname}
Summary:	Shared %{name} library
Group:          System/Libraries

%description -n	%{libname}
alterMIME is a small program which is used to alter your mime-encoded
emailpacks as typically received by Inflex, XaMime and AMaViS.
 
alterMIME will allow you to put in things like disclaimers in each email's
text body, and also permit you to nullify (make into a zero-byte) attachments.

%package -n	%{develname}
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel lib%{name}-devel
Provides:	%{libname}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel
Requires:	%{libname} = %{version}-%{release}

%description -n	%{develname}
alterMIME is a small program which is used to alter your mime-encoded
emailpacks as typically received by Inflex, XaMime and AMaViS.
 
alterMIME will allow you to put in things like disclaimers in each email's
text body, and also permit you to nullify (make into a zero-byte) attachments.

%prep

%setup -q
%patch0 -p0

%build
%serverbuild

%make RPM_OPT_FLAGS="$CFLAGS -fPIC -D_REENTRANT -I." libdir=%{_libdir} LDFLAGS="-Wl,--as-needed -Wl,--no-undefined"

%install
rm -rf %{buildroot}

%makeinstall_std \
    bindir=%{_bindir} \
    libdir=%{_libdir} \
    includedir=%{_includedir}/%{name} \

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG INSTALL LICENCE README
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
