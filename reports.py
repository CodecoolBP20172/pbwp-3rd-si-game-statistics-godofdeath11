#from printing import print_decide,print_count_games,print_get_latest,print_count_by_genre,print_get_line_number_by_title,print_sort_abc,print_get_genres,print_when_was_top_sold_fps
#from export import export_decide


def count_games(file_name):
    number_of_games = 0
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            number_of_games +=1
    return number_of_games


def decide(file_name, year):
    contains = 0
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            if str(year) == tablazat[line][2]:
                contains =+ 1
    if contains > 0:
        return True
    else:
        return False


def get_latest(file_name):
    latest_date = 0
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            if int(tablazat[line][2]) > int(latest_date):
                latest_date = tablazat[line][2]
                game = tablazat[line][0]
    return game


def count_by_genre(file_name, genre):
    number_of_genre = 0
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            if genre in tablazat[line][3]:
                number_of_genre += 1
    return number_of_genre


def get_line_number_by_title(file_name, title):
    line_number = 0
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            if title == tablazat[line][0]:
                line_number = line + 1
    return line_number


def sort_abc(file_name):
    list_of_games = []
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            list_of_games.append(tablazat[line][0])
    list_of_games.sort()
    return list_of_games


def get_genres(file_name):
    list_of_genres = []
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            list_of_genres.append(tablazat[line][3])
    set_of_genres = set(list_of_genres)
    list_of_genres = list(set_of_genres)
    list_of_genres.sort(key=str.lower)
    return(list_of_genres)


def when_was_top_sold_fps(file_name):
    most_sold = 0
    date_of_relase = 0
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            if tablazat[line][3] == "First-person shooter":
                if float(tablazat[line][1]) > float(most_sold):
                    most_sold = tablazat[line][1]
                    date_of_relase = int(tablazat[line][2])
    return date_of_relase
count_games("game_stat.txt")
