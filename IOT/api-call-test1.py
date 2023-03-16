# testing
import requests
url = "https://sbm-apps.dev/ERECRUITMENT2/MASTERDATA/WEB_GET_USERTABLE"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for item in data['data']:
        use_id = item['USEID']
        use_nam = item['USENAM']
        is_windows = item['ISWINDOWS']
        bus_func = item['BUSFUNC']
        created_by = item['CREATEDBY']
        created_on = item['CREATEDON']
        print(f"USEID: {use_id}, USENAM: {use_nam}, ISWINDOWS: {is_windows}, BUSFUNC: {bus_func}, CREATEDBY: {created_by}, CREATEDON: {created_on}")
else:
    print(f"Failed to fetch data, status code: {response.status_code}")
# testing

# import requests
# import json

# # Define the URL and request parameters
# url = "https://sbm-apps.dev/ERECRUITMENT2/MASTERDATA/WEB_CREATE_USER"
# params = {
#     "USER_ID": "sbm_testing",
#     "USER_NAME": "testing",
#     "USER_GROUP": "SYSTEM-ADMIN"
# }

# # Send the POST request with the parameters
# response = requests.post(url, data=json.dumps(params), headers={"Content-Type": "application/json"})

# # Check if the request was successful
# if response.ok:
#     data = response.json()
#     if data["Result"]:
#         print("User created successfully")
#     else:
#         print("Error creating user:", data["Message"])
# else:
#     print("Error creating user. HTTP status code:", response.status_code)
