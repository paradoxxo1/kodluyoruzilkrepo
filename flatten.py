##### 1- Flatten fonksiyonu

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

##### 2- Liste elemanlarını tersine döndüren fonksiyon


def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        if isinstance(item, list):
            reversed_lst.append(reverse_list(item))
        else:
            reversed_lst.append(item)
    return reversed_lst[::-1]

# Bu fonksiyonları kullanarak önce verilen listeyi tersine çevirir,
# ardından elde edilen sonucu flatten fonksiyonuna sokarak düzleştirir 
# ve sonucu döndürürüz.

def reverse_and_flatten(lst):
    reversed_lst = reverse_list(lst)
    flat_list = flatten(reversed_lst)
    return flat_list


# Örneğin, reverse_and_flatten([[1, 2], [3, 4], [5, 6, 7]]) şeklinde kullanarak
# sonuç [1, 2, 3, 4, 5, 6, 7] elde ederiz. 
# Ancak, bu fonksiyonun önce tersine çevirme yapması 
# ve daha sonra düzleştirme yapması nedeniyle daha yavaş çalışabilir.