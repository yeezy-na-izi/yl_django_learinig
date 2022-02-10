string = input()
i = 1
counter = 0
while string != 'И будет нам счастье!' and counter != 5:
    copy_string = string[:len(string) - i + 1:i + 1]
    if len(set(copy_string)) >= 7:
        print(string)
        counter += 1
    i += 1
    string = input()


def something(qwe: any):
    return qwe


something('123')
