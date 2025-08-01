def main():
    time_float = convert(input('Whats the time? ')) #input('Whats the time?').split(':') = time
    if 7 <= time_float <= 8:
        print('breakfast time')
    elif 12 <= time_float <= 13:
        print('lunch time')
    elif 18 <= time_float <= 19:
        print('dinner time')

def convert(time):
    time = time.split(':')
    time = [float(i) for i in time]
    time = time[0] + time[1]/60
    return time

if __name__ == "__main__":
    main()
