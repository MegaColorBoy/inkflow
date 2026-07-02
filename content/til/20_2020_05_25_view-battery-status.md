title: View battery status
date: May 25th, 2020
slug: view-battery-status
category: Linux

This comes in handy if you're using the terminal in full screen but still want to know your battery life. Just type the following:

```bash
upower -i /org/freedesktop/UPower/devices/battery_BAT0
```

