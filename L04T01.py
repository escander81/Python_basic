from sys import argv
def income():
    try:
        rate, hrs, bonus = map(float, argv[1:])
        print(f"Salary: (rate * hrs + bonus)")
    except ValueError:
        print('Enter rate, working hours, bonus: ')
income()