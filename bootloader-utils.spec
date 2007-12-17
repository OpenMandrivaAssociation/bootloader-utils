%define _mypost_service() if [ $1 = 1 ]; then /sbin/chkconfig --add %{1}; fi;

Summary:	Small utils needed for the kernel
Name:		bootloader-utils
Version:	1.15
Release:	%mkrel 1
Source0:	%{name}-%{version}.tar.bz2
License:	GPL+
Group:		System/Kernel and hardware
Requires:	perl-base

Requires(post,preun):	chkconfig rpm-helper
Requires(post,preun):	initscripts >= 7.06-21mdk

URL:            http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/initscripts/mandrake/loader/
Requires:	drakxtools-backend >= 10-52mdk
BuildRequires:	perl-MDK-Common
BuildArch:	noarch

%description
Utilities needed to install/remove a kernel.  Also for updating
bootloaders.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make ROOT=$RPM_BUILD_ROOT mandir=%{_mandir} install

%post
%_mypost_service kheader

%preun
%_preun_service kheader

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) /etc/sysconfig/installkernel
/etc/rc.d/init.d/kheader
/sbin/installkernel
/sbin/kernel_remove_initrd
%{_sbindir}/detectloader
%{_sbindir}/rebootin
%{_mandir}/man8/detectloader.*
%{_mandir}/man8/rebootin.*

