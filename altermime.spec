%define major 0
%define libname %mklibname altermime %{major}
%define devname %mklibname altermime -d

Summary:	Allows you to modify mailpacks
Name:		altermime
Version:	0.3.10
Release:	6
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

%files
%doc CHANGELOG LICENCE README
%{_bindir}/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared %{name} library
Group:		System/Libraries

%description -n %{libname}
alterMIME is a small program which is used to alter your mime-encoded
emailpacks as typically received by Inflex, XaMime and AMaViS.

alterMIME will allow you to put in things like disclaimers in each email's
text body, and also permit you to nullify (make into a zero-byte) attachments.

%files -n %{libname}
%{_libdir}/libaltermime.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
alterMIME is a small program which is used to alter your mime-encoded
emailpacks as typically received by Inflex, XaMime and AMaViS.

alterMIME will allow you to put in things like disclaimers in each email's
text body, and also permit you to nullify (make into a zero-byte) attachments.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/libaltermime.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%serverbuild

%make RPM_OPT_FLAGS="%{optflags} -fPIC -D_REENTRANT -I." libdir=%{_libdir} LDFLAGS="%{ldflags}"

%install
%makeinstall_std \
	bindir=%{_bindir} \
	libdir=%{_libdir} \
	includedir=%{_includedir}/%{name} \

