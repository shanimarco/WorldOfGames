def add_score(difficulty):
    point_of_winning = (int(difficulty) * 3) + 5
    try:
        my_file = open("Score.txt", 'r')
        old_point = my_file.read()
        new_score = int(old_point) + (point_of_winning)
    except:
        my_file = open("Score.txt", 'w')
        new_score = point_of_winning
    finally:
        with open("Score.txt", 'w') as my_file:
            my_file.write(str(new_score))
            my_file.close()

