

class Validators:
    def completion(char):
        if char != 'x':
            return False
        return True

    def priority(string):
        # format: (A)
        if not string[0] == '(' and string[2] == ')':
            return False
        priority_value = ord(string[1]) - 41 - 24
        if priority_value > 25 or priority_value < 0:
            return False
        return True

    def date(string):
        # foramt: YYYY-MM-DD
        string = string.strip()
        split = string.split('-')
        if len(split) != 3:
            return False
        year = split[0]
        month = split[1]
        day = split[2]

        if len(year) != 4:
            return False
        if len(month) != 2:
            return False
        if len(day) != 2:
            return False

        err = True
        for date in split:
            try:
                temp = int(date)
            except ValueError:
                err = False
        return err
