# extract_ligand.py

## What is it?
Program to extract ligand from .pdb/.cif files


## Usage
1. Prepare .pdb/.cif files.
1. Edit `extract_ligand.yaml`.
	* `INPUT_FILES`: target file list
	* `OUTPUT_DIR`: output directory
	* `OUTPUT_EXT`: output ext (`.pdb` or `.cif`)
	* `IGNORE_RESIDUES`: ignore residue name list
1. Execute.

	```{.py .numberSource .line-numbers}
	$ python extract_ligand.py extract_ligand.yaml
	```


## Requirement
* Python3
	* pyyaml
	* parmed


## License
The MIT License (MIT)

Copyright (c) 2026 mumeiyamibito


## Authors
* mumeiyamibito


## ChangeLog
### Ver. 20261117
* Release.
