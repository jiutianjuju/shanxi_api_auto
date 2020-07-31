import requests
from selenium import webdriver
def get_the_lpart(LineID,CableID):
    url = "http://192.168.0.2:10812/api/Asset/GetLinePartViewList_Advanced_Province"
    headers = {'city':'anhui'}
    data = {
            'LinePartName':'',
            'CityID':'d800515e-0237-4cd1-8df3-e7228339655a',
            'OperationGroupID':'4b88da1a-7ed3-11ea-b517-0242ac160002',
            'VoltageID':'554a3cfe-455d-4054-82da-a39c12f62980',
            'LineID':LineID,
            'CableID':CableID,
            'PageSize':'10',
            'PageIndex':'1',
            'LoadDropDown':'',
            'OperationStatus':'',
            'StartTime':'',
            'EndTime':'',
            }

    res = requests.post(url,headers=headers,data=data)
    # print(res.json())
    dict1 = res.json()
    lparts = dict1['Data']
    lpartlists = lparts['LinePartAccountViewList']
    result_lists = []
    for lpart in lpartlists:
        # return lpart['LinePartName']
        result_lists.append(lpart['LinePartName'])
    # print(result_lists)
    return result_lists

def get_lpart_detail(LineID,CableID,lpartname):

    lists = get_the_lpart(LineID,CableID)
    # print(lists)
# print(lists)
    for i in range(len(lists)):
        if lists[i] == lpartname:
            xpath = '//*[@id="line-container"]/div[4]/div/div[1]/div[3]/table/tbody/tr[%d]/td[12]/div/div/i'%(i+1)
        else:
            pass
    # print(xpath)
    return xpath

# LineID = "19b75799-faf2-4552-9562-e9c6e8268d0a"
# CableID = "acd9b32c-2063-4aed-b841-3b9aae2ba6f5"
# lpartname = "测试新增达1回线电缆电缆段2"
# get_lpart_detail(LineID,CableID,lpartname)