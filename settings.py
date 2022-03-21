with open("settings.txt") as f:
    for i in f.read().split("\n"):
        if "size" in i:
            size = i[5:].split(" ")
            W, H = int(size[0]), int(size[1])
            size = (W, H)
        if "FPS" in i:
            FPS = int(i[4:])
        if "hp" in i:
            hp = int(i[3:])
        if "step" in i:
            step = int(i[5:])
        if "cannon_count" in i:
            cannon_count = int(i[len('cannon_count')+1:])