import os

def hello_world():
    print("Hello World")
    print(os.listdir(os.getcwd()))

if __name__ == "__main__":
    hello_world()