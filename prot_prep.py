#Run Schrodinger protein preparation wizard on pdb structure

# from argparse import ArgumentParser
# import configparser

# parser = ArgumentParser(description='Run the Protein preparation wizard of Schrodinger')

# parser.add_argument('-pdb', nargs='?', help='Input .pdb file to be prepared', required=True)
# parser.add_argument('-set', nargs='?', help='PrepWizard settings file', required=True)

# args = parser.parse_args()



# pdb_file = args.pdb
# set_file = args.set

from schrodinger.application.prepwizard2 import prepare

#prepare the structures to be input to the prepwizard
input_pdb = './6CQ8.pdb'

pdb_structure = prepare.retrieve_and_read_pdb('6CQ8')

#reference for settings can be found 'prepwiz_settings_ref.txt
prep_wiz_settings = prepare.PrepWizardSettings()

#prepare protein structure, default return is one structure.
struct = prepare.prepare_structure(pdb_structure, prep_wiz_settings, logger=log.logging.Logger)
