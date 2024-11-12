import sys
import os
import json
from sample import sample

f = open("filePaths.json")
filePaths = json.load(f)

treeNames = [
    'Events',
]

samples = dict(
    [
        (
            sampleName,
            sample(listOfFiles = filePaths[sampleName], treeNames = treeNames)
        )
        for sampleName in filePaths
    ]
)

f.close()