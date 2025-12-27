import os

def Create_file(filename):
    try:
        with open(filename,"x") as f:
            print(f"File Name {filename}: Created Successfully!")

    except FileExistsError:
        print(f"File Name {filename} already exists!")

    except Exception as E:
        print("An error Occurred !")



def view_all_files(): 
    files = os.listdir()
    if not files:
        print("No file found!")
    else:
        print("Files in directory !")
        for file in files:
            print(file)         



def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully !")

    except FileExistsError:
        print("File Not Found")

    except Exception as e:
        print("An Error Occurred !")   


def read_file(filename):
    try:
        with open(filename,"r") as f:
            content = f.read()
            print(f"Content of '{filename}' : \n{content}")

    except FileExistsError:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print("An Error Occurred !")


def edit_file(filename):
    try:
        with open(filename,"a") as f:
            content = input("Enter data to add = ")
            f.write(content + "\n")

            print("Content added to {filename} Successful")


    except FileExistsError:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print("An Error Occurred !")




def main():
    while True:
        print("File Management App")
        print("1 : Create a File")  
        print("2 : Viwe all  Files")
        print("3 : Delete a File")
        print("4 : Read a File")
        print("5 : Edit File")
        print("6 : Exit File")   



        Choice = input("Enter Your Choice(1-6) =")

        if Choice == "1":
             filename = input("Enter the file name to create = ")
             Create_file(filename)



        elif Choice == "2":
            view_all_files()


        elif Choice == "3":
            filename = input("Enter the name of file you want to delete =")
            delete_file(filename)


        elif Choice == "4":
            filename = input("Enter file name to read = ")
            read_file(filename)


        elif Choice == "5":
            filename = input("Enter file name to edit =")
            edit_file(filename)


        elif Choice == "6":
            print("Closing the app.......")
            break

        else:
            print("In-Valid Syntax plase enter 1 to 6 number")



if __name__ == "__main__":
    main()                                           

     