#
# Copyright (C) 2018 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
#  Author(s):  Vendula Poncova <vponcova@redhat.com>
#
from enum import Enum

from pyanaconda.core.configuration.base import Section


class TargetType(Enum):
    """Type of the installation target."""
    HARDWARE = "HARDWARE"
    IMAGE = "IMAGE"
    DIRECTORY = "DIRECTORY"


class TargetSection(Section):
    """The Installation Target section."""

    @property
    def type(self):
        """Type of the installation target."""
        return self._get_option("type", TargetType)

    @property
    def physical_root(self):
        """A path to the physical root of the target."""
        return self._get_option("physical_root")

    @property
    def is_hardware(self):
        """Are we installing on hardware?"""
        return self.type is TargetType.HARDWARE

    @property
    def is_image(self):
        """Are we installing on an image?"""
        return self.type is TargetType.IMAGE

    @property
    def is_directory(self):
        """Are we installing to a directory?"""
        return self.type is TargetType.DIRECTORY