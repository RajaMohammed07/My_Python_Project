def process_roster(roster):

  updated_roster = []

  high_performers = 0



  for driver in roster:

    temp = list(driver)

    temp.append("active")

    updated_roster.append(tuple(temp))



    if driver[1] > 50:

      high_performers += 1



  names = []

  for driver in updated_roster:

    names.append(driver[0])



  names.sort()



  return {

    "updated_roster": updated_roster,

    "sorted_names": names,

    "high_performers": high_performers

  }





if __name__ == "__main__":

  sample_roster = [

    ("Arjun", 65),

    ("Priya", 42),

    ("Rahul", 80),

    ("Meena", 50),

    ("Karan", 95),

    ("Divya", 35),

    ("Vikram", 60),

  ]



  print(process_roster(sample_roster))