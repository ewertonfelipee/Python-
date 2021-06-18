# TIME CONVERSION

def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%d:%d:%d" % (hour, min, sec)

# Driver program
n = int(input())
print(convert(n))