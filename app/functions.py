from itertools import product

abcs = list('abcdefghijklmnopqrstuvwxyz')
nums = list('0123456789')

def get_id_from_plate(plate:str):
    global abcs, nums
    #target = list("aaaa000")
    target = list(plate.lower())
    abc, num = tuple(target[:4]), tuple(target[-3:])
    for i, _abc in enumerate(product(abcs, repeat=4)):
        if abc == _abc:
            for j, _num in enumerate(product(nums, repeat=3)):
                if num == _num:
                    return (i+1)+j+(i*999)

def get_plate_from_id(id:int):
    global abcs, nums
    #target = 456_976_000
    target = int(id)
    for i, _abc in enumerate(product(abcs, repeat=4)):
        if target in range(i*1000,i*1000+1001):
            for j, _num in enumerate(product(nums, repeat=3)):
                if target == (i+1+j+(i*999)):
                    return ''.join(_abc+_num)