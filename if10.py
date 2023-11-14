def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0:  Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Freezing"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30:  "Very Cold"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<0:
        if 1<temp and temp<10:
            if 10<temp and temp<21:
                if 20<temp and temp<31:
                    if 30<temp and temp<41:
                        if 40<temp:
                            return"Freezing"
                        return  "Very Cold"
                    return  "Cold"
                return "Normal"
            return "Hot"
        return "Very Hot"
    print(main(25))
                        