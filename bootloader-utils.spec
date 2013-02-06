Summary:	Small utils needed for the kernel
Name:		bootloader-utils
Version:	1.15
Release:	10
Source0:	%{name}-%{version}.tar.bz2
Patch0:		bootloader-utils.initrdsymlink.patch
License:	GPL+
Group:		System/Kernel and hardware
Requires:	perl-base

Requires(post,preun):	chkconfig rpm-helper
Requires(post,preun):	initscripts >= 7.06-21

URL:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/bootloader-utils/
Requires:	drakxtools-backend >= 10-52
BuildRequires:	perl-MDK-Common
BuildArch:	noarch

%description
Utilities needed to install/remove a kernel.  Also for updating
bootloaders.

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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.15-7mdv2011.0
+ Revision: 663331
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.15-6mdv2011.0
+ Revision: 603764
- rebuild

* Thu Mar 11 2010 Thomas Backlund <tmb@mandriva.org> 1.15-5mdv2010.1
+ Revision: 518229
- drop obsolete kheader initscript, not used by kernel since 2.6.22-6mdv (#52803)
- fix url

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.15-4mdv2010.0
+ Revision: 413181
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.15-3mdv2009.1
+ Revision: 350210
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.15-2mdv2009.0
+ Revision: 220489
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Sep 09 2007 Adam Williamson <awilliamson@mandriva.org> 1.15-1mdv2008.0
+ Revision: 83195
- rebuild for 2008
- Fedora license policy
- slight spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Mon Jan 15 2007 Pixel <pixel@mandriva.com> 1.15-1mdv2007.0
+ Revision: 109040
- rebootin with grub: handle short-non-blank labels (used for BOOT_IMAGE=xxx) (#26813)

* Thu Oct 26 2006 Pixel <pixel@mandriva.com> 1.14-1mdv2007.1
+ Revision: 72643
- handle "savedefault --once" (grub, #26700)
- Import bootloader-utils

* Sat Aug 12 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.13-1mdv2007.0
- handle default, legacy & xen0 kernels

* Wed May 31 2006 Pixel <pixel@mandriva.com> 1.12-1mdv2007.0
- rename *desktop586 and *desktop686 to *desktop for better consistency

* Tue May 30 2006 Pixel <pixel@mandriva.com> 1.11-1mdv2007.0
- add support for mdv extension (eg: 1mdv instead of 1mdk)
- add support for "laptop" kernels (was mm kernels)
  (from Thomas Backlund)

* Wed May 17 2006 Pixel <pixel@mandriva.com> 1.10-1mdk
- kheader: add support for tmb kernels
- /etc/init.d/kheader should not be a config file
- s/Mandrakesoft/Mandriva/

* Mon Jan 09 2006 Olivier Blin <oblin@mandriva.com> 1.9-6mdk
- convert parallel init to LSB
- fix post/preun Requires

* Sun Jan 01 2006 Olivier Blin <oblin@mandriva.com> 1.9-5mdk
- parallel init support

* Tue Aug 30 2005 Pixel <pixel@mandriva.com> 1.9-4mdk
- nice handling of "make modules_install" not done 
  (when installing own built kernel) (bugzilla #17981)

* Fri Aug 12 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.9-3mdk
- fix rpmlint errors (PreReq) 
- fix URL
- mkrel

* Fri Nov 12 2004 Pixel <pixel@mandrakesoft.com> 1.9-2mdk
- kheader is now generated from kheader.pl when building package
- kheader: add i586-up-1GB and i686-up-64GB (bugzilla #12189)

* Fri Aug 27 2004 Juan Quintela <quintela@mandrakesoft.com> 1.9-1mdk
- new -C option to work with cramfs.

* Mon Jul 19 2004 Pixel <pixel@mandrakesoft.com> 1.8-6mdk
- installkernel is skipped DURING_INSTALL

* Mon Jul 19 2004 Pixel <pixel@mandrakesoft.com> 1.8-5mdk
- installkernel:
  - ensure the PATH contains /sbin and /usr/sbin
  - force rebuilding the initrd in "copy" mode
    (since one may build more than one kernel with the same version)
  - use --no-short-name in "copy" mode

* Tue Jul 06 2004 Pixel <pixel@mandrakesoft.com> 1.8-4mdk
- bootloader-config prefers --no-short-name instead of --no-link

* Fri Jul 02 2004 Pixel <pixel@mandrakesoft.com> 1.8-3mdk
- require drakxtools-backend instead of drakxtools-newt

* Thu Jul 01 2004 Pixel <pixel@mandrakesoft.com> 1.8-2mdk
- installkernel *is* used for copying installing kernels in /boot 
  (cf arch/i386/boot/install.sh used by kernel's "make install")

* Tue Jun 29 2004 Pixel <pixel@mandrakesoft.com> 1.8-1mdk
- installkernel:
  - it is now a wrapper to bootloader-config (in drakxtools-newt)
  - always have option AUTOREMOVE
  - always have option NOCOPY (was useful to copy your home built kernel)
    => option NOCONFIG deprecated
  - force option -s when installing and -S when removing
    (ie always do/remove the "build" symlink to the source tree)
  - force bootloader auto-detection (options AUTODETECT and LOADER are deprecated)
  - option OPTIONS is removed (what was it for exactly?)
- detectloader is now a wrapper to bootloader-config (in drakxtools-newt)
- helper scripts make-initrd, lilo, grub and yaboot obsolete

* Tue May 18 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.7-1mdk
- sanitize /etc/fstab parsing: do not match "/foobar/" when looking
  for "/"
- grub configuration:
  o simplify code through reusing MDK::Common
  o minimal "LABEL=foobar" managment aka handle it when looking for
    boot device (generic LABEL=foobar support is still lacking)
  o santize boot partition lookup:
    * do not match "/foobar/" when looking for "/"
    * do not match "/foobar/boot" when looking for "/boot"

* Tue Mar 02 2004 Nicolas Planel <nplanel@mandrakesoft.com> 1.6-7mdk
- getroot() don't have arguement.

* Tue Mar 02 2004 Nicolas Planel <nplanel@mandrakesoft.com> 1.6-6mdk
- append is not null anymore.
- ide-scsi removed from command line for all kernel (2.6 2.4).

* Fri Feb 27 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.6-5mdk
- when boot loader is grub, do not remove unrelated kernel entries (#5952)
- from Thomas Backlund <tmb@mandrake.org>:
  o typo fixes
  o make some messages somewhat more understandable

