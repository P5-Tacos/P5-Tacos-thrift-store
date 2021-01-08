def BB1():
    name = "Vintage socks"
    tag = "footwear"
    description = "cool design/logo"
    price = "5"
    size = "Men's M"
    folder ="barbarella" #name of folder file is stored in
    info = {"name": name, "tag":tag, "description": description, "size":size, "price": price, "folder":folder}
    return info

def BB2():
    name ="Vintage Jacket"
    tag = "jacket"
    description = "bomber jacket 94"
    price = "45"
    size = "Men's XL"
    folder ="barbarella" #name of folder file is stored in
    info = {"name": name, "tag":tag, "description": description, "size":size, "price": price, "folder":folder}
    return info

def inventory_itemsBB():
    return [BB1(), BB2()]