import requests

USERNAME = "leticiamari"
TOKEN = "wbhdujihawudhoaoaoaoao"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}


# response = requests.post(url=pixela_endpoint, json= user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id" : GRAPH_ID,
    "name" : "Study Graph",
    "unit" : "Hours",
    "type" : "int",
    "color" : "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}


#
# response = requests.post(url=graph_endpoint, json = graph_config, headers=headers)
# print(response.text)

att_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

graph_att = {
    "date" : "20250505",
    "quantity": "5",
}


response = requests.post(url=att_endpoint, json=graph_att, headers=headers)
print(response.text)
