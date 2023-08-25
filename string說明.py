# paragraph1 = "This planet has - or rather had - a problem, which was \
# this: most of the people living on it were unhappy for pretty much \
# of the time. Many solutions were suggested for this problem, but \
# most of these were largely concerned with the movements of small \
# green pieces of paper, which is odd because on the whole it wasn't \
# the small green pieces of paper that were unhappy."
#
# print(paragraph1)

paragraph2 = """This planet has - or rather had - a problem, which was
this: most of the people living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concerned with the movements of small
green pieces of paper, which is odd because on the whole it wasn't
the small green pieces of paper that were unhappy."""

ans = paragraph2.find('of')
ans = paragraph2[68:].find('of')
print(ans)