#Code Wars
def multi_table(number):
    idk = ""
    for i in range (1, 11):
        if i < 10:
            idk += f"{i} * {number} = {i * number}\n"
        else:
            idk += f"{i} * {number} = {i * number}"
        return idk