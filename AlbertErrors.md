#Error
**Error posted here:** albertlauncher/albert#768

#### Source
Compiled and https://download.opensuse.org/repositories/home:manuelschneid3r/Fedora_29/home:manuelschneid3r.repo (tried both)

#### Environment
```
  Albert version: 0.16.1
            Build date: Jan 26 2019 15:31:13
            Qt version: 5.11.3
  QT_QPA_PLATFORMTHEME:
       Binary location: /usr/bin/albert
                   PWD: /home/geo
                 SHELL: /bin/bash
                  LANG: en_AU.UTF-8
      XDG_SESSION_TYPE: wayland
   XDG_CURRENT_DESKTOP:
       DESKTOP_SESSION: sway
   XDG_SESSION_DESKTOP: sway
                    OS: Fedora 29 (Workstation Edition)
     OS (type/version): fedora/29
             Build ABI: x86_64-little_endian-lp64
  Arch (build/current): x86_64/x86_64
 Kernel (type/version): linux/4.20.3-200.fc29.x86_64
```


```
\S
Kernel \r on an \m (\l)
4.20.3-200.fc29.x86_64
DESKTOP_SESSION=sway
XDG_SESSION_TYPE=wayland
XDG_SESSION_DESKTOP=sway
QMake version 3.1
Using Qt version 5.11.3 in /usr/lib64
albert 0.16.1
```

#### Steps to reproduce
Fedora 29 Workstation
Sway WM
```console
mkdir Albert
  cd Albert
  sudo dnf install python3-devel qt5-qtx11extras-devel qt5-qtsvg-devel muParser-devel libqalculate-devel qt5-qtcharts-devel qt5-qtwayland-devel -y
  git clone --recursive https://github.com/albertlauncher/albert.git
  mkdir albert-build
  cd albert-build
  cmake ../albert -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Debug
```

#### Expected behaviour
No Segmentation fault's

#### Actual behaviour
```
17:16:16 [INFO:default] Systems icon theme is: "hicolor"
warning: Loadable section ".note.gnu.property" outside of ELF segments
warning: Loadable section ".note.gnu.property" outside of ELF segments
17:16:16 [WARN:default] Application has not been terminated graciously.
warning: Loadable section ".note.gnu.property" outside of ELF segments
warning: Loadable section ".note.gnu.property" outside of ELF segments
17:16:17 [INFO:default] Loading extension "org.albert.extension.applications"
[New Thread 0x7fffe6270700 (LWP 3397)]
17:16:17 [INFO:applications] Start indexing applications.
17:16:17 [INFO:default] Loading extension "org.albert.extension.chromebookmarks"
[New Thread 0x7fffe5a2a700 (LWP 3398)]
17:16:17 [INFO:default] Start indexing Chrome bookmarks.
17:16:17 [INFO:default] Loading extension "org.albert.extension.system"
17:16:17 [INFO:default] Loading extension "org.albert.extension.terminal"
17:16:17 [INFO:default] Loading extension "org.albert.extension.websearch"
```

Error Codes from dgb bt
```
#0  0x00007ffff7a57aa1 in _XSend (dpy=dpy@entry=0x51db30, data=data@entry=0x0, size=size@entry=0) at xcb_io.c:464
#1  0x00007ffff7a57f24 in _XFlush (dpy=0x51db30) at xcb_io.c:516
#2  0x00007ffff7a5aafd in _XGetRequest (dpy=dpy@entry=0x51db30, type=type@entry=119 'w', len=len@entry=4) at XlibInt.c:1717
#3  0x00007ffff7a46701 in XGetModifierMapping (dpy=0x51db30) at ModMap.c:42
#4  0x00000000004a732f in GlobalShortcut::HotkeyManagerPrivate::HotkeyManagerPrivate (this=0x61d920, parent=0x0)
    at /home/geo/Albert/albert/lib/globalshortcut/src/hotkeymanager_x11.cpp:394
#5  0x00000000004a6282 in GlobalShortcut::HotkeyManager::HotkeyManager (this=0x576f20, parent=0x0)
    at /home/geo/Albert/albert/lib/globalshortcut/src/hotkeymanager.cpp:14
#6  0x0000000000473cf4 in main (argc=1, argv=0x7fffffffdfe8) at /home/geo/Albert/albert/src/app/main.cpp:329
```


Note: I started with the rebo and it worked fine untill I installed _qt5-qtwayland-devel_ to fix  

```[WARN:qt.qpa.plugin] Could not find the Qt platform plugin "wayland" in "" ``` error and got the Segmentation error. Now even with _qt5-qtwayland-devel_ uninstalled I get the same error :(

Tried setting  QT_QPA_PLATFORM="" environment variable and still no luck.
