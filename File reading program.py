while(True):
    try:
        filesname = input("File name")
        with open(filesname, 'r') as rc:
            print(rc.name)
            contents = rc.read(1000)
            print(contents,end='\n')
    except:
        print("Error")

