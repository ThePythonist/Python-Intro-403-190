import datetime


def show_age(birth):
    # now = str(datetime.datetime.now())
    # thisyear = now[:4]
    # age = int(thisyear) - birth
    # print(age)
    # ------------------------------------------
    # year = datetime.datetime.now().year
    # age = year - birth
    # print(age)
    # ------------------------------------------
    year = datetime.datetime.now().strftime("%Y")
    age = int(year) - birth
    print(age)


show_age(2009)
