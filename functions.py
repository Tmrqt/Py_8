#def write(data):
#    with open("contacts.txt", "a") as f:
#        f.write(data)

# def find_str(data):
#    with open("contacts.txt", "r") as f:
#        lst = f.readline()
#        for person in lst:
#            if data in person:
#                print(person) 

def person_data_select(person):
    persons_list = []
    with open("contacts.txt", "r") as f:
        lst = f.readline()
        for line in lst:
            if person in line:
                persons_list.append(line)
    return persons_list, lst

def person_data_delete(lst, persons_list, num_line, data_person):
    with open("contacts.txt", "w") as f:
        for line in lst:
            if persons_list[num_line-1] != line:
                f.write(line)
            else:
                f.write(data_person)
    print("Изменено")

def person_data_change(lst, persons_list, num_line):
    with open("contacts.txt", "w") as f:
        for line in lst:
            if persons_list[num_line-1] != line:
                f.write(line)
            else:
                continue
    print("Удалено")