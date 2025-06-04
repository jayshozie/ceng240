MIT License
Copyright (c) 2025 Emir Baha Yıldırım
Please see the LICENSE file for more details.

-------------------------------------------------------------------------------

This markdown is a guide on installing Python and Visual Studio Code (VSCode)
to your system.

-------------------------------------------------------------------------------

# Python Installation

<details>
    <summary>Windows 11/10</summary>

You can install Python from [www.python.org/downloads/](https://www.python.org/downloads/).
When you go into the website, you'll see a yellow button that says
`Download Python 3.xx.x`, click on it and you should see it downloading its
installation files.

After the installation is done, click on that file and run it.

## Testing

<details>
    <summary>Windows 11</summary>

Search for `Terminal` in your Start menu, and hit enter. It should open
PowerShell CLI as default. Write the command,
```pwsh
python3 --version
```
to the command line and hit enter. If you see something similar to;
```pwsh
Python 3.13.3
```
you are good to go. If the PowerShell gives out an error, read it. If it says
something in the lines of "There is no command such as 'python3'.", then it's
not installed, or it's not in the $PATH. Please search for the error on the
Internet (in reputable websites such as, [stackoverflow](https://stackoverflow.com)).
</details>

<details>
    <summary>Windows 10</summary>

Search for `Terminal` in your Start menu, if it doesn't exist do `Ctrl+R` and
write `powershell.exe` and hit enter. You should see a window with blue
background pop up. Write the command;
```pwsh
python3 --version
```
to the command line and hit enter. If you see something similar to;
```pwsh
Python 3.13.3
```
you are good to go. If the PowerShell gives out an error, read it. If it says
something in the lines of "There is no command such as 'python3'." then it's
not installed, or it's not in the $PATH. Please search for the error on the
Internet (in reputable websites such as, [stackoverflow](https://stackoverflow.com)).
</details>
</details>

-------------------------------------------------------------------------------

<details>
    <summary>Linux/macOS</summary>

First, please check if it's installed, because a lot of Linux and macOS come
with Python installed. To check open up your preferred terminal (Ctrl+Alt+T)
and write the command;
```bash session
python3 --version
```
to the command line and hit enter. If you see something similar to;
```bash session
Python 3.13.3
```
you are good to go. Although it's not recommended to use the built-in version
of Python, you can. I strongly recommend you to update it, because the built-in
Python will be something like `Python 3.8.x`, which is really old at this
point.
<details>
    <summary>macOS</summary>

To upgrade Python, please run the command;
```bash session
brew upgrade
```
This will upgrade (update) all packages installed. After the installations are
done, please run the command;
```bash session
python3 --version
```
If you see something similar to;
```bash session
Python 3.13.3
```
you are good to go. If the shell gives an error, read it. If it says something
in the lines of "python3: command not found", then it's not installed, or it's
not in the $PATH. Please search for the error on the Internet (in reputable
websites such as, [stackoverflow](https://stackoverflow.com)).
</details>
<details>
    <summary>Linux</summary>

Dude, you're using a linux distro, do you really need me to explain you how to
install python or any other package? Anyway. 

<details>
    <summary>Ubuntu (and its derivations)</summary>

If you're on a Debian based distro (e.g., Ubuntu (or its derivations), Kali
Linux, Pop! OS, Linux Mint, etc.) run the command;
```bash session
sudo apt update
sudo apt upgrade
```
Then, run the command;
```bash session
python3 --version
```
If you see something similar to;
```bash session
Python 3.13.3
```
you are good to go. If you don't or see something else, run the command;
```bash session
sudo apt install python3
```
and check whether it's installed with the previous command.
</details>

<details>
    <summary>Arch Linux (and its derivations)</summary>

If you are on Arch Linux or one of its derivations and you're still reading,
first of all, fuck you. Second of all, if you could install arch without issues
then you certainly can fucking install Python. Show off.
</details>

</details>
