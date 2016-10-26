"My-music-collection" is an application that was designed for coursework purpose. It works on Levinux Enviroment provided by Advanced Web Technologies lecturer, Simon Wells. 
It can be accessed by following steps:


1. First you have click "PipulateWindows.vbs" which you can find on your computer inside the levinux-napier folder. 
2. When you cklick on it, the Levinux server will start working. You will see the loading page and after that a few options to choose. Select "2" to log in to the server.
3. You will be asked for username and password. Enter "tc" as username and "foo" as password.
4. Run "Putty.exe" to connect to the Levinux server through SSH connection.
5. In the putty's login window type "tc@localhost" in the "Host Name", choose port "2222".
6. At the bottom of the login window there is a button called "open" - click on it. Then insert password "foo" again. Now you should be connected via putty to your server.
7. In order to find the application type "cd coursework/ " and then "cd src /". To see the folder content type "ls".
8. Next type "python my-music-catalogue.py" to run the python application.
9. Access the applocation via any browser (Chrome, Firefox etc).
10. In the browser's address bar type "localhost:5000".
11. Now you should be able to see My Music Collection application.