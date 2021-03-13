# Find the kind of error in running and use it in try and except.
def divisionBy(num):
    try:
        return(100/num)
    except ZeroDivisionError:
        return ("Cant divide a number by 0")
print(divisionBy(20))
# 5
print(divisionBy(0))
# Cant divide a number by 0




def val(num):
    try:
        if num >=100:
            print(num)
        else:
            print(num+100)
    except ValueError:
        return ("Did not enter a number")
print(val(99))
# 199
print(val('g'))
# Did not enter a number
