# This is a program that I am using to simulate outcomes for
# future Neuroscience MSc applications!
# Feel free to take the code and plug in your own ^_^

import random  # generates random numbers

# list of universities I like and their acceptance rates (in percent)
universities = [
    ("ETH Zürich", 10),
    ("KU Leuven", 25),
    ("UZH", 20),
    ("TU München", 20),
    ("EPFL", 25),
    ("MIT", 8),
    ("Cambridge", 10),
    ("UC London", 15),
    ("Melbourne", 40),
    ("UVienna", 40),
    ("Aarhus", 40),
    ("Edinburgh", 30),
    ("PSL Paris", 20)
]

# map each university to its country
countries = {
    "ETH Zürich": "Switzerland",
    "KU Leuven": "Belgium",
    "UZH": "Switzerland",
    "TU München": "Germany",
    "EPFL": "Switzerland",
    "MIT": "The United States",
    "Cambridge": "The United Kingdom",
    "UC London": "The United Kingdom",
    "Melbourne": "Australia",
    "UVienna": "Austria",
    "Aarhus": "Denmark",
    "Edinburgh": "The United Kingdom",
    "PSL Paris": "France"
}

print("Simulating ONE application round:\n")

# Single round simulation
acceptances_this_round = 0
accepted_schools = []
accepted_countries = set()

for name, acceptance_rate in universities:
    roll = random.randint(1, 100)

    if roll <= acceptance_rate:
        result = "ACCEPTED"
        acceptances_this_round += 1
        accepted_schools.append(name)
        accepted_countries.add(countries[name])
    else:
        result = "REJECTED"

    print(
        f"{name}: acceptance rate is {acceptance_rate}% | "
        f"random roll = {roll} → {result}"
    )

print(f"\nTotal acceptances this round: {acceptances_this_round}\n")

# list accepted schools
if accepted_schools:
    print("You were accepted to:")
    for s in accepted_schools:
        print(f" - {s}")
else:
    print("No acceptances this round. Try again next year! 😭")

print()

# welcome messages
if accepted_countries:
    for country in sorted(accepted_countries):
        print(f"Welcome to {country}!")
    print()

N = 10000  # simulate 10000 cycles
count_at_least_one = 0
count_at_least_three = 0

for _ in range(N):
    offers = 0
    for _, acceptance_rate in universities:
        roll = random.randint(1, 100)
        if roll <= acceptance_rate:
            offers += 1

    if offers >= 1:
        count_at_least_one += 1
    if offers >= 3:
        count_at_least_three += 1

p_at_least_one = count_at_least_one / N
p_at_least_three = count_at_least_three / N

print("After running", N, "simulated application rounds:")
print(f"- Chance of getting ≥ 1 acceptance: {p_at_least_one:.2%}")
print(f"- Chance of getting ≥ 3 acceptances: {p_at_least_three:.2%}")

