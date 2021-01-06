# beta decay

from pyfeyn.user import *

fd = FeynDiagram()

muon_in = Point(-3, 0)
muon_out = Point(0, 0)
muon = Fermion(muon_in, muon_out).addArrow().addLabel(r"\Pmuon",pos=0.3)

numu_in = Point(muon_out.x(), muon_out.y())
numu_out = Point(3., 3.)
numu = Fermion(numu_in, numu_out).addArrow().addLabel(r"\Pgngm",pos=0.7)

w_in = Point(muon_out.x(), muon_out.y())
w_out = Point(1.5, -1.5)
w = Photon(w_in, w_out).addLabel(r"\PWminus")

electron_in = Point(w_out.x(), w_out.y())
electron_out = Point(3., 0.)
electron = Fermion(electron_in, electron_out).addArrow().addLabel(r"\Pelectron",pos=0.7)

anue_in = Point(w_out.x(), w_out.y())
anue_out = Point(3., -3.)
anue = Fermion(anue_out, anue_in).addArrow().addLabel(r"\Pagne",pos=0.3)

fd.draw("muon_decay.pdf")

