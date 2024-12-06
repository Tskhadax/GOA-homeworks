#Code Wars
geese = ["african","Roman Tufted","Toilouse","Piligrim"]
def goose_filter(birds):
    for i in geese:
        for elements in birds:
            if i == elements:
                birds.remove(i)
    return birds