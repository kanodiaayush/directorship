# Convert text files to csv
# Put text files in cross_directorship/
# Output files show up in output/
# One sample is added in the github
import pandas as pd
import ast
import json
import os
import datetime
from decimal import Decimal


files = os.listdir("cross_directorship/")
df_list = []
count = 0
data = []
for filename in files:
    if not filename.endswith('.txt'):
        continue
    with open('cross_directorship/%s' % filename) as f:
        count += 1
        content = f.read()
        data = eval(content)
        data.extend(eval(content))
        ans = pd.DataFrame(data)
        # ans = ans.append(df_list)
        # ans = ans.reindex(sorted(ans.columns, reverse=True), axis=1)
        ans = ans.reindex(sorted(ans.columns, reverse=True), axis=1)
        ans.to_csv('output/%s.csv' % filename[:-4], index=False)
        print("Done %s" % filename)
        # if count > 10:
            # break
    # break

        # data = ast.literal_eval(content)
# columns = set()
# for df in df_list:
    # columns.update(df.columns)
# print(columns)
# input()
# ans = [pd.DataFrame(columns=list(columns))]
# ans.columns = columns

# ans.extend(df_list)
# for elem in ans:
    # print(type(elem))
# input()
# print(ans)
# ans = pd.concat(ans)
# ans = pd.DataFrame(data)
# ans = ans.append(df_list)
# ans = ans.reindex(sorted(ans.columns, reverse=True), axis=1)
# ans.to_csv('data.csv', index=False)
# print(ans)

