def family_members():
  """
  This function allows the user to enter the 5 names of their family members and their corresponding ages from the keyboard.
  It displays each family member's name with their corresponding age.
  It calculates and displays the sum of all ages and the average.
  It prints "the family is mature" if the average age is greater than 60, else "it's young".
  """

  sum_of_ages = 0
  for i in range(5):
    name = input("Enter the name of family member {}: ".format(i + 1))
    age = int(input("Enter the age of family member {}: ".format(i + 1)))
    print("{} is {} years old.".format(name, age))
    sum_of_ages += age

  average_age = sum_of_ages / 5
  print("The sum of all ages is {}.".format(sum_of_ages))
  print("The average age is {}.".format(average_age))

  if average_age > 60:
    print("The family is mature.")
  else:
    print("The family is young.")

if __name__ == "__main__":
  family_members()
