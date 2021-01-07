def item1a():
    name = "boxing shorts"
    tag ="shorts"
    description = "for lighting fast feet"
    size = "Mens Large"
    price = "30"
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price}
    return info

def item2a():
    name = "blue polo"
    tag ="shirt"
    description = "great for any look"
    price = "10"
    size = "Female Large"
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price}
    return info

def item3a():
    name = "Fo Leather Jacket"
    tag ="jacket"
    description = "Looks like leather"
    price = "30"
    size = "Mens medium"
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price}
    return info

def item4a():
    name = "sandals"
    tag ="footwear"
    description = "studded with jewels"
    price = "10"
    size = "kids 10"
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price}
    return info


def inventory_items():
    return [item1a(), item2a(), item3a(), item4a()]


def item1b():
    name = "Vintage socks"
    tag = "footwear"
    description = "cool design/logo"
    price = "5"
    size = "Men's M"
    info = {"name": name, "tag":tag, "description": description, "size":size, "price": price}
    return info

def item2b():
    name ="Vintage Jacket"
    tag = "jacket"
    description = "bomber jacket 94"
    price = "45"
    size = "Men's XL"
    info = {"name": name, "tag":tag, "description": description, "size":size, "price": price}
    return info

def inventory_itemsbarb():
    return [item1b(), item2b()]