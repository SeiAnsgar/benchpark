# Copyright 2023 Lawrence Livermore National Security, LLC and other
# Benchpark Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

"""
CAPELLA system:
144 nodes@: 
4xNVIDIA H100-SXM5; 
2xAMD EPYC CPU 9334 (32 cores);
768 GB RAM(12x32GB); 
800GB NVMe storage
OS: Alma Linux 9.4 
"""

from benchpark.system import System

from benchpark.directives import variant, maintainers
from benchpark.paths import hardware_descriptions

#has to be named according to its folder name

#init the system:
#benchpark system init --dest='/data/horse/ws/anse978b-ss_benchpark/my_systems/capella_system' zih-capella

class ZihCapella(System):
    """This is the generic system class for an x86 system, gcc compiler, mpi.
    It can be easily copied and modified to model other systems."""

    def __init__(self, spec):
        super().__init__(spec)

        self.scheduler = "slurm"
        setattr(self, "sys_cores_per_node", 64)
        setattr(self, "gpu_cores_per_node", 4)

    def compute_packages_section(self):
        selections = {
            "packages": {
                "GCCcore": {
                    "externals": [{"spec": "gcc@13.2.0", "prefix": "/software/genoa/r24.04/GCCcore/13.2.0/"}],
                    "buildable": False,
                },
                "openmpi": {
                    "externals": [{"spec": "openmpi@4.1.6", "prefix": "/software/rapids/r24.10/OpenMPI/4.1.6-GCC-13.2.0/"}],
                    "buildable": False,
                },
            }
        }
        return selections

    def compute_software_section(self):
        """This is somewhat vestigial, and maybe deleted later. The experiments
        will fail if these variables are not defined though, so for now
        they are still generated (but with more-generic values).
        """
        return {
            "software": {
                "packages": {
                    "default-compiler": {"pkg_spec": "gcc"},
                    "compiler-gcc": {"pkg_spec": "gcc"},
                    "default-mpi": {"pkg_spec": "openmpi"},
                    "blas": {"pkg_spec": "openblas"},
                    "lapack": {"pkg_spec": "openblas"},
                }
            }
        }
