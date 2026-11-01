# Virtual screening against ABCA1 variants

Built during my Computer Science and Biosciences degree at IIIT-Delhi (2023). It docks a ChEMBL ligand set against homology models of wild-type ABCA1 and six missense variants (V825I, L681I, Y159N, R219K, K1587R, E1172D), then ranks the ligands by predicted binding affinity. The models come from [Homology-Modelling](https://github.com/aryanteng/Homology-Modelling).

- `ligand_to_sdf.py` fetches ligand structures from the ChEMBL API and writes SDF files to `ligands_sdf/`.
- Docking runs per ligand and model with AutoDock Vina (`.pdbqt` inputs, `_log.log` outputs).
- `ranking.py` parses the best pose's affinity from every log and writes `data.txt`, sorted from strongest binder (kcal/mol).
- `plot.py` plots the distribution of binding affinities (KDE).

Archived: kept for reference, not maintained.
