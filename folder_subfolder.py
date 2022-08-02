import os
for folder in range(1, 2+1):
    os.makedirs(str(folder))

for folder in range(1, 2+1):
    for subfolder in ["mon", "tue", "wed", "thu", "fri"]:
        os.makedirs(str(folder)+"/"+str(subfolder))
