# Assignment 6.5

# str = 'X-DSPAM-Confidence: 0.8475'
# ipos = str.find(':')
# piece = str[ipos+2:]
# value = float(piece)
# print(value)

str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
# print(ipos)
piece = str[ipos+2:]
# print(piece)
# print(piece+42.0)
value = float(piece)
print(value)
# print(value+42.0)
