#Code Wars
def well(x):
    for i in range(len(x)):
        if x.count("good") == 1 or x.count("good") == 2:
            return "Pulish!"
        elif x.count("good") > 2:
            return "i smell a series!"
        else:
            return "Fail!"