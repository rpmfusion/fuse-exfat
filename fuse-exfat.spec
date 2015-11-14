Name:           fuse-exfat
Summary:        Free exFAT file system implementation
Version:        1.2.2
Release:        1%{?dist}
License:        GPLv2+
Group:          System Environment/Base
Source0:        https://github.com/relan/exfat/releases/download/v%{version}/fuse-exfat-%{version}.tar.gz
URL:            https://github.com/relan/exfat
BuildRequires:  fuse-devel

%description
This driver is the first free exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is intended
to replace FAT32 removing some of it's limitations. exFAT is a standard FS
for SDXC memory cards.

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"


%files
%doc COPYING
%{_sbindir}/mount.exfat-fuse
%{_sbindir}/mount.exfat
%{_mandir}/man8/*

%changelog
* Sat Nov 14 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Sat Dec 20 2014 TingPing <tingping@tingping.se> - 1.1.0-1
- Update to 1.1.0

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 17 2013 TingPing <tingping@tingping.se> - 1.0.1-1
- Initial package

