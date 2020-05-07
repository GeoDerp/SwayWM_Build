# List Of Things To Do
### Before I can call it finished:

earlier things to do
--------------------------------------------------------
- [ ] make a basic 3 way hue module for waybar
- [ ] Finish implementing Tackle Box + update readme to support
  - https://github.com/simotek/tacklebox
  - https://github.com/simotek/tackle
- [ ] implement wpgtk for TackleBox
- [ ] introduce new terminal or upgrade kitty (find terminal that best suites waybar/sway)
- [ ] implement waybar modules im using into build, + update readme to support
- [ ] possibly update install script and build intsall script to another language to add better support and less errors (possiblya nsible)
- [ ] since albert seems depreciated move to (and implemnt rpm into opensuse-build & wpgtk supprt)
   - https://github.com/Ulauncher/Ulauncher 
   or  
   - https://github.com/Biont/sway-launcher-desktop 
     
--------------------------------------------------------
- [x] FIX OPEN SUSE [BUILD PACKAGES](https://build.opensuse.org/project/show/home:GeoDerp:redflower)
- [x] FIX ALBERT, [*Error.md*](https://github.com/GeoDerp/Fedora-Sway-WM-Build-/blob/master/AlbertErrors.md), [*Issue*](https://github.com/albertlauncher/albert/issues/768)
[**Update:** it kinda works, it's using x not Wayland and has a tendency to not run on startup (that may be a sway issue)]
- [x] Figure out bug with waybar, [*Error.md*](https://github.com/GeoDerp/Fedora-Sway-WM-Build-/blob/master/WaybarError.md), [*Issue*](https://github.com/Alexays/Waybar/issues/182) (Fixed here: [Fix](https://github.com/Alexays/Waybar/issues/182#issuecomment-486518315))
- [ ] Load workspace script
- [ ] Figure out Waybar's overlay button problem
- [x] Upgrade Install script, until my OCD has been met
- [ ] Upgrade Waybar with plugins and custom modules *(like weather)*
- [x] Make sure all font awesome icons work in install
- [ ] Learn how to make a GDM theme, and maybe even a Grub
- [x] Make Atom theme, upgrade UI and add plugins *(If anyone would love to make one for his rice, that would be very much appreciated.)*
- [x] Make a proper thumbnail/gif for readme.md *(Feel free to send me an image for this if you have made one)*
- [x] Turn Sway, wlroots,waybar, swaylock,swayidle build into an automated rpm to allow easy install, update and uninstall *(mainly for updates).*
*Might use something like (open build service)[https://openbuildservice.org/] to automate the process of pulling the latest version of the git repo + the spec file and auto compile into an rpm*
[**Update:** [BUILD PACKAGES](https://build.opensuse.org/project/show/home:GeoDerp:redflower) ]
- [x] Figure out issue with swaylock not acceptkng password [24/2/19](https://github.com/GeoDerp/Fedora-Sway-WM-Build-/commit/5db0a8b39b4cdc83d8a9ba77414aab04889958c1)
- [x] Publish on Reddit [The post](https://www.reddit.com/r/unixporn/comments/bo4va6/sway_fedora_30_redflower/)
- [x] get wf-recorder  working on OBS (**Wont Get working due to ffmpeg**, if you want to download it uncomment from install script)
  - [x] Add key bind in sway .config for wf-recorder
  - [ ] see if i can replace ffmpeg to OpenH264
- [ ] check out oomox and maybe implement it (I personally wont, if someone want to do that and integrate it with wpgtk that will be grate)
- [x] Implement teamsilver (should work, haven't tested)
- [x] Find all the dependencies names verients from fedora for opensuse and implement an if opensuse install for [BuildSwayInstallScript Line:69]( https://github.com/GeoDerp/SwayWM_Build/blob/8636e9792867fc92c0ad39fa12368cb2b81edab7/BuildSwayInstallScript#L69)
- [x] check Albert, not starting on boot problem
- [ ] make and add Hexchat rice?!?! mabie with wpgtk?
- [x] BRING BACK [WPGTK](https://github.com/deviantfero/wpgtk), for easy theme changing. Don't know how I will use it to change the GTK theme but should be able to customise everything else
- [x] implement wpgtk.vim
- [x] After making a dedicated Atom theme, implement wpgtk so it will auto change with the colour scheme (if possible) - **Can Find wpgtk Atom themes [here](https://github.com/GeoDerp/wpgtk.atom)**
- [ ] Make a Systemd Timer for wpgtk theme rotation every 10min or so (```sleep 10m && wpg -m```), and implement as an option for users.   
- [ ] Implement a capibility to auto pull images from a well known source using veribles for preference. For when when the wallpaper gets called to change using wpgtk*(with ALT+SHIFT+W)*
- [ ] Find the time to create a well documented wiki on how everything works and how you can change things to better suit your wont/needs.
- [ ] add the ability so everytime you ssh into a particular mashine wpgtk changes the theme to a theme of your choice for that mashine

***If Anyone would like to help with any of these, or have an idea on what to add to this list, feel free to let me know, and that would be kindly appreciated :grin:***
