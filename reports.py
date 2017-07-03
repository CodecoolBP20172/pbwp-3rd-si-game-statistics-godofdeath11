#from export import export_decide
def making_table(file_name):
    with open(file_name, "r") as f:
        table = f.read().split("\n")
        return table

def count_games(file_name):
    number_of_games = 0
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t")]
        number_of_games += 1
    return number_of_games


def decide(file_name, year):
    contains = 0
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t")]
        if str(year) == table[line][2]:
            contains = + 1
    if contains > 0:  # Ha egyszer is adott hozzá akkor van olyan év
        return True
    else:
        return False


def get_latest(file_name):
    latest_date = 0
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t")]
        if int(table[line][2]) > int(latest_date):
           latest_date = table[line][2]
           game = table[line][0]  # Addig cseréli le amig talál késöbbi évet
    return game


def count_by_genre(file_name, genre):
    number_of_genre = 0
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t")]
        if genre == table[line][3]:
            number_of_genre += 1
    return number_of_genre


def get_line_number_by_title(file_name, title):
    line_number = 0
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t")]
        if title == table[line][0]:
            line_number = line + 1
    return line_number


def sort_abc(file_name):
    list_of_games = []
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t")]
        list_of_games.append(table[line][0])
    list_of_games.sort()
    return list_of_games


def get_genres(file_name):
    list_of_genres = []
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t")]
        list_of_genres.append(table[line][3])
    set_of_genres = set(list_of_genres)  # eltuntetkuk az ismétlödéseket
    list_of_genres = list(set_of_genres)
    list_of_genres.sort(key=str.lower)
    return list_of_genres


def when_was_top_sold_fps(file_name):
    most_sold = 0
    date_of_relase = 0
    table = making_table(file_name)
    for line in range(len(table)):
        table[line] = [tabulator for tabulator in table[line].split("\t")]
        if table[line][3] == "First-person shooter":
            if float(table[line][1]) > float(most_sold):
                most_sold = table[line][1]
                date_of_relase = int(table[line][2])  # Addig cseréli amig talál nagyobbat
    return date_of_relase


count_games("game_stat.txt")
