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

##[ Name        ]## test0
##[ Maintainer  ]## Niels Serup <ns@metanohi.org>
##[ Description ]## Just a basic level
##[ Start date  ]## 2010 August 14

from naghni.level import Level as GenericLevel
from naghni.object.shapes import *
from naghni.object.solids import *

class Level(GenericLevel):
    """A test level"""
    name='Test 0'

    def create_level(self):
        lines0 = self.add_pattern('patterns/lines0.svg')

        for i in range(12):
            self.add_solid(RegularPolygon, (700 + i * 150, -330),
                           25, 3 + i / 2,
                           density=0.7 / (i + 1) + 0.1,
                           function='eat')
        for i in range(24):
            self.add_solid(Circle, (700 + i * 75, -430), 10,
                           density=0.8 / (i + 1) + 0.1)
        for i in range(24):
            kargs = dict(
                density=0.8 / (i + 1) + 0.1,
                fillbg=lines0)
            if i % 2 == 0:
                kargs['function'] = 'air'
            self.add_solid(Circle, (700 + i * 75, -70), 10, **kargs)

        self.add_solid(Circle, (1200, -170), 60, function='hole',
                       density=0.4)

        self.add_shape(Line, (-200, 'inf'), (-200, '-inf'),
                       fillarea=(-1, 0), fillbg=lines0)
        self.add_shape(Line, (-200, 200), (200, -200),
                       fillarea=(0, -1), fillbg=lines0)
        self.add_shape(BezierCurve, (200, -200), (2000, -1800),
                       (4200, 400), fillarea=(0, -1), fillbg=lines0)
        self.add_shape(Line, (4200, 'inf'), (4200, '-inf'),
                       fillarea=(1, 0), fillbg=lines0)

        self.add_solid(Circle, (60, 400), 40, density=0.5,
                       function='character')
