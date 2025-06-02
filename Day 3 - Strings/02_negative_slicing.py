name = "Germany"

negativeSlicing = name[-6:-1]
negativeSlicing2 = name[1:6]
print(negativeSlicing)
print(negativeSlicing2)

print(name[:6])
print(name[3:])

# slicing with skip value

b = "abcdefghijklmnopqestuvwxyz"
sliceSkip = b[1:9]
sliceSkip2 = b[1:9:3]
print(sliceSkip)
print(sliceSkip2)
