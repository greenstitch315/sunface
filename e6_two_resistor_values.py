import sys

E6_BASE = [1.0, 1.5, 2.2, 3.3, 4.7, 6.8]

def e6_values(min_ohm, max_ohm):
    values = set()
    decade = 1
    while decade <= max_ohm:
        for b in E6_BASE:
            v = round(b * decade, 6)
            if min_ohm <= v <= max_ohm:
                values.add(v)
        decade *= 10
    return sorted(values)

def combos(values):
    results = {}
    for i, r1 in enumerate(values):
        for r2 in values[i:]:
            total = round(r1 + r2, 6)
            results.setdefault(total, []).append((r1, r2))
    return dict(sorted(results.items()))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <min_ohm> <max_ohm>")
        sys.exit(1)

    min_ohm, max_ohm = float(sys.argv[1]), float(sys.argv[2])
    base = e6_values(min_ohm, max_ohm)
    all_values = combos(base)
    print(f"{len(base)} E6 values from {base[0]} to {base[-1]}")
    print(f"{len(all_values)} distinct values achievable with two E6 resistors in series:\n")
    for total, pairs in all_values.items():
        pair_str = ", ".join(f"{r1}+{r2}" for r1, r2 in pairs)
        print(f"{total} = {pair_str}")
