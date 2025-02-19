s = input()

if s[:2] == '12' and s[-2:] == 'AM':
    print('00' + s[2:-2])
elif s[-2:] == 'AM':
    print(s[:-2])
elif s[:2] == '12' and s[-2:] == 'PM':
    print(s[:-2])
else:
    print(str(int(s[:2]) + 12) + s[2:-2])