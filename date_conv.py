# Given a date string in the form Day Month Year, where:
#
# Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
#  "Sep", "Oct", "Nov", "Dec"}.
# Year is in the range [1900, 2100].
# Convert the date string to the format YYYY-MM-DD, where:
#
# YYYY denotes the 4 digit year.
# MM denotes the 2 digit month.
# DD denotes the 2 digit day.
# Input: date = "20th Oct 2052"
# Output: "2052-10-20"
# Input: date = "6th Jun 1933"
# Output: "1933-06-06"
# Input: date = "26th May 1960"
# Output: "1960-05-26"


def date_conv(inp):
    inp_split = inp.split(" ")
    month_map = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
                 "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                 "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    day_temp = inp_split[0]

    if len(day_temp) == 3:
        day = "0" + day_temp[0]
    else:
        day = day_temp[:2]

    year = inp_split[2]
    month = month_map[inp_split[1]]
    date = year+"-"+month+"-"+day
    return date


print(date_conv("5th Oct 2052"))
print(date_conv("26th May 1960"))
print(date_conv("6th Jun 1933"))
