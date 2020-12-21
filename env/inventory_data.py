def item1():
    name = "boxing shorts"
    tag ="shorts"
    description = "for lighting fast feet"
    size = "Mens Large"
    price = "30"
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price}
    return info

def item2():
    name = "blue polo"
    tag ="shirt"
    description = "great for any look"
    price = "10"
    size = "Female Large"
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price}
    return info

def item3():
    name = "Fo Leather Jacket"
    tag ="jacket"
    description = "Looks like leather"
    price = "30"
    size = "Mens medium"
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price}
    return info

def item4():
    name = "sandals"
    tag ="footwear"
    description = "studded with jewels"
    price = "10"
    size = "kids 10"
    info = {"name": name,"tag":tag, "description": description, "size":size, "price": price}
    return info


def inventory_items():
    return [item1(), item2(), item3(), item4()]