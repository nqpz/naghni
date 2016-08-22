# Naghni Levels: A builtin set of levels for Naghni
# Copyright (C) 2010  Niels Serup

# This file is part of Naghni Levels.
#
# Naghni Levels is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Naghni Levels is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Naghni Levels. If not, see <http://www.gnu.org/licenses/>.

##[ Name        ]## test2
##[ Maintainer  ]## Niels Serup <ns@metanohi.org>
##[ Description ]## Just a basic level
##[ Start date  ]## 2010 August 14

from naghni.level import Level as GenericLevel
from naghni.object.shapes import *
from naghni.object.solids import *
import random

class Level(GenericLevel):
    """A test level"""
    name='Test 2'

    def create_level(self):
        lines0 = self.add_pattern('patterns/lines0.svg')
        lines1 = self.add_pattern('patterns/lines1.svg')
        soil0 = self.add_pattern('patterns/soil0.svg')
        patterns = lines0, lines1, soil0

        for i in range(500):
            if i % 4 == 0:
                self.add_solid(Circle, (i * 40, i), 10, fillbg=random.choice(patterns))
            self.add_solid(Circle, (i * 40, i + 40), 10, function='eat')

        self.add_solid(Circle, (20000, 1000), 100, function='hole',
                       density=0.2)

        self.add_solid(Circle, (50, 50), 50, density=0.9,
                       function='character')
