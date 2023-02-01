from collections import OrderedDict

ordered_dictionary = OrderedDict()
N = int(input())
data = []

for i in range(N):
    data = list(map(str, input().split()))
    net_price = int(data[-1])
    data.pop(-1)
    item_name = " ".join(data)
    if item_name not in ordered_dictionary.keys():
        ordered_dictionary[item_name] = net_price
    else:
        ordered_dictionary[item_name] += net_price

for k,v in ordered_dictionary.items():
        print(k,v)
