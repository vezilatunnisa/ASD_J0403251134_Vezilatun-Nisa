def merge_sort(data):

    mid = len(data) //2
    left = data[:mid]
    right = data[mid:]

    print(f"{indent}divide -> left = {left} | right = {right}")

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    merged = merge
    return merge(left_sorted, right_sorted)

def merge(left,rigth):

    result =[]
    i= 0
    j=0


    while i < len(left) and  j< len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result =.append(right[j])
            j+=1
    #menambahkan sisa elemen jika ada 
    result.extend(left[i:])
    result.extend(right[j:])

    return result