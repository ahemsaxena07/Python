# # # #file input/output

# # # # f = open("hello.txt", "r")
# # # # content = f.read()
# # # # f.close
# # # with open("data.txt", "w") as f:
# # #     f.write("hello wrold!\n")
# # #     f.write(str(["line1", "line2", "line3"]))
    
# # # with open("data.txt", "a") as f:
# # #     f.write("new log entery\n")

# # # with open("data.txt") as f:
# # #     first_line = f.readline()

# # # import csv
# # # with open("data.csv", "w", newline = "") as f:
# # #     writer = csv.DictWriter(f, fieldnames = ["name", "age"])
# # #     writer.writeheader()
# # #     writer.writerow({"name": "alice", "age": 30})
# # # with open("data.csv") as f:
# # #     for row in csv.DictReader(f):
# # #         print(row["name"], row["age"])

# # import json
# # data = {"user": [{"name": "ahem", "age": 20}]}
# # with open("data.json", "w") as f:
# #     json.dump(data, f, indent = 2)
# # with open("data.json") as f:
# #     loaded = json.load(f)

# import pickle
# my_dic = {"model" :[1.2,3.4], "label": "cat"}
# with open("model.pkl", "wb") as f:
#     pickle.dump(my_dic, f)
# with open("model.pkl", "rb") as f:
#     restored = pickle.load(f)

f = open('numberstxt', 'w+')
f.write(str(233)+'\n')
f.write(str(13.45))
f.seek(0)
a = int(f.readline())
b = int(float(f.readline()))
print(a + a)
print(b + b)