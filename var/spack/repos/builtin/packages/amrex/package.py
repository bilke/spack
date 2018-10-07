# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Amrex(CMakePackage):
    """AMReX is a publicly available software framework designed
    for building massively parallel block- structured adaptive
    mesh refinement (AMR) applications."""

    homepage = "https://amrex-codes.github.io/amrex/"
    git      = "https://github.com/AMReX-Codes/amrex.git"

    version('develop', branch='development')

    # Config options
    variant('dimensions', default='3',
            description='Dimensionality', values=('2', '3'))
    variant('shared',  default=False,
            description='Build shared library')
    variant('mpi',          default=True,
            description='Build with MPI support')
    variant('openmp',       default=False,
            description='Build with OpenMP support')
    variant('precision',  default='double',
            description='Real precision (double/single)',
            values=('single', 'double'))
    variant('eb',  default=False,
            description='Build Embedded Boundary classes')
    variant('fortran',  default=False,
            description='Build Fortran API')
    variant('linear_solvers', default=True,
            description='Build linear solvers')
    variant('amrdata',    default=False,
            description='Build data services')
    variant('particles',  default=False,
            description='Build particle classes')
    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    # Build dependencies
    depends_on('mpi', when='+mpi')
    depends_on('python@2.7:', type='build')
    depends_on('cmake@3.5:',  type='build')
    conflicts('%clang')

    def cmake_is_on(self, option):
        return 'ON' if option in self.spec else 'OFF'

    def cmake_args(self):
        args = [
            '-DUSE_XSDK_DEFAULTS=ON',
            '-DDIM:STRING=%s' % self.spec.variants['dimensions'].value,
            '-DBUILD_SHARED_LIBS:BOOL=%s' % self.cmake_is_on('+shared'),
            '-DENABLE_MPI:BOOL=%s' % self.cmake_is_on('+mpi'),
            '-DENABLE_OMP:BOOL=%s' % self.cmake_is_on('+openmp'),
            '-DXSDK_PRECISION:STRING=%s' %
            self.spec.variants['precision'].value.upper(),
            '-DENABLE_EB:BOOL=%s' % self.cmake_is_on('+eb'),
            '-DXSDK_ENABLE_Fortran:BOOL=%s' % self.cmake_is_on('+fortran'),
            '-DENABLE_LINEAR_SOLVERS:BOOL=%s' %
            self.cmake_is_on('+linear_solvers'),
            '-DENABLE_AMRDATA:BOOL=%s' % self.cmake_is_on('+amrdata'),
            '-DENABLE_PARTICLES:BOOL=%s' % self.cmake_is_on('+particles')
        ]
        return args
