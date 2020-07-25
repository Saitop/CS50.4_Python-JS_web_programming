s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

s.remove(2)

print(s)
print(f"The set has {len(s)} elements.")

s2 = set([3,3,3,2,1])
print(s2)