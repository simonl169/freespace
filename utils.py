import shutil


def show_disk_space():

    total, used, free = shutil.disk_usage("/")

    if __name__ == "__main__":
        print("Total: %d GiB" % (total // (2**30)))
        print("Used: %d GiB" % (used // (2**30)))
        print("Free: %d GiB" % (free // (2**30)))

    return total, used, free

def show_free_perc():
    total, used, free = show_disk_space()
    percentage = free/total*100

    print("Total: %d GiB" % (total // (2 ** 30)))
    print("Used: %d GiB" % (used // (2 ** 30)))
    print("Free: %d GiB" % (free // (2 ** 30)))
    print("")

    print("Free: %d %%" % (percentage))

    return percentage
