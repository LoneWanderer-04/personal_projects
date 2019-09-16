import requests

domain =  'https://api.mercedes-benz.com/image_tryout/v1/vehicles/WME4533441K012345/'

def get_from_domain(endpoint, args):
    r = requests.get(url = domain + endpoint, params = args)
    data = r.json()
    return data


args = {
    "perspectives" : "EXT010, EXT200, INT3",
    "night" : True
}
print(get_from_domain('vehicles', args))