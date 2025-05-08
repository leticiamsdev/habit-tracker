import requests
from datetime import datetime

USERNAME = "leticiamari"

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

today = datetime.now()
#
#
# response = requests.post(url=graph_endpoint, json = graph_config, headers=headers)
# print(response.text)

att_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

graph_att = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today? "),
}


response = requests.post(url=att_endpoint, json=graph_att, headers=headers)
print(response.text)



graph_put = {
    "quantity": "10",
}
#
# put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
# response = requests.put(url=put_endpoint, json = graph_put, headers=headers)
# print(response.text)

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20250503"
#
# response = requests.delete(url= delete_endpoint, headers=headers)
# print(response.text)