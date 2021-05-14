import csv


def read_csv():
    votes = []
    i = 15
    last_id = 0
    with open('C:\\Users\\micha\\Downloads\\1_wd.csv', 'r') as f:
        reader = csv.reader(f)
        for u_id, a, b in reader:
            if int(u_id) > last_id:
                last_id = int(u_id)
        last_user_id_plus_1 = last_id + 1
    for x in range(i, last_user_id_plus_1):
        dict_15 = {14: "'trudnoĹ›ci w pracy'", 15: "'kłopoty finansowe'", 16: "'problemy rodzinne'", 17: "'problemy uczuciowe'",
                   18: "'smutek i poczucie niskiej wartoĹ›ci'", 19: "'problemy na uczelni'", 20: "'inne'"}
        dict_17 = {22: "'regularne godziny wstawania'",
                   23: "'unikanie ĹşrĂłdeĹ‚ Ĺ›wiatĹ‚a niebieskiego minimum godzinÄ™ przed spaniem'",
                   24: "'ostatnia kawa 8h przed pĂłjĹ›ciem spaÄ‡ '", 25: "'obniĹĽenie temperatury w sypialni przed snem'",
                   26: "'wypicie szklanki wody przed snem'", 27: "'Ĺ‚ĂłĹĽko jedynie jako miejsce snu i aktywnoĹ›ci seksualnej'"}
        dict_24 = {34: "'chrapanie'", 35: "'mĂłwienie przez sen'", 36: "'nocne kurcze miÄ™Ĺ›ni'", 37: "'lunatykowanie'",
                   38: "'nie posiadam takiej osoby'"}

        with open('C:\\Users\\micha\\Downloads\\1_wd.csv', 'r') as file:
            reader = csv.reader(file)
            buf_list = [x]
            for user_id, question_id, answer in reader:
                #print(f'{user_id}, {question_id}, {answer}')
                if int(user_id) == x:
                    buf_list.append(f"'{answer}'")
        is_in_buf_lis(dict_15, buf_list)
        is_in_buf_lis(dict_17, buf_list)
        is_in_buf_lis(dict_24, buf_list)
        votes.append(buf_list)

    with open('C:\\Users\\micha\\Downloads\\2_wd.csv', 'w', newline='') as file_out:
        writer = csv.writer(file_out)
        writer.writerows(votes)


def is_in_buf_lis(dict_n, buf_list):
    for key in dict_n:
        if dict_n[key] not in buf_list:
            buf_list.insert(key, "?")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_csv()
