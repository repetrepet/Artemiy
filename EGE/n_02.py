# (x ≡ ( w ∨ y)) ∨ ((w  → z ) ∧ (y  → w))
# F = 0

print('x y z w')
for x in range(0, 2):
  for y in range(0, 2):
    for w in range(0, 2):
      for z in range(0, 2):
        if ((x == (w or y)) or ((w <= z) and (y <= w))) == 0:
          print(x, y, z, w)

# =================================================

# f = (x ∧ ¬y) ∨ (y ≡ z ) ∨ w
# f = 0

print('x y z w')
for x in range(0, 2):
  for y in range(0, 2):
    for z in range(0, 2):
      for w in range(0, 2):
        if ((x and (not(y))) or (y == z) or w) == 0:
          print(x, y, z, w)

# =================================================

# ((x → y) ≡ (y → z)) ∧ (y ∨ w)
# f = 1

print('x y z w')
for x in range(0, 2):
  for y in range(0, 2):
    for z in range(0, 2):
      for w in range(0, 2):
        if (((x <= y) == (y <= z)) and (y or w)) == 1:
          print(x, y, z, w)

# =================================================

# ((y → x) ≡ (x → w)) ∧ (z ∨ x)
# f = 1

print('x y z w')
for x in range(0, 2):
  for y in range(0, 2):
    for z in range(0, 2):
      for w in range(0, 2):
        if (((y <= x) == (x <= w)) and (z or x)) == 1:
          print(x, y, z, w)

# =================================================

# Логическое выражение: (x ≡ ( w ∨ y)) ∨ ((w → z ) ∧ (y → w))
# F = 0 (ищем наборы, где выражение ложно)

print('x y z w')
for x in range(0, 2):
  for y in range(0, 2):
    for w in range(0, 2):
      for z in range(0, 2):
        if ((x == (w or y)) or ((w <= z) and (y <= w))) == 0:
          print(x, y, z, w)

# =================================================

# Логическое выражение: (x ∧ ¬y) ∨ (y ≡ z ) ∨ w
# F = 0 (ищем наборы, где выражение ложно)

print('x y z w')
for x in range(0, 2):
  for y in range(0, 2):
    for z in range(0, 2):
      for w in range(0, 2):
        if ((x and (not(y))) or (y == z) or w) == 0:
          print(x, y, z, w)

# =================================================

# Логическое выражение: ((x → y) ≡ (y → z)) ∧ (y ∨ w)
# F = 1 (ищем наборы, где выражение истинно)

print('x y z w')
for x in range(0, 2):
  for y in range(0, 2):
    for z in range(0, 2):
      for w in range(0, 2):
        if (((x <= y) == (y <= z)) and (y or w)) == 1:
          print(x, y, z, w)

# =================================================

# Логическое выражение: ((y → x) ≡ (x → w)) ∧ (z ∨ x)
# F = 1 (ищем наборы, где выражение истинно)

print('x y z w')
for x in range(0, 2):
  for y in range(0, 2):
    for z in range(0, 2):
      for w in range(0, 2):
        if (((y <= x) == (x <= w)) and (z or x)) == 1:
          print(x, y, z, w)
