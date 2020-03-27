import requests
# import json

def getData(country):
    response = requests.get("https://corona.lmao.ninja/v2/historical/"+country)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code


def writeData(jsonData, country):
    country = country.title()
    print(canada["timeline"]["cases"])
    filename = "fitVirusCV19_v05\ourData\getData" + country + ".m"
    with open(filename, "w") as dataFile:
        dataFile.write("function [country, C,date0] = getData"+country+"()\n")
        dataFile.write("country = '" + country + "';\n")
        firstdate = "2020/"+list(jsonData.keys())[0][:-3]
        dataFile.write("date0=datenum('"+firstdate+"'); % start date\n")
        dataFile.write("C = [\n")

        for i, val in enumerate(jsonData):
            dataFile.write(str(jsonData[val]) + " % " + str(val) + "\n")

        dataFile.write("]';\nend")

country = "canada"
canada = getData(country=country)
writeData(canada['timeline']['cases'], country)
# print(canada['timeline']['cases'][0])
