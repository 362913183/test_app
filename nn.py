from Base.read_data import red_data
def red_yml():
    data = red_data('search.yaml').get('SearchData')
    data_list = []
    for i in data.keys():
        data_list.append((i, data.get(i).get('test')))
    return data_list

print(red_yml())