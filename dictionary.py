month_conversion = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
print(month_conversion[1])
print(month_conversion.get(13, "Oops, invalid key"))

month_conversion = {
    "Jan": "January", # keys can be either strings or numbers!
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(month_conversion["Jan"])
print(month_conversion.get("Luv"))
print(month_conversion.get("Luv", "Oops, invalid key")) # the .get function allows you to set a default value for a non-existent key input
