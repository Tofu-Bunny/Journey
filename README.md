# Fancy Flying Enabler for keyboard-only players

![c:](https://i.imgur.com/s43yIIE.png)


### DISCLAIMER!!

i made this tool purely for fun, and to allow keyboard-only players (like me) to experience/experiment with some of the more advanced Fancy Flying tech which is normally inaccessible to those of us who do not own a controller or simply prefer playing with a mouse and keyboard. Since the tool allows for perfect precision and consistency, please do not use it to submit any speedrun times, as one might argue it could be used to gain an unfair advantage in certain situations and that is certainly not the reason why i made this. This tool is meant for accessibility and goofing around in the desert sky. Please use it responsibly and be respectful to your fellow companions. Thank you.

### WHAT DOES THE TOOL DO?

All the script does is emulate a virtual gamepad and send left-stick inputs to your computer, basically tricking your pc into thinking that you have a controller plugged in. It binds 2 extra keys that will simulate pushing forward on a virtual left-stick by less than 100%, allowing you to walk or slow fall only using a keyboard. The game does not need to be running beforehand and the script does not directly interact with it in any way. Additionally, the game recognizes both gamepad and keyboard inputs at the same time and the script doesn't overwrite either of them, so all your normal keyboard inputs will be completely unchanged.

### PREREQUISITES AND INSTALLATION

The script runs in Python 3. If you need to install it, you can find it at [python.org](https://www.python.org/downloads/release/python-3124/).

It also utilizes the 'vgamepad' and 'keyboard' modules; to install those:
1. After installing Python, press `win + R`, type `cmd` and press OK
2. Type `pip install vgamepad` and press `Enter`
3. Type `pip install keyboard` and press `Enter`

Here's a picture of what that should look like!

![example install](https://i.imgur.com/89fFdhr.png)

Additional information about these two modules can be found here:
- vgamepad: https://pypi.org/project/vgamepad/
- keyboard: https://pypi.org/project/keyboard/

### USING THE SCRIPT AND CUSTOMIZING KEYBINDS

If you just want to RUN the script, you can simply double click on it. This window will appear:

![script in Terminal](https://i.imgur.com/JcFEChj.png)

And, you're good! The script is running and it's ready to be used. Pushing the `QUIT` button (`F9` by default) will end the script and close this window.

If you want to customize keybinds:

First off, `right-click` on the .py file > `Edit with IDLE` > `Edit with IDLE (your version)`. A new window will open up:

![script](https://i.imgur.com/axMdMQB.png)

If you want to run the script from here, simply press `F5` or click on `Run` > `Run Module`. A new window that looks like this will appear:

![running script](https://i.imgur.com/UmboKeO.png)


If you want to customize the controls and strength percentages, look near the top of the code in the first window and you will see 2 sections labled "Set keybinds here" and "Set steer values (in%) here". This is where you can change keybinds and strength values.
- `BIND1`: Keybind #1   (default is Q)
- `BIND2`: Keybind #2   (default is E)
- `TOGGLE`: ON/OFF toggle key   (default is T)
- `QUIT`: The quit button   (default is F9)
- `PER1`: How much Keybind 1 pushes forward (in %, accepts any value from 0 to 100, default is 63)
- `PER2`: How much Keybind 2 pushes forward (in %, accepts any value from 0 to 100, default is 70)

All these can be changed to whatever suits your needs. Once you're happy with them, click `File` > `Save` and you're ready to run.

Once you launch the script, you can check that it's working correctly here: https://hardwaretester.com/gamepad . Simply press any of the binds and look at the stick move.

### CONTROLS

By default:
- 'F9' ends the script
- 'T' toggles controls ON and OFF
- 'Q' moves the left stick forward 63% (soft touch for Flap Boosting, right before Slow Boost)
- 'E' moves the left stick forward 70% (firmer touch for Slow Boosting)

Like previously mentioned, all keybinds and percentages can be customized to whatever you like. i decided to set the keybinds to Q and E because it makes them super easy to press while using WASD for movement, but if you use a different control scheme or prefer different % values feel free to change them to whatever suits you!

#  

An additional special thanks to Arckoor for suggesting and helping with a couple things, and to NathanJ for insight on pressure percentages <3

Aaand that's pretty much it! Once again please use this tool responsibly and have fun.

See you in the sky.

-Tofu
