import requests
import json

API_URL = "https://api-inference.huggingface.co/models/mattmdjaga/segformer_b2_clothes"
headers = {"Authorization": f"Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("rich_young.jpg")
outfile = open("rich.jsonl", "w")
for row in output:
    json.dump(row, outfile)
    outfile.write('\n')
    #print(len(row))
#print(output)
