months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    date = get_date('Date: ')
    print(f'{date[0]}-{int(date[1]):02d}-{int(date[2]):02d}')



def get_date(date):
    ISO_8601 = {
        'Y': 0,
        'M': 0,
        'D': 0
    }

    while True:
        date1 = input(date).split('/')
        try:
            ISO_8601['Y'] = date1[2]
            ISO_8601['M'] = date1[0]
            ISO_8601['D'] = date1[1]
            if int(ISO_8601['M']) > 12 or int(ISO_8601['D']) > 31:
                raise IndexError
        except IndexError:
            date1 = ''.join(date1).split(' ')
            try:

                ISO_8601['Y'] = date1[2]
                ISO_8601['M'] = months.index(date1[0].title()) + 1
                if date1[1].find(',') == -1:
                    raise IndexError
                else:
                    ISO_8601['D'] = date1[1].replace(',','')

                if int(ISO_8601['Y']) < 0 or int(ISO_8601['D']) > 31:
                    raise IndexError
            except IndexError:
                pass
            except ValueError:
                pass
            else:
                ISO_date = (ISO_8601['Y'],ISO_8601['M'], ISO_8601['D'])
                return ISO_date
        except ValueError:
            pass
        else:
            ISO_date = (ISO_8601['Y'],ISO_8601['M'], ISO_8601['D'])
            return ISO_date




main()
