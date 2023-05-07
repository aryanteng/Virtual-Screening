import os
import re

# Define the regex pattern to extract the affinity value
affinity_pattern = re.compile(r"\s+1\s+(-?\d+\.\d+)\s+")

# Define a dictionary to store the ligand names and their corresponding affinities
ligand_affinities = {}

# Iterate over the log files in the ligands_sdf directory
for filename in os.listdir("ligands_sdf"):
    if filename.endswith("_log.log"):
        filepath = os.path.join("ligands_sdf", filename)
        with open(filepath) as f:
            lines = f.readlines()
            # Extract the affinity value from the log file
            affinity_match = affinity_pattern.search("".join(lines))
            if affinity_match:
                affinity = float(affinity_match.group(1))
                # Get the ligand name from the log file name
                ligand_name = filename.replace("_log.log", "")
                # Store the ligand name and affinity in the dictionary
                ligand_affinities[ligand_name] = affinity

# Sort the ligand_affinities dictionary by ascending affinity values
sorted_affinities = sorted(ligand_affinities.items(), key=lambda x: x[1])

# Print the ligand name and affinity for the ligand with the lowest affinity in each log file
for ligand, affinity in sorted_affinities:
    print(f"{ligand}: {affinity}")
