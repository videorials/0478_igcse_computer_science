# >> -------------------- << import and return all data from file to array >>
def load_to_array(Filename):
    File = open(f"data/{Filename}", "r")
    Array = []
    for Item in File:
        Array.append(Item.replace("\n", ""))
    File.close()
    return Array


# >> -------------------- << import and return qty data from file to array >>
def load_qty_to_array(Filename, Qty):
    File = open(f"data/{Filename}", "r")
    Array = []
    Count = 0
    for Item in File:
        if Count < Qty:
            Array.append(Item.replace("\n", ""))
            Count = Count + 1
        else:
            break
    File.close()
    return Array