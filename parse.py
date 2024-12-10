#
# Parser for hand position data
#

import pandas as pd
from hand_position_data import a, b, d, e, h, l, o, r, w

filesData = [a, b, d, e, h, l, o, r, w]
fileNames = ['a', 'b', 'd', 'e', 'h', 'l', 'o', 'r', 'w']

allData = []
dataUsed = {}

# Formatting the data
for fileIndex, data in enumerate(filesData):
    for arrayIndex, dataArray in enumerate(data):
        row = []
        if len(dataArray) == 20:
            for tupleIndex, joint in enumerate(dataArray):
                if isinstance(joint, tuple) and len(joint) == 2:
                    x, y = joint
                    row.append(x)
                    row.append(y)
            if fileNames[fileIndex] in dataUsed:
                dataUsed[fileNames[fileIndex]] += 1
            else:
                dataUsed[fileNames[fileIndex]] = 1

            row.append(fileNames[fileIndex])
            allData.append(row)

df = pd.DataFrame(allData)

print(dataUsed)
columnHeaders = []
for i in range(20):
    columnHeaders.append(f'Joint {i + 1} (x)')
    columnHeaders.append(f'Joint {i + 1} (y)')
columnHeaders.append('Letter')
df.columns = columnHeaders


output = 'positions2.xlsx'
with pd.ExcelWriter(output) as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)






