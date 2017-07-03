def making_table(file_name):
    with open(file_name, "r") as f:
        table = f.read().split("\n")
        return table



def get_most_played(file_name):
    most_sold = 0
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t") ]
        if float(table[line][1]) > float(most_sold):
            most_sold = table[line][1]                          #Ha talál nagyobbat mint az elözö akkor lecseréli.
            name_of_most_sold = (table[line][0])
    return name_of_most_sold


def sum_sold(file_name):
    sum_sold = 0
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t") ]
        sum_sold += float(table[line][1])
    return sum_sold


def get_selling_avg(file_name):
    table = making_table(file_name)
    avarage_selling = float(sum_sold(file_name)) / (float(len(table)))
    return avarage_selling 


def count_longest_title(file_name):
    lenght_of_title = 0
    table = making_table(file_name)
    for line in range(len(table) - 1):
        table[line] = [tabulator for tabulator in table[line].split("\t") ]
        if len(table[line][0]) > lenght_of_title:
            lenght_of_title = len(table[line][0])
    return lenght_of_title


def get_date_avg(file_name):
    total_date = 0
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t") ]
        total_date += int(table[line][2])
    avarage_selling = total_date / (len(table))
    if avarage_selling % 1 != 0:        #Ha 1-el osztva nincs maradék akkor kerek szám
        avarage_selling += 1            
    avarage_selling = int(avarage_selling)  #lefele kerekités
    return avarage_selling


def get_game(file_name, title):
    game_properties = []
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t") ]
        if table[line][0] == title:
            for words in table[line]:
                if words.isdigit():                         #Ha kerek szám
                    game_properties.append(int(words))
                else:
                    try:
                        words = float(words)                #Ha nem tudjuk floatá alakitani, akor string
                        game_properties.append(words)
                    except :
                        game_properties.append(words)
    return game_properties


def count_grouped_by_genre(file_name):
    genre_dictionary = {}
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t") ]
        try:                                                
            if genre_dictionary[table[line][3]] > 0:        #Ha van már ilyen akkor egyet adunk hozzá
                genre_dictionary[table[line][3]] +=1
        except:                                             #Különben csinálunk egy uj Key-t
                genre_dictionary[table[line][3]] = 1
    return(genre_dictionary)


#def get_date_ordered(file_name):
#    final_list = []
#    ready_list = []
#    unordered_dictionary = {}
#    temp_date = 0
#        table = making_table(file_name)
#        for line in range(len(table)):
#            table[line] = [tabulator for tabulator in table[line].split("\t") ]
#            unordered_dictionary[table[line][0]] = table[line][2]
#    ordered_dictionary = [(k, unordered_dictionary[k]) for k in sorted(unordered_dictionary, key = unordered_dictionary.get, reverse = True)]
#    for key in ordered_dictionary:
#        final_list.append(key)
    #print(final_list)
    #final_list[1] = [final_list[1][0],"asd"]
    #print(final_list[1])
#   for x in range(len(final_list)-1):
#       if final_list[x+1][1] > final_list[x][1]:
#           temp_name = final_list[x+1]
#           final_list[x+2]=final_list[+1]
#           final_list[x+1]=temp_name
#   for x in final_list:
#       ready_list.append(x[0])
#   return ready_list
#
#et_date_ordered("game_stat.txt")

# Report functions
