class n_list:
    def nested(self):
        n = int(input())
        list3 = []
        for i in range(n):   
            name = input()
            grade = float(input())
            list3.append([name,grade])
        list3.sort(key=lambda x: x[1])
        list3.pop(0)
        print(list3[1][0])
        print(list3[0][0])

nested_list = n_list()
nested_list.nested()