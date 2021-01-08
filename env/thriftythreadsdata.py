def TT1():
    name = "boxing shorts"
    tag ="shorts"
    description = "for lighting fast feet"
    size = "Mens Large"
    price = "30"
    folder ="thrifty_threads" #name of folder file is stored in
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price, "folder": folder}
    return info

def TT2():
    name = "blue polo"
    tag ="shirt"
    description = "great for any look"
    price = "10"
    size = "Female Large"
    folder ="thrifty_threads" #name of folder file is stored in
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price, "folder": folder}
    return info

def TT3():
    name = "Fo Leather Jacket"
    tag ="jacket"
    description = "Looks like leather"
    price = "30"
    size = "Mens medium"
    folder ="thrifty_threads" #name of folder file is stored in
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price, "folder": folder}
    return info

def TT4():
    name = "sandals"
    tag ="footwear"
    description = "studded with jewels"
    price = "10"
    size = "kids 10"
    folder ="thrifty_threads" #name of folder file is stored in
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price, "folder": folder}
    return info


def inventory_itemsTT():
    return [TT1(), TT2(), TT3(), TT4()]


