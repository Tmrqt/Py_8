import functions
import ask

while True:
    q = ask()
    if q == 1:
       person = ask.find_str()
       persons_list, lst = functions.person_data_select(person)
       num_line = ask.choose_str() 
       data_person = ask.get_data()
       functions.person_data_change(lst, persons_list, num_line, data_person)
    elif q == 2:       
        person = ask.find_str()
        persons_list, lst = functions.person_data_select(person)
        num_line = ask.choose_str() 
        data_person = ask.get_data()
        functions.person_data_delete(lst, persons_list, num_line)  
    else:
        break
