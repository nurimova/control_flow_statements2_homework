def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if number==1:
        return "Monday"
    if number==2:
        return"Tuesday"
    if number==3:
        return "Wednesday"
    if number==4:
        return "Thursday"
    if number==5:
        return "Friday"
    if number==6:
        return "Saturday"
    if number==7:
        return "Sunday"
    else:
        return "bunday hafta kuni yo'q"
print(main(5))