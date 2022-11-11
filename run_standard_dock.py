from schrodinger.pipeline import pipeline
from schrodinger.pipeline import stage
from schrodinger.pipeline import pipeio
from schrodinger import structure

import glob

#test for stage

#input ligands
INPUT_DIR = './ECBD_bioactives_sdfs'

inp_dir_glob = INPUT_DIR + '/*.sdf'

# lig_file = './ECBD_Bioactives/ECBD_bioactives.sdf'

lig_flist = glob.glob(inp_dir_glob)

# RDL_specs = {
#     'STAGECLASS': 'filtering.LigFilterStage',
#     'INPUTS': lig_file,
#     'OUTPUTS': 'RDL_OUT',
#     'CONDITIONS': ["Molecular_weight <= 650", "Num_rotatable_bonds <= 10", "Num_rings <= 6"],
# }

# INPUT_STAGE_SPECS = {
#     'VARCLASS': 'Structures',
#     'FILES': lig_file
# }


# stage_obj = stage.Stage('RDL', specs=RDL_specs)

# outputs = stage_obj.run()

# sdf library 

# ligands = structure.SDReader(lig_file)
# mae_ligfname = 'lig_out'
# structure.MaestroWriter(mae_ligfname)

input_ligands = pipeio.Structures(lig_flist)

#now can add stages

# print(input_ligands.getFiles())

# ligands = pipeio.Structures(lig_file)
# ligands.count()

# stageobj = stage.Stage('RDL')
# stageobj['STAGECLASS'] = 'filtering.LigFilterStage'
# stageobj.setInput(1, 'INPUT1', lig_file)
# stageobj['OUTPUTS'] = 'RDL_OUT'
# stageobj['CONDITIONS'] = ["Molecular_weight <= 650", "Num_rotatable_bonds <= 10", "Num_rings <= 6"]

