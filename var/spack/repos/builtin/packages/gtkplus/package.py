# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gtkplus(AutotoolsPackage):
    """The GTK+ 2 package contains libraries used for creating graphical user
       interfaces for applications."""
    homepage = "http://www.gtk.org"
    url = "http://ftp.gnome.org/pub/gnome/sources/gtk+/2.24/gtk+-2.24.31.tar.xz"

    version('2.24.32', 'b6c8a93ddda5eabe3bfee1eb39636c9a03d2a56c7b62828b359bf197943c582e')
    version('2.24.31', '68c1922732c7efc08df4656a5366dcc3afdc8791513400dac276009b40954658')
    version('2.24.25', '38af1020cb8ff3d10dda2c8807f11e92af9d2fa4045de61c62eedb7fbc7ea5b3')

    depends_on('pkgconfig', type='build')

    depends_on('atk')
    depends_on('gdk-pixbuf')
    depends_on('glib')
    depends_on('shared-mime-info')
    # Hardcode X11 support (former +X variant),
    # see #6940 for rationale:
    depends_on('pango+X')
    depends_on('gobject-introspection')

    patch('no-demos.patch')

    def patch(self):
        # remove disable deprecated flag.
        filter_file(r'CFLAGS="-DGDK_PIXBUF_DISABLE_DEPRECATED $CFLAGS"',
                    '', 'configure', string=True)

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.prepend_path("XDG_DATA_DIRS",
                               self.prefix.share)
        run_env.prepend_path("XDG_DATA_DIRS",
                             self.prefix.share)
