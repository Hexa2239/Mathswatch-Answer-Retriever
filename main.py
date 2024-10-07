try:
    import os
    from flask import Flask, request, jsonify, send_file
    import json
    from array import array
except:
    print("Package import failed. Verify you have everything needed installed.")
# Needed for DATA Checking
# data_folder = './data'

# for root, dirs, files in os.walk(data_folder):
#     for file in files:
#         print(os.path.join(root, file))

data_folder = "./data"
jsonFiles = []

app = Flask("Mathswatch Data Grabber")

@app.get("/")
def get():
    return send_file("./public/index.html"), 200

@app.get("/api/getID")
def getAnswer():
    jsonFiles = []

    for root, dirs, files in os.walk(data_folder):
        for file in files:
            jsonFiles.append(file)
    
    print(jsonFiles)

    requestedQuestionId = request.args.get("id")

    for file in jsonFiles:
        with open(data_folder + "/" + file, "r") as f:
            text = f.read()
            jsonData = json.loads(text)

            if (jsonData["status"] == "success"):
                print("This file is good!")

                for obj in jsonData["data"]:
                    if str(obj["question_id"]) == requestedQuestionId:
                        formattedAnswer = ""
                        ind = 0
                        print("Found question")

                        for a in obj["answer"]:
                            ind = 0
                            for t in a["text"]:
                                if (len(obj["answer"]) == ind + 1):
                                    formattedAnswer += t
                                else:
                                    formattedAnswer += t + "|"
                                ind += 1

                        return formattedAnswer
                        


                return "Not Found", 200


app.run(port=40020, host="0.0.0.0")

