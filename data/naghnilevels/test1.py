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

##[ Name        ]## test1
##[ Maintainer  ]## Niels Serup <ns@metanohi.org>
##[ Description ]## Just a basic level
##[ Start date  ]## 2010 August 14

from naghni.level import Level as GenericLevel
from naghni.object.shapes import *
from naghni.object.solids import *

class Level(GenericLevel):
    """A test level"""
    name='Test 1'

    def create_level(self):
        soil0 = self.add_pattern('patterns/soil0.svg')
        lines1 = self.add_pattern('patterns/lines1.svg')

        self.add_shape(Line, (0, 'inf'), (0, '-inf'),
                       fillarea=(-1, 0), fillbg=soil0)
        p = 0
        v = -1000
        h = 250
        def valley():
            self.add_shape(BezierCurve, (p, 0), (p+1000, v),
                           (p+2000, 0), fillarea=(0, -1),
                           fillbg=soil0)
        def hill():
            self.add_shape(BezierCurve, (p+2000, 0), (p+2500, h),
                           (p+3000, 0), fillarea=(0, -1),
                           fillbg=soil0)
        for i in range(10):
            valley()
            hill()
            l = 5
            s = 1800 / l
            rs = s / 5
            tp = p + 100
            for j in range(l):
                self.add_solid(RegularPolygon, (tp, 0),
                               rs, j + i + 3,
                               density=0.5 / (i+1) + 0.1,
                               function='eat')
                tp += s

            p += 3000
            v += 60
            h -= 15
        valley()
        p += 2000
        self.add_shape(Line, (p, 'inf'), (p, '-inf'),
                       fillarea=(1, 0), fillbg=soil0)

        self.add_solid(Circle, (p-500, 200), 100, function='hole',
                       density=0.7)
        self.add_solid(Circle, (p-600, 200), 100, function='hole',
                       density=0.7)

        # Fancy polygon
        self.add_solid(Polygon, (40, 50), (700, 200), (400, 800),
                       (200, 1100), (250, 600), (300, 620),
                       density=0.7, fillbg=lines1)

        self.add_solid(Circle, (60, 400), 40, density=0.5,
                       function='character')
