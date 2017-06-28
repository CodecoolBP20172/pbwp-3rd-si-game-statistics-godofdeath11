def export_count_games(file_name):
    with open(file_name, "r") as f:
        number_of_games = len(f.readlines())
    with open("answers.txt", "a") as w:
        w.write(number_of_games + '\n')


def export_decide(file_name, year):
    if str(year) in open(file_name).read():
        with open("answers.txt", "a") as w:
            w.write("True" + '\n')
    else:
        with open("answers.txt" "a") as w:
            w.write("False" + '\n')


def export_get_latest(file_name):
    latest_date = 0
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            if int(tablazat[line][2]) > int(latest_date):
                latest_date = tablazat[line][2]
                game = tablazat[line][0]
    with open("answers.txt" "a") as w:
        w.write(game + '\n')


def export_count_by_genre(file_name, genre):
    number_of_genre = 0
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            if genre in tablazat[line][3]:
                number_of_genre += 1
    with open("answers.txt" "a") as w:
        w.write(number_of_genre + '\n')


def export_get_line_number_by_title(file_name, title):
    line_number = 0
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            if title in tablazat[line][0]:
                line_number = line + 1
    with open("answers.txt" "a") as w:
        w.write(line_number + '\n')


def export_sort_abc(file_name):
    list_of_games = []
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            list_of_games.append(tablazat[line][0])
    list_of_games.sort()
    with open("answers.txt" "a") as w:
        w.write(list_of_games + '\n')


def export_get_genres(file_name):
    list_of_genres = []
    with open(file_name, "r") as f:
        tablazat = f.read().strip("\t").split("\n")
        for line in range(len(tablazat) - 1):
            tablazat[line] = [splits for splits in tablazat[line].split("\t") if splits is not ""]
            list_of_genres.append(tablazat[line][3])
    set_of_genres = set(list_of_genres)
    list_of_genres = list(set_of_genres)
    list_of_genres.sort(key=str.lower)
    with open("answers.txt" "a") as w:
        w.write(list_of_genres + '\n')


def export_when_was_top_sold_fps(file_name):
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
    with open("answers.txt" "a") as w:
        w.write(date_of_relase + '\n')
# Export functions
