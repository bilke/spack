##############################################################################
# Copyright (c) 2017, Los Alamos National Security, LLC
# Produced at the Los Alamos National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class CandleBenchmarks(Package):
    """ECP-CANDLE Benchmarks"""

    homepage = "https://github.com/ECP-CANDLE/Benchmarks"
    url      = "https://github.com/ECP-CANDLE/Benchmarks/archive/v1.0.tar.gz"

    tags = ['proxy-app', 'ecp-proxy-app']

    version('0.1', sha256='767f74f43ee3a5d4e0f26750f2a96b8433e25a9cd4f2d29938ac8acf263ab58d')
    version('0.0', '6eced30dc15374bc9f90a86d0396e470')

    variant('mpi', default=True, description='Build with MPI support')

    extends('python@2.7:')
    depends_on('py-theano +gpu', type=('build', 'run'))
    depends_on('py-keras', type=('build', 'run'))
    depends_on('py-matplotlib +image@:2.2.3', type=('build', 'run'))
    depends_on('py-tqdm', type=('build', 'run'))
    depends_on('py-scikit-learn', type=('build', 'run'))
    depends_on('opencv@3.2.0: +core +highgui +imgproc +jpeg +png +tiff +zlib +python -dnn ~eigen ~gtk')
    depends_on('py-mdanalysis', type=('build', 'run'))
    depends_on('py-mpi4py', when='+mpi', type=('build', 'run'))
    depends_on('py-h5py~mpi', when='~mpi', type=('build', 'run'))
    depends_on('py-h5py+mpi', when='+mpi', type=('build', 'run'))
    depends_on('py-requests', type=('build', 'run'))

    # see #3244, but use external for now
    # depends_on('tensorflow')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix.bin)
