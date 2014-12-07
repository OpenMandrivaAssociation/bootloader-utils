Summary:	Small utils needed for the kernel
Name:		bootloader-utils
Version:	1.16
Release:	9
License:	GPL+
Group:		System/Kernel and hardware
URL:		https://abf.io/omv_software/bootloader-utils
Source0:	%{name}-%{version}.tar.xz
Patch0:		bootloader-utils.initrdsymlink.patch
BuildRequires:	perl-MDK-Common
BuildArch:	noarch
Requires:	drakxtools-backend >= 10-52
Requires:	perl-base
Requires(post,preun):	chkconfig
Requires(post,preun):	rpm-helper
Requires(post,preun):	initscripts >= 7.06-21

%description
Utilities needed to install/remove a kernel.
Also for updating bootloaders.

%prep
%setup -q
%patch0 -p1

%build
make

%install
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

%files
%config(noreplace) /etc/sysconfig/installkernel
/sbin/installkernel
/sbin/kernel_remove_initrd
%{_sbindir}/detectloader
%{_sbindir}/rebootin
%{_mandir}/man8/detectloader.*
%{_mandir}/man8/rebootin.*
