import requests
import json
#Test if call is succesful
def get_API_data(url):
    response = requests.get(url,verify =False)
    apidata = response.json()
    #Our Json file gives 2 dictionaries with the second key being another dictionary. This is the dictionary we will focus on
    midstep = apidata['entries']
    return midstep
#Counts number of a given category
def category_count(category,api_dict):
    count = 0
    for x in range(len(api_dict)):
        if api_dict[x]['Category']== category:
            count +=1
    return count

def output_of_category(category,api_dict):
    names=[]
    for x in range(len(api_dict)):
        if api_dict[x]['Category']== category:
            names.append(api_dict[x]['API'])
    return names