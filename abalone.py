def find_measurement_prompt(determiner):
    print(f"Find what {determiner}?\n"
          "  a - Length\n"  # 2
          "  b - Diameter\n"  # 3
          "  c - Height\n"  # 4
          "  d - Whole weight\n"  # 5
          "  e - Shucked weight\n"  # 6
          "  f - Viscera Weight\n"  # 7
          "  g - Shell Weight\n"  # 8
          "  h - Rings\n"  # 9
          "  i - Feb temp\n"  # 16
          "  j - Economic value\n"  # 18
          "  m - Find another measurement\n")


def action_choice_calculations(determiner):
    print(f"You are finding {determiner}\n")
    while True:
        find_measurement_prompt(determiner)
        user_choice = input("Your choice: ").replace(" ", "")
        print()
        if user_choice == "m":
            break
        if user_choice == "a":
            user_choice_calculations(determiner, "length")
        elif user_choice == "b":
            user_choice_calculations(determiner, "diameter")
        elif user_choice == "c":
            user_choice_calculations(determiner, "height")
        elif user_choice == "d":
            user_choice_calculations(determiner, "whole weight")
        elif user_choice == "e":
            user_choice_calculations(determiner, "shucked weight")
        elif user_choice == "f":
            user_choice_calculations(determiner, "viscera weight")
        elif user_choice == "g":
            user_choice_calculations(determiner, "shell weight")
        elif user_choice == "h":
            user_choice_calculations(determiner, "rings")
        elif user_choice == "i":
            user_choice_calculations(determiner, "feb temp")
        elif user_choice == "j":
            user_choice_calculations(determiner, "economic value")
        else:
            print("Invalid Choice. Try Again")
        print()


def find_base_source(determiner, scale):
    print(f"Find {determiner} {scale} based on?\n"
          f"  a - Gender\n"  # 1
          f"  b - Collector ID\n"  # 10
          f"  c - Organization\n"  # 13
          f"  d - Water Region ID\n"  # 15
          f"  e - Category\n"  # 17
          f"  g - Go back\n")


def user_choice_calculations(determiner, scale):
    while True:
        find_base_source(determiner, scale)
        user_base = input("Your Choice: ").replace(" ", "")
        if user_base == "g":
            break
        if user_base == "a":
            base_source_calculations(abalone_data, determiner, scale, "gender")
        elif user_base == "b":
            base_source_calculations(abalone_data, determiner, scale, "collector id")
        elif user_base == "c":
            base_source_calculations(abalone_data, determiner, scale, "organization")
        elif user_base == "d":
            base_source_calculations(abalone_data, determiner, scale, "water region")
        elif user_base == "e":
            base_source_calculations(abalone_data, determiner, scale, "category")
        else:
            print("Invalid choice, try again")
        print()


def base_source_calculations(data, determiner, scale, base):
    import numpy as np
    import statistics

    num = 2
    if scale == "length":
        num = 2
    elif scale == "diameter":
        num = 3
    elif scale == "height":
        num = 4
    elif scale == "whole weight":
        num = 5
    elif scale == "shucked weight":
        num = 6
    elif scale == "viscera weight":
        num = 7
    elif scale == "shell weight":
        num = 8
    elif scale == "rings":
        num = 9
    elif scale == "feb temp":
        num = 16
    elif scale == "economic value":
        num = 18

    measurement = np.mean
    if determiner == "average":
        measurement = np.mean
    elif determiner == "maximum":
        measurement = max
    elif determiner == "minimum":
        measurement = min
    elif determiner == "standard deviation":
        measurement = statistics.stdev
    elif determiner == "variance":
        measurement = statistics.variance


    group = 1
    if base == "gender":
        group = 1
    elif base == "collector id":
        group = 10
    elif base == "organization":
        group = 13
    elif base == "water region":
        group = 15
    elif base == "category":
        group = 17

    source_dict = {}
    for row in data:
        classification = row[group]
        if classification in source_dict:
            source_dict[classification].append(row[num])
        else:
            source_dict[classification] = [row[num]]
    source_list = sorted(source_dict.items())

    for item in source_list:
        print(f"{item[0]}: {measurement(item[1]):.5f}")


if __name__ == "__main__":
    import csv
    import numpy as np

    user_file = input("Enter Abalone Data File: ").lower()
    print()

    with open(user_file, "r") as csvfile:
        abalone_reader = csv.reader(csvfile, delimiter=",")
        next(abalone_reader)

        abalone_data = []
        for row in abalone_reader:
            abalone_data.append([row[0],  # ID
                                 row[1],  # Gender
                                 float(row[2]),  # Length
                                 float(row[3]),  # Diameter
                                 float(row[4]),  # Height
                                 float(row[5]),  # Whole Weight
                                 float(row[6]),  # Shucked Weight
                                 float(row[7]),  # Viscera Weight
                                 float(row[8]),  # Shell Weight
                                 int(row[9]),  # Rings
                                 int(row[10]),  # Collector ID
                                 row[11].strip(),  # Collector First name
                                 row[12].strip(),  # Collector Last name
                                 row[13].strip(),  # Collector organization
                                 int(row[14]),  # Water ID
                                 row[15].strip(),  # Water Region
                                 float(row[16])  # Feb Temp
                                 # row[17] Category
                                 # int(row[18]) Economic Value
                                 ])

    for row in abalone_data:
        value = 1 + ((1 / 3) * (row[2] - 0.5)) + ((1 / 3) * (row[3] - 0.4)) + ((1 / 3) * (row[4] - 0.4))
        abalone_value = value * row[5] * 0.5

        if (
                ((row[9] > 15) and (row[1] == "I")) or
                ((row[1] == "M") and (row[2] > 0.75)) or
                (((row[8] > 0.8) and (row[6] > 0.5)) or row[6] > 1.2)
        ):
            row.append("I")
            row.append(abalone_value * 1.5)
        elif (
                ((row[8] < 0.4) and (row[6] < 0.4)) or
                (((row[9] > 15) and (row[1] == "M")) or ((row[9] > 18) and (row[1] == "F"))) or
                (row[2] < 0.36)
        ):
            row.append("II")
            row.append(abalone_value * 0.8)
        else:
            row.append("III")
            row.append(abalone_value)

    while True:
        print("Select an action to take:\n"
              "  a - Find average\n"
              "  b - Find maximum\n"
              "  c - Find minimum\n"
              "  d - Find standard deviation\n"
              "  e - Find variance\n"
              "  f - Find abalone\n"
              "  q - quit\n")

        user_action = input("Your choice: ").replace(" ", "")
        if user_action == "q":
            break
        if user_action == "a":
            action_choice_calculations("average")
        elif user_action == "b":
            action_choice_calculations("maximum")
        elif user_action == "c":
            action_choice_calculations("minimum")
        elif user_action == "d":
            action_choice_calculations("standard deviation")
        elif user_action == "e":
            action_choice_calculations("variance")
        elif user_action == "f":
            while True:
                user_id = input("\nEnter Abalone ID (press 'g' to Go Back): ").replace(" ", "")
                if user_id == 'g':
                    break

                user_result = "none"
                for row in abalone_data:
                    if user_id == row[0]:
                        user_result = row
                    else:
                        continue

                if user_result != "none":
                    print(f"Gender: {user_result[1]}\n"
                          f"Length: {user_result[2]}\n"
                          f"Diameter: {user_result[3]}\n"
                          f"Height: {user_result[4]}\n"
                          f"Whole Weight: {user_result[5]}\n"
                          f"Shucked Weight: {user_result[6]}\n"
                          f"Viscera Weight: {user_result[7]}\n"
                          f"Shell Weight: {user_result[8]}\n"
                          f"Rings: {user_result[9]}\n"
                          f"Collector ID: {user_result[10]}\n"
                          f"Collector First Name: {user_result[11]}\n"
                          f"Collector Last Name: {user_result[12]}\n"
                          f"Collector Organization: {user_result[13]}\n"
                          f"Water ID: {user_result[14]}\n"
                          f"Water Region: {user_result[15]}\n"
                          f"Feb Temp: {user_result[16]}\n"
                          f"Category: {user_result[17]}\n"
                          f"Economic Value: {user_result[18]:.5f}\n")
                else:
                    print("Abalone does not exist, try again")
        else:
            print("Invalid choice. Try again")
        print()
