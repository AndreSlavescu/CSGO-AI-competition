import json

t_count = {}
ct_count = {}


for i in range(0, 18):
    istr = str(i).zfill(2)
    with open("dataset_"+istr+".json", "r") as read_file:
        data = json.load(read_file)

    for j in data:
        winner = j["round_winner"]
        if winner == "Terrorist":
            if j["map"] in t_count: 
                t_count[j["map"]] += 1
            else:
                t_count[j["map"]] = 1
        else:
            if j["map"] in ct_count: 
                ct_count[j["map"]] += 1
            else:
                ct_count[j["map"]] = 1
            

for k in t_count.keys():
    t_count1 = t_count[k] 
    ct_count1 = ct_count[k]
    if t_count1 > ct_count1:
        print("Terrorists have more wins",k, t_count1-ct_count1)
    if ct_count1 > t_count1:
        print("Counter Terrorists have more wins",k, ct_count1-t_count1)


print(t_count)
print(ct_count)

#print(data[0]["map_crc"])
