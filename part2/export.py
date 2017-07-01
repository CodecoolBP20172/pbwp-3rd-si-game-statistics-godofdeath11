
def export_get_most_played(file_name):
    most_sold = 0
    with open(file_name, "r") as f:
        table = f.read().strip("\t").split("\n")
        for line in range(len(table)):
            table[line] = [splits for splits in table[line].split("\t") if splits is not ""]
            if float(table[line][1]) > float(most_sold):
                most_sold = table[line][1]   
                name_of_most_sold = (table[line][0])
    with open("answers.txt" "a")
        w.write( name_of_most_sold + '\n')


def export_sum_sold(file_name):
    sum_sold = 0
    with open(file_name, "r") as f:
        table = f.read().strip("\t").split("\n")
        for line in range(len(table)):
            table[line] = [splits for splits in table[line].split("\t") if splits is not ""]
            sum_sold += float(table[line][1])
    with open("answers.txt" "a")
        w.write( sum_sold + '\n')


def export_get_selling_avg(file_name):
    with open(file_name, "r") as f:
        table = f.read().strip("\t").split("\n")
        avarage_selling = float(sum_sold(file_name)) / (float(len(table)))
    with open("answers.txt" "a")
        w.write( avarage_selling  + '\n')


def export_count_longest_title(file_name):
    lenght_of_title = 0
    with open(file_name, "r") as f:
        table = f.read().strip("\t").split("\n")
        for line in range(len(table) - 1):
            table[line] = [splits for splits in table[line].split("\t") if splits is not ""]
            if len(table[line][0]) > lenght_of_title:
                lenght_of_title = len(table[line][0])
    with open("answers.txt" "a")
        w.write( lenght_of_title + '\n')


def export_get_date_avg(file_name):
    with open(file_name, "r") as f:
        total_date = 0
        table = f.read().strip("\t").split("\n")
        for line in range(len(table)):
            table[line] = [splits for splits in table[line].split("\t") if splits is not ""]
            total_date += int(table[line][2])
    avarage_selling = total_date / (len(table))
    if avarage_selling % 1 != 0:
        avarage_selling += 1 
    avarage_selling = int(avarage_selling)
    with open("answers.txt" "a")
        w.write( avarage_selling + '\n')


def export_get_game(file_name, title):
    game_properties = []
    with open(file_name, "r") as f:
        table = f.read().strip("\t").split("\n")
        for line in range(len(table)):
            table[line] = [splits for splits in table[line].split("\t") if splits is not ""]
            if table[line][0] == title:
                for words in table[line]:
                    if words.isdigit():
                        game_properties.append(int(words))
                    else:
                        try:
                            words = float(words)
                            game_properties.append(words)
                        except :
                            game_properties.append(words)
    with open("answers.txt" "a")
        w.write( game_properties + '\n')


def export_count_grouped_by_genre(file_name):
    genre_dictionary = {}
    with open(file_name, "r") as f:
        table = f.read().strip("\t").split("\n")
        for line in range(len(table)):
            table[line] = [splits for splits in table[line].split("\t") if splits is not ""]
            try:
                if genre_dictionary[table[line][3]] > 0:
                    genre_dictionary[table[line][3]] +=1
            except:
                    genre_dictionary[table[line][3]] = 1
    with open("answers.txt" "a")
        w.write((genre_dictionary + '\n'))


def export_get_date_ordered(file_name):
    unordered_dictionary = {}
    final_list = []
    temp_name = 0
    temp_date = 0
    with open(file_name, "r") as f:
        table = f.read().strip("\t").split("\n")
        for line in range(len(table)):
            table[line] = [splits for splits in table[line].split("\t") if splits is not ""]
            unordered_dictionary[table[line][0]] = table[line][2]
    ordered_dictionary = [(k, unordered_dictionary[k]) for k in sorted(unordered_dictionary, key = unordered_dictionary.get, reverse = True)]
    for key in ordered_dictionary:
        final_list.append(key[0])
    with open("answers.txt" "a")
        w.write( final_list + '\n')

# Report functions
