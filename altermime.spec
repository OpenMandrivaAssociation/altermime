%define	major 0
%define libname	%mklibname altermime %{major}
%define develname %mklibname -d altermime

Summary:	Allows you to modify mailpacks
Name:		altermime
Version:	0.3.10
Release:	5
License:	BSD
Group:		Networking/Mail
URL:		http://www.pldaniels.com/altermime/
Source0:	http://www.pldaniels.com/altermime/%{name}-%{version}.tar.gz
Patch0:		altermime-0.3.7-shared.diff
BuildRequires:	libtool

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
Provides:	%{libname}-devel = %{EVRD}
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
export LDFLAGS="`rpm --eval %%configure|grep LDFLAGS|cut -d\\" -f2|sed -e 's/\$LDFLAGS\ //'`"

%make RPM_OPT_FLAGS="$CFLAGS -fPIC -D_REENTRANT -I." libdir=%{_libdir} LDFLAGS="$LDFLAGS"

%install
%makeinstall_std \
    bindir=%{_bindir} \
    libdir=%{_libdir} \
    includedir=%{_includedir}/%{name} \

%files
%doc CHANGELOG INSTALL LICENCE README
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/*.so


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.10-4mdv2011.0
+ Revision: 616560
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.3.10-3mdv2010.0
+ Revision: 436643
- rebuild

* Fri Dec 19 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.10-2mdv2009.1
+ Revision: 316156
- use LDFLAGS from the %%configure macro

* Mon Nov 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.10-1mdv2009.1
+ Revision: 303930
- 0.3.10
- rediffed P0

* Thu Oct 30 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.9-1mdv2009.1
+ Revision: 298719
- 0.3.9
- drop redundant patches; P1

* Mon Oct 13 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.8-3mdv2009.1
+ Revision: 293305
- added fixes from altermime-0.3-dev (P1)

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.8-2mdv2009.0
+ Revision: 238929
- use -Wl,--as-needed -Wl,--no-undefined

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.8-1mdv2008.0
+ Revision: 51856
- conform to the latest specs and adjust deps accordingly


* Tue Dec 12 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.7-3mdv2007.0
+ Revision: 95317
- fix deps
- Import altermime

* Fri Aug 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.7-0.3.7-2mdv2007.0
- rebuild

* Thu Mar 30 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.7-1mdk
- 0.3.7
- rediffed P0

* Wed Jan 18 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.6-2mdk
- make it install correctly on x86_64

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.6-1mdk
- 0.3.6
- use libtool

* Fri Dec 31 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3.5-3mdk
- revert latest "lib64 fixes"

* Tue Dec 28 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3.5-2mdk
- lib64 fixes

* Sat Nov 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3.5-1mdk
- 0.3.5
- provide a shared lib here too as well (P0)

