class leap:
    def is_leap():
        year = int(input())
        if year / 4 == 0 or year % 4 == 0 and year != 2100: 
            print('True')
        else:
            print('False')

n = leap()
leap.is_leap()