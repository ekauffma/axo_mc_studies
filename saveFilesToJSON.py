import os
import json

datasets_MC = [
        "JPsi",
        ]
directories_MC = [
        "/eos/cms/store/group/phys_exotica/axol1tl/MC_ScoutingNano_withAXOscore/JPsiToMuMu_PT-0to100_pythia8-gun/"
        ]

datasets_data = [
        "2024F",
        ]
directories_data = [
        "/eos/cms/store/group/phys_exotica/axol1tl/Data_ScoutingNano_withAXOscore/2024F/"
        ]

def list_root_files(directory):
    root_files = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.root'):
                full_path = os.path.join(dirpath, filename)
                root_files.append(full_path)
    return root_files

filePaths_MC = {}
for i in range(len(datasets_MC)):
    filePaths_MC[datasets_MC[i]] = list_root_files(directories_MC[i])

with open("filePaths.json", "w") as outfile:
    json.dump(filePaths_MC, outfile)

filePaths_data = {}
for i in range(len(datasets_data)):
    filePaths_data[datasets_data[i]] = list_root_files(directories_data[i])

with open("filePaths_data.json", "w") as outfile:
    json.dump(filePaths_data, outfile)

