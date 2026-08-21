import json

try:
    with open("store.json", "x") as file:
        json.dump({"status": "created"}, file)
    print("File created successfully")

except Exception as e:
    print("Failed creating the file:", e)

try:
    with open("store.json", "a") as file:
        file.write("done")
    print("Append done")

except Exception:
    print("Error occurred in append")