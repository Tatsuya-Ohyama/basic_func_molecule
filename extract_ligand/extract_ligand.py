#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%% ====================
# modules
import sys, signal
sys.dont_write_bytecode = True
signal.signal(signal.SIGINT, signal.SIG_DFL)

import yaml
import parmed
import os



#%% ====================
# constant
CONFIG_FILE = "extract_ligand.yaml" if len([v for v in sys.argv if v.endswith((".yaml", ".yml"))]) == 0 else [v for v in sys.argv if v.endswith((".yaml", ".yml"))][0]

STANDARD_RESIDUES = {
	"ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE",
	"LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL",
	"HIE", "HID", "HIP", "CYM", "ACE", "NME",
	"SOL", "HOH", "WAT"
}



#%% ====================
# read .yaml config
config = None

print(f"read .yaml config: {CONFIG_FILE}")
with open(CONFIG_FILE, "r") as obj_input:
	config = yaml.safe_load(obj_input)



#%% ====================
# read .pdb and output .pdb
if not os.path.isdir(config['OUTPUT_DIR']):
	os.makedirs(config['OUTPUT_DIR'])

for pdb_file in config['INPUT_FILES']:
	print(f"read .pdb: {pdb_file}")
	obj_mol = parmed.load_file(pdb_file)

	basename = os.path.basename(pdb_file)
	basename = os.path.splitext(basename)[0]
	list_res_idx = []
	for obj_residue in obj_mol.residues:
		residue_name = obj_residue.name
		if residue_name in STANDARD_RESIDUES or residue_name in config['IGNORE_RESIDUES']:
			continue

		idx = obj_residue.idx
		chain = obj_residue.chain
		residue_id = obj_residue.number
		output_file = os.path.join(config['OUTPUT_DIR'], f"{basename}-{chain}_{residue_name}-{residue_id}{config['OUTPUT_EXT']}")
		obj_mol[idx,:].save(output_file, overwrite=True)
		print(f"    output {config['OUTPUT_EXT']}: {output_file}")

