from data import *

# Initial check
reco_count = 0
comm_count = 0

for analysis in analyses:
    if analysis["recommendation"] and bool(analysis["recommendation"]):
        # print(analysis["id"], analysis["recommendation"])
        reco_count += 1

    if analysis["comment"] and bool(analysis["comment"]):
        # print(analysis["id"], analysis["comment"])
        comm_count += 1
print("---------Count--------------")
print("analyses with recommendations", reco_count)
print("analyses with comments", comm_count)
print("----------------------------")
# Copying recomendations to comments

for analysis in analyses:
    if bool(analysis["recommendation"]):
        if bool(analysis["comment"]):
            analysis["comment"] = (
                analysis["recommendation"] + " and " + analysis["comment"]
            )
            comm_count += 1
        else:
            analysis["comment"] = analysis["recommendation"]

    print(analysis["id"], analysis["comment"])

print("---------Count--------------")
print("analyses with recommendations", reco_count)
print("analyses with comments", comm_count)
