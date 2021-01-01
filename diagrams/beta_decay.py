# beta decay

from pyfeyn.user import *

fd = FeynDiagram()

xfirst_quark = -3
ydist_quark = 0.65
yfirst_quark = -1

xblob_radius = 0.5
yblob_radius = 1.0

xshift_fermion = 0.2
line_bend = -0.0

n_blob = Ellipse(x=xfirst_quark, y=yfirst_quark - ydist_quark, xradius=xblob_radius, yradius=yblob_radius, fill=[color.rgb.red])
p_blob = Ellipse(x=-xfirst_quark, y=yfirst_quark - ydist_quark, xradius=xblob_radius, yradius=yblob_radius, fill=[color.rgb.green])
#n_blob = Ellipse(x=xfirst_quark, y=yfirst_quark - ydist_quark, xradius=xblob_radius, yradius=yblob_radius)
#p_blob = Ellipse(x=-xfirst_quark, y=yfirst_quark - ydist_quark, xradius=xblob_radius, yradius=yblob_radius)

p1a = Point(xfirst_quark, yfirst_quark)
p1b = Point(-xfirst_quark, yfirst_quark)
p1ain = Point(p1a.x() + xshift_fermion, p1a.y())
p1bout = Point(p1b.x() - xshift_fermion, p1b.y())
#fermion1 = Fermion(p1ain, p1bout).bend(line_bend).addArrow(position=0.3).addArrow(position=0.7).addLabel(r"\Pdown",pos=-0.038, displace=0.0).addLabel(r"\Pup", pos=1.045, displace=0.001)
line1 = Line(p1ain, p1bout).bend(line_bend).addArrow(position=0.3).addArrow(position=0.7).addLabel(r"\Pdown",pos=-0.038, displace=0.0).addLabel(r"\Pup", pos=1.045, displace=0.001)

p2a = Point(xfirst_quark, yfirst_quark - ydist_quark)
p2b = Point(-xfirst_quark, yfirst_quark - ydist_quark)
p2ain = Point(p2a.x() + xshift_fermion, p2a.y())
p2bout = Point(p2b.x() - xshift_fermion, p2b.y())
fermion2 = Fermion(p2ain, p2bout).bend(line_bend).addArrow(position=0.3).addArrow(position=0.7).addLabel(r"\Pdown",pos=-0.038, displace=0.0).addLabel(r"\Pdown", pos=1.045, displace=0.001)

p3a = Point(xfirst_quark, yfirst_quark - 2.0 * ydist_quark)
p3b = Point(-xfirst_quark, yfirst_quark - 2.0 * ydist_quark)
p3ain = Point(p3a.x() + xshift_fermion, p3a.y())
p3bout = Point(p3b.x() - xshift_fermion, p3b.y())
fermion3 = Fermion(p3ain, p3bout).bend(line_bend).addArrow(position=0.3).addArrow(position=0.7).addLabel(r"\Pup",pos=-0.038, displace=0.0).addLabel(r"\Pup", pos=1.045, displace=0.001)

w_in = Point(-0.5, yfirst_quark)
w_out = Point(0.5, yfirst_quark + 2.0 * ydist_quark)
bos = Photon(w_in, w_out).addLabel(r"\PWminus")

e_out = Point(-xfirst_quark - xshift_fermion, yfirst_quark + ydist_quark)
f1 = Fermion(w_out, e_out).addArrow().addLabel(r"\Pelectron", pos=1.1, displace=0.0) 
#f1 = Fermion(w_out, e_out).addArrow().addLabel(r"\Pelectron", displace=0.2) 

nue_out = Point(-xfirst_quark - xshift_fermion, yfirst_quark + 3.0 * ydist_quark)
f2 = Fermion(nue_out, w_out).addArrow().addLabel(r"\Pagne", pos=-0.1, displace=0.05) 
#f2 = Fermion(nue_out, w_out).addArrow().addLabel(r"\Pagne", displace=0.2)

fd.draw("beta_decay.pdf")



#line1 = MultiLine(p1a, p1b,n=3).bend(-0.5).addArrow()
#line1 = MultiLine(p1a, p1b,n=2).bend(-0.5).addArrow(position=0.3).addArrow(position=0.7)
#line1 = Line(p1a, p1b).bend(-0.5).addArrow(position=0.3).addArrow(position=0.7)
#c1 = Circle(center=p1a, radius=0.5, fill=[color.rgb.red], points=[p1a])
#c2 = Circle(center=p1b, radius=0.5, fill=[color.rgb.blue], points=[p1b])
#n_blob = Ellipse(x=xfirst_quark, y=yfirst_quark - ydist_quark, xradius=xblob_radius, yradius=yblob_radius).setFillStyle(CROSSHATCHED45)
