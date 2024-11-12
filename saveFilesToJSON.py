import os
import json

datasets = [
        "JPsi",
        ]
directories = [
        "/eos/cms/store/group/phys_exotica/axol1tl/MC_ScoutingNano_withAXOscore/JPsiToMuMu_PT-0to100_pythia8-gun/"
        ]

def list_root_files(directory):
    root_files = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.root'):
                full_path = os.path.join(dirpath, filename)
                root_files.append(full_path)
    return root_files

filePaths = {}
for i in range(len(datasets)):
    filePaths[datasets[i]] = list_root_files(directories[i])

with open("filePaths.json", "w") as outfile:
    json.dump(filePaths, outfile)
