def find_cube_pairs(target):
    solutions = []
    max_num = round(target ** (1/3))

    for a in range(1, max_num + 1):
        for b in range(a, max_num + 1):
            if a**3 + b**3 == target:
                solutions.append((a,b))

    return solutions

pairs = find_cube_pairs(1729)
print("Valid cube pairds for 1729:")
for a,b in pairs:
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")