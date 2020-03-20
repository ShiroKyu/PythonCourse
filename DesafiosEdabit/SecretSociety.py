'''
society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"

society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"

society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]) ➞ "CJMPRR"
'''


def society_name(friends):
    friends = sorted(friends)
    sName = [s[0] for s in friends]
    return ''.join(sName)


def society_name2(friends): return ''.join(sorted(i[0] for i in friends))


print(society_name2(["Phoebe", "Chandler",
                     "Rachel", "Ross", "Monica", "Joey"]))
