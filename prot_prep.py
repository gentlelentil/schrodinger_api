from schrodinger.application.prepwizard2 import prepare
import os
from datetime import datetime

# #prepare the structures to be input to the prepwizard
# input_pdbid = '6CQ8'
# # output_ID = './PP2_out/' + input_pdbid + '_prep.mae'
# output_ID = input_pdbid + '_prep.mae'

# pdb_structure = prepare.retrieve_and_read_pdb(input_pdbid)


# # #reference for settings can be found 'prepwiz_settings_ref.txt
# prep_wiz_settings = prepare.PrepWizardSettings()

# #prepare protein structure, default return is one structure.
# struct = prepare.prepare_structure(pdb_structure, prep_wiz_settings)

# assert len(struct) == 1

# out_struct = struct[0]
# out_struct.write(output_ID)

# struct.write(output_ID, format='MAESTRO')

def prepare_protein(input_pbid):
    """
    fct to run prepwizard2 from $SCHRODINGER. 
    Creates directory of form YYMMDD_PP2_OUT containing the minimised protein structure.
    Settings for running the prepwizard can be found in prepwiz_settings_ref.txt. Note these are the standard settings for running prepwizard through the GUI.
    returns the file path of the output het state.
    """


    now = datetime.now()
    dt_form = now.strftime('%y%m%d')
    dirpath = dt_form + '_PP2_OUT'
    try:
        os.mkdir(dirpath) 
    except FileExistsError:
        print('Directory already exists, adding to dir')
    finally:
        os.chdir(dirpath)
    
    output_ID = input_pbid + '_prepared.mae'
    pdb_structure = prepare.retrieve_and_read_pdb(input_pdbid)
    prep_wiz_settings = prepare.PrepWizardSettings()
    struct = prepare.prepare_structure(pdb_structure, prep_wiz_settings)

    try:
        assert len(struct) == 1
        out_struct = struct[0]
    except AssertionError:
        print('More het states than 1 have been generated, please check prepwizard settings')
        return 1

    out_struct.write(output_ID)

    return output_ID