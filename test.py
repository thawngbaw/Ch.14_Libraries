from my_func import yoda

def main():
    yoda()


print("The __name__ variable is:", __name__)


if __name__ == "__main__":
    yoda()
    print("This is being run directly!")
else:
    print("this is being import")
