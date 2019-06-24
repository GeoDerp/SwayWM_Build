# Fedora/openSUSE Sway Build
<a href="https://build.opensuse.org/project/show/home:GeoDerp:redflower"><img src="https://img.shields.io/badge/RPM's-OBS-brightgreen.svg?style=for-the-badge&logo=opensuse"></a>
<a href="https://github.com/GeoDerp/SwayWM_Build/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-red.svg?style=for-the-badge&logo="></a>
<a href="https://getfedora.org/"><img src="https://img.shields.io/badge/Supports-Fedora-blue.svg?style=for-the-badge&logo=fedora"></a>
<a href="https://www.opensuse.org/"><img src="https://img.shields.io/badge/Supports-openSUSE-brightgreen.svg?style=for-the-badge&logo=opensuse"></a>


***Default :rice_ball: Name:*** **Redflower**
![alt text](https://raw.githubusercontent.com/GeoDerp/Fedora-Sway-WM-Build-/master/Images/thumbnail3.png)

Introducing my Fedora Workstation Sway WM Build with custom rice for WayBar, kitty, Albert, Sway and GTK3.
Feel free to use the install script to install all the dependencies and the rice, or you can do it by hand.    

## Why I made this?
The main goal for this was to crate a simple automation method for installing sway on Fedora.
 While I was installing Sway for myself I found it to be quite challenging to get it running for Fedora 29, so I decided to create this script and make it public, so if any one else is having issues they can look to this for help.

Of course after some work I found myself wanting to do more to this project and that's where everything else comes in play. I know this may look like a big hunk of mess, but I'll try to do my best to explain everything, and how it all works and why you should use it.

## how to use install script

Before you start the install make sure you have a clean install of [fedora workstation](https://getfedora.org/en/workstation/) and/or [openSUSE_Tumbleweed](https://software.opensuse.org/distributions/tumbleweed)  with the **gnome** (*should be default*). *(Feel free to try other versions but I am not 100% sure it will work)*.
And have git installed, if you haven't, just put ```sudo dnf/zypper install git -y``` in the terminal before using command below.

In Terminal type:
```console
cd ~/
git clone https://github.com/GeoDerp/SwayWM_Build.git
cd "SwayWM_Build"
sudo chmod +x "SwayInstallScript"
./SwayInstallScript
```
*(If you want the source builds and not the rpm's use ```BuildSwayInstallScript``` , This May Not Work On openSUSE [haven't tested]).*  

### Rpm packages:
[**OpenBuildService**](https://build.opensuse.org/project/show/home:GeoDerp:redflower)   
*Packages include: sway, wlroots, swaylock, swaybg, swayidle, swaybg, waybar, grim, wayland*

### GTK Theme
***Theme***:
The GTK Theme is a hacked mix of of [materia-theme](https://github.com/nana-4/materia-theme) from [**@nana-4**](https://github.com/nana-4)
and [Vimix-gtk-theme](https://github.com/vinceliuice/vimix-gtk-themes) By [**@vinceliuice**](https://github.com/vinceliuice)

***Icons***:
Icons is a modified version of [vimix-icon-theme](https://github.com/vinceliuice/vimix-icon-theme) by [**@vinceliuice**](https://github.com/vinceliuice)

***Cursor***:
Cursor is [Capitaine cursors](https://github.com/keeferrourke/capitaine-cursors) by [**@keeferrourke**](https://github.com/vinceliuice)

### Easy Theme changing !!
![alt text](https://raw.githubusercontent.com/GeoDerp/SwayWM_Build/master/Images/wpgtk-Implementation-Example.gif)

 - With the implementation of [wpgtk](https://github.com/deviantfero/wpgtk) by  [**@kdeviantfero**](https://github.com/deviantfero), all you have to do is change the wallpaper directory, $wall, in the sway config *(~/.config/sway)* and reset sway with *(ctrl+shift+r)*. The wallpaper will change, as well as all the theme colours from a generated colour pallet using the image as a reference.
 - Alternatively you can import multiple images into the wpgtk database using the [**wpg**](https://github.com/deviantfero/wpgtk/wiki) command *(cli with ``wpg -a`` or gui ``wpg``)* and press *(ctrl+shift+w)* when ever you want to change to another wallpaper/theme.  

 For more info, check out [**@kdeviantfero's**](https://github.com/deviantfero) youtube introductory video's: [playlist](https://www.youtube.com/watch?v=P3D0jtG6G2s&list=PL1wdmeKDuvmQ7Op-KTJQCAtAa75b9TlL3)

### Thank you to:

* **[Alexays](https://github.com/Alexays) For helping me Debug WayBar**
* **[c-edw](https://github.com/c-edw) For Showing me a docker file to use as an reference**   
* **[simotek](https://github.com/simotek) For Spending the time and debugging my code, for teaching me and helping maintain OBS**
* **[kdeviantfero](https://github.com/deviantfero) For helping me out with wpgtk**


*Sorry in advance for all my grammar and spelling mistakes.*

*sincerely*, [**GeoDerp**](https://github.com/GeoDerp)
