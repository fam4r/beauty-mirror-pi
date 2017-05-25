# Beauty Mirror Pi

by famar and [nicolasfara](https://github.com/nicolasfara) for FabLabRomagna

Using pygame, made for Raspberry Pi.
Tested on Raspberry Pi 3.

## Requirements:
- Raspberry Pi 3
- python3
- pygame
  - [Website](http://www.pygame.org/wiki/about)
  - [Installation](http://www.pygame.org/wiki/GettingStarted) (see later - already installed on Raspbian)
  - [Docs](http://www.pygame.org/docs/)
- PIR sensor

## Getting started:

Clone the repo and enter into the folder, then exec following commands.

```bash
# Install pygame
pip install pygame --user
# Check if it's installed correctly
python -m pygame.examples.aliens
# Exec beauty-mirror-pi.py
python3 beauty-mirror-pi.py
```

To open it at startup (works with Raspbian Pixel DE):
`nano ./boot_at_startup` and change the path to the `.py` file.

Then
```shell
nano ~/.config/lxsession/LXDE-pi/autostart
@/path/to/repo/start_at_boot.sh
```
