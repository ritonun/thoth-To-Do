import datetime


def convert_priority_char_to_int(char):
    value = ord(char) - 41 - 24
    if value > 25 or value < 0:
        raise SyntaxError('Priority syntax has to be A-Z')
    return value

def convert_priority_int_to_char(integer):
    if integer > 25 or integer < 0:
        raise SyntaxError('Priority syntax has to be A-Z')
    value = chr(integer + 41 + 24)
    return value

def str_to_timestamp(date_str):
    time = datetime.datetime.strptime(date_str, "%Y-%M-%d")
    time = datetime.datetime.timestamp(time)
    return time

def timestamp_to_str(time):
    date = datetime.datetime.fromtimestamp(time).strftime('%Y-%M-%d')
    return date

def get_date_str():
    time = datetime.datetime.now().strftime('%Y-%M-%d')
    return time
