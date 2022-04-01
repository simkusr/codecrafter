# primitive counter
def counter(arr):
    res = dict()
    for itm in arr:
        if itm not in res.keys():
            res[itm] = 1
        else:
            res[itm] += 1
    return res

if __name__ == '__main__':
    while True:
        arr = input("enter a list of items: ")
        print(arr)
        rly_arr = arr.split(",")
        new_arr = []
        for i in rly_arr:
            new_arr.append(int(i))
        print(counter(new_arr))

