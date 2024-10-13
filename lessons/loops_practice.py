"""Practice of for Loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]
# tell every pet they're a good boy
for elem in pets:
    print(f"Good boy, {elem}!")  # "good boy, " + elem + "!"


names: list[str] = ["Alyssa", "Janet", "Varinda"]
# print each index: name
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
    # idx prints numbers, names[idx] prints names
