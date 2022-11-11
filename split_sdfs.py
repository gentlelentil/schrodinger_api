import os
import pandas as pd

#RDKit related imports
from rdkit.Chem import AllChem as Chem

def split_sdfs(fpath):
    top, tail = os.path.split(fpath)
    mol_supp = Chem.SDMolSupplier(fpath)
    tail_noext = os.path.splitext(tail)[0]
    dirname = tail_noext + '_sdfs'
    try:
        os.mkdir(dirname)
    except FileExistsError:
        print('Directory already exists')

    for ID, i in enumerate(mol_supp):
        fname = tail + str(ID) + '.sdf'
        fpath = os.path.join(dirname, fname)
        with Chem.SDWriter(fpath) as w:
            w.write(i)


if __name__ == '__main__':
    split_sdfs('./ECBD_Bioactives/ECBD_bioactives.sdf') 
