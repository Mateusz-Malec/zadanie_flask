users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}]

polish_users = [user for user in users if user.get("country") == "Poland"]
print(polish_users)

numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]

sum_of_first_10_elements = sum(numbers[5:15])
print(sum_of_first_10_elements)

powers_of_2 = [2 ** i for i in range(1, 21)]
print(powers_of_2)
