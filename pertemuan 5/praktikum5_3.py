def jumlah_list(data,index=0):
    if index == len(data):
        return 0
    
    return data[index] + jumlah_list(data, index + 1)