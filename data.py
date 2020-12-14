def playdata():
    answer1 = "Hey, Hey, Hey!"
    #name = "John Mortensen"
    #dob = "October 21"
    #job = "Teacher"
    #story = "As a High School student I learned to type on a typewriter. \"Now is the time for all good men to come to the aid of their party.\" This is a phrase first proposed as a typing drill by instructor Charles E. Weller; its use is recounted in his book The Early History of the Typewriter, p. 21 (1918). Frank E. McGurrin, an expert on the early Remington typewriter, used it in demonstrating his touch typing abilities in January 1889. It has appeared in a number of typing books, often in the form \"Now is the time for all good men to come to the aid of their country. IMO, McGurrin would need to make an abridgement of this phrase today to, \"Now is the time for all good individuals to come to the aid of their country.\" A thought from my past, as we get ready to vote!"
    info = {"asnwer1": answer1}
    return info

thislist = []

def answersdata(numberOne, numberTwo):
    calc = numberOne + numberTwo #takes the user input and contatinates it together
    thislist.append(calc)
    return thislist

"""def answersdata(toAppend): #this is the correct way
    thislist.append(toAppend)
    return thislist"""

def testdata():
    parent_list = [{'A': 'val1', 'B': 'val2'}, {'C': 'val3', 'D': 'val4'}]
    return parent_list
"""

board = {
    "a8": "BR1n", "b8": "BN1", "c8": "BB1", "d8": "BQ1", "e8": "BK1n", "f8": "BB2", "g8": "BN2", "h8": "BR2n",
    "a7": "bp1", "b7": "bp2", "c7": "bp3", "d7": "bp4", "e7": "bp5", "f7": "bp6", "g7": "bp7", "h7": "bp8",
    "a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "  ", "g6": "  ", "h6": "  ",
    "a5": "  ", "b5": "  ", "c5": "  ", "d5": "  ", "e5": "  ", "f5": "  ", "g5": "  ", "h5": "  ",
    "a4": "  ", "b4": "  ", "c4": "  ", "d4": "  ", "e4": "  ", "f4": "  ", "g4": "  ", "h4": "  ",
    "a3": "  ", "b3": "  ", "c3": "  ", "d3": "  ", "e3": "  ", "f3": "  ", "g3": "  ", "h3": "  ",
    "a2": "wp1", "b2": "wp2", "c2": "wp3", "d2": "wp4", "e2": "wp5", "f2": "wp6", "g2": "wp7", "h2": "wp8",
    "a1": "WR1n", "b1": "WN1", "c1": "WB1", "d1": "WQ1", "e1": "WK1n", "f1": "WB2", "g1": "WN2", "h1": "WR2n"
}"""