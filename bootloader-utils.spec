Summary:	Small utils needed for the kernel
Name:		bootloader-utils
Version:	1.15
Release:	%mkrel 6
Source0:	%{name}-%{version}.tar.bz2
License:	GPL+
Group:		System/Kernel and hardware
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	perl-base

Requires(post,preun):	chkconfig rpm-helper
Requires(post,preun):	initscripts >= 7.06-21mdk

URL:            http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/bootloader-utils/
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
rm -rf %{buildroot}
make ROOT=%{buildroot} mandir=%{_mandir} install
# nuke obsolete kheader initscript
rm -rf %{buildroot}/etc/rc.d/init.d/kheader

%pre
# disable obsolete kheader script on update if it exists
if [ $1 = 2 ]; then
    if [ -x /etc/rc.d/init.d/kheader ]; then
	chkconfig --del kheader
    fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) /etc/sysconfig/installkernel
/sbin/installkernel
/sbin/kernel_remove_initrd
%{_sbindir}/detectloader
%{_sbindir}/rebootin
%{_mandir}/man8/detectloader.*
%{_mandir}/man8/rebootin.*

