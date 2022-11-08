from schrodinger.protein import getpdb
from schrodinger import structure
from schrodinger.structutils import analyze


struc = getpdb.get_pdb('6CQ8')

st = structure.Structure.read(struc)

# pdb_struc = structure.StructureReader.read(struc)

fname = '/home/nathaniel/Desktop/schrodinger_api/6CQ8_out.mae'

with structure.StructureWriter(fname) as writer:
    writer.append(st)

ligands = analyze.find_ligands(st)
print(len(ligands))



