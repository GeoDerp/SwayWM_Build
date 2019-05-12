# openSUSE Build Service
Here are all the core files used for all the packages used in this project.   
  
**Disclaimer**: I Did not create all these packages and cannot claim ownership. If you will like to know who was the founder check the .changes files for there respective packages

## Project 
Here: [home:GeoDerp:redflower](https://build.opensuse.org/project/show/home:GeoDerp:redflower)

## Install 
If you like to install just the sway rpms do:

 ``` shell 
 #finding OS
. /etc/os-release
if [[ $NAME = Fedora* ]]
then ins=dnf
elif  [[ $NAME = openSUSE* ]]
then ins=zypper
elif [[ ! -z "$OSTREE_VERSION" ]] #For SilverBlue (SilverBlue may not work on riceing stage, haven't tested)
then ins=rpm-ostree
else echo "can't find distro name, defaulting to Fedora" && ins=dnf
fi

#configuring os variable  
if [[ $NAME = Fedora* ]]
then os="$NAME"_"$VERSION_ID"
elif [[ ! -z "$OSTREE_VERSION" ]] #For Silverteam 
then os="$NAME"_"$VERSION_ID"
elif  [[ $NAME = "openSUSE Leap" ]]
then os="$NAME"_"$VERSION_ID"
elif  [[ $NAME = "openSUSE Tumbleweed" ]]
then os=$NAME
else echo "can't find distro name"
fi

echo "Installing wlroots,sway,swaylock,swayidle,albert,grim and waybar from rpm"
  sudo rpm --import https://build.opensuse.org/projects/home:GeoDerp:redflower/public_key
  sudo $ins config-manager --add-repo "https://download.opensuse.org/repositories/home:/GeoDerp:/redflower/"$os"/home:GeoDerp:redflower.repo"
  sudo $ins install wlroots sway swaylock swaybg swayidle albert grim waybar -y
  sudo $ins install fmt-devel -y
  sudo bash -c ' echo "auth include login" > /etc/pam.d/swaylock'
  # since albert only works in xwayland for the time being we have to tell it to run in xwayland and not wayland 
  sudo bash -c ' echo export QT_QPA_PLATFORM="xcb" >> /etc/profile.d/albert.sh'
  #when we start up sway we will try to run albert in x11 and all the other QT programs in wayland
  sudo bash -c ' echo export QT_QPA_PLATFORM="wayland" >> /etc/profile.d/qtwayland.sh'
  source /etc/profile.d/albert.sh

 ```
