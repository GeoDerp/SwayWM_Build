# Fedora Sway Build

***WARNING THIS IN BETA, some applications are broke and im currently troubleshooting. Sorry for the inconvenience***

**Rice Name: Redflower**
![alt text](https://raw.githubusercontent.com/GeoDerp/Fedora-Sway-WM-Build-/master/Images/img.png)

Introducing my Fedora Workstation Sway WM Build with custom rice for WayBar, irssi, kitty, Albert, sway and GTK3.
Feel free to use the install script to install all the dependencies and the rice, or you can do it by hand.    

## Why I made this?
The main goal for this was to crate a simple automation method for installing sway on Fedora.
 While I was installing Sway for myself I found it to be quite challenging to get it running for Fedora 29, so I decided to create this script and make it public, so if any one else is having issues they can look to this for help.

## how to use install script

Before you start the install make sure you have a clean install of fedora workstation (feel free to try other versions but I am not 100% sure it will work).
And have git installed, if you don't put *sudo dnf install git -y* in the terminal.

In Terminal type:
```console
cd ~/
git clone https://github.com/GeoDerp/Fedora-Sway-WM-Build-.git
cd "Fedora-Sway-WM-Build-"
sudo chmod +x "FedoraSwayInstallScript"
./FedoraSwayInstallScript
```


### GTK Theme
***Theme***:
The GTK Theme is a hacked mix of of [materia-theme](https://github.com/nana-4/materia-theme) from [**@nana-4**](https://github.com/nana-4)
and [Vimix-gtk-theme](https://github.com/vinceliuice/vimix-gtk-themes) By [**@vinceliuice**](https://github.com/vinceliuice)

***Icons***:
Icons is a modified version of [vimix-icon-theme](https://github.com/vinceliuice/vimix-icon-theme) by [**@vinceliuice**](https://github.com/vinceliuice) (This may not be the final choice)

***Cursor***:
Cursor is [Capitaine cursors](https://github.com/keeferrourke/capitaine-cursors) by [**@keeferrourke**](https://github.com/vinceliuice)

<!--
To use the Chrome theme;
Open Chrome, put (chrome://extensions) in the url bar then click developer mode.
Select the (load unpacked) button, find the (~/.themes/VimixRedFlower/Chrome Theme) directory and click open.
-->

### Thank you to:

* **[Alexays](https://github.com/Alexays) For helping me Debug WayBar**
* **[c-edw](https://github.com/c-edw) For Showing me a docker file to use as an reference**   
* **[simotek](https://github.com/simotek) For Spending the time and debugging some of my code**

Sorry in advance for all the grammar and spelling mistakes.

*sincerely*, [**GeoDerp**](https://github.com/GeoDerp)
