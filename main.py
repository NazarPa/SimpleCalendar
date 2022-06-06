import calendar

yy = int(input('Enter the year: '))  # year
mm = int(input('Enter the month:' ))    # month

try:
    print('\n\n' + calendar.month(yy, mm))
except:
    print('\nWrong value!')
