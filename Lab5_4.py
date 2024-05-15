def fixRating(ratingList):
    return [4 if x == 3 else x for x in ratingList if x !=2]

one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print(fixRating(one))
print(fixRating(two))
print(fixRating(three))