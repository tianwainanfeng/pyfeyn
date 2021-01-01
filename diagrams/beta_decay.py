# beta decay

from pyfeyn.user import *

fd = FeynDiagram()

p1a = Point(-3, 0)
p1b = Point( 3, 0)
#line1 = Line(p1a, p1b).bend(-0.5).addArrow()
#line1 = MultiLine(p1a, p1b,n=3).bend(-0.5).addArrow()
line1 = MultiLine(p1a, p1b,n=2).bend(-0.5).addArrow(position=0.3).addArrow(position=0.7)
#line1 = MultiLine(p1a, p1b,n=2).bend(-0.5).addArrow(position=0.8)
c1 = Circle(center=p1a, radius=0.5, fill=[color.rgb.red], points=[p1a])
c2 = Circle(center=p1b, radius=0.5, fill=[color.rgb.blue], points=[p1b])

fd.draw("beta_decay.pdf")
