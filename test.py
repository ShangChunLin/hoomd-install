#from hoomd doc https://buildmedia.readthedocs.org/media/pdf/hoomd-blue/latest/hoomd-blue.pdf
# run by : python3 test.py --gpu=0
import hoomd
from hoomd import md
hoomd.context.initialize()

# Create a 10x10x10 simple cubic lattice of particles with type name A
hoomd.init.create_lattice(unitcell=hoomd.lattice.sc(a=2.0, type_name='A'), n=10)

# Specify Lennard-Jones interactions between particle pairs
nl = md.nlist.cell()
lj = md.pair.lj(r_cut=3.0, nlist=nl)
lj.pair_coeff.set('A', 'A', epsilon=1.0, sigma=1.0)

# Integrate at constant temperature
md.integrate.mode_standard(dt=0.005)
hoomd.md.integrate.langevin(group=hoomd.group.all(), kT=1.2, seed=4)

# Run for 10,000 time steps
hoomd.run(10e5)
