# Extract_data
record = ["Jimmy", "Smith", (8, 12, 1928), "piano"]
# record = ["Wes", "Montgomery", (6, 3, 1923), "guitar"]
last_name = record[1]
fist_name = record[0]
born = record[2]
born_year = record[2][2]
job = record[-1]
print(f"Last name: {last_name}"
      f"\nBorn: {born}"
      f"\n{fist_name} was born in {born_year} and was a great {job} player.")