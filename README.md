# RazerFX

`RazerFX` is a command-line interface (CLI) based tool that allow user to set RGB color for each key. This project is written using Python 3.x. Currently only works on Razer BlackWidow 2019 (en_US) keyboard.

![bright color palette](resources/example.jpg)
*`RazerFX` tested on Razer BlackWidow 2019 (en_US) keyboard*


## Prerequisites

Make sure to install `OpenRazer` driver first. See https://openrazer.github.io/.


## How to install?


```
$ git clone https://github.com/nikAizuddin/razerfx.git
$ cd razerfx
$ python3 -m pip install .
```


## How to use `RazerFX`?

To use default color palatte `bright` and without changing backlight brightness, simply execute the following command:

```
$ razerfx apply
```

To use different color palette such as `pastel` and change backlight brightness to `25%`:

```
$ razerfx --colorpal=pastel --brightness=25 apply
```

To list all `Razer` devices recognized by `OpenRazer` driver:

```
$ razerfx device_info
```

To list all key matrices for Razer BlackWidow 2019 (en_US) keyboard:

```
$ razerfx keyboard_matrix
```

For debugging purpose, you can view color palettes:

```
$ razerfx --colorpal=bright show_colorpal
```

Images below shows different type of color palette that you can use for `--colorpal` flag:

![bright color palette](resources/colorpal-bright.png)
*`bright` color palette*

![colorblind color palette](resources/colorpal-colorblind.png)
*`colorblind` color palette*

![dark color palette](resources/colorpal-dark.png)
*`dark` color palette*

![deep color palette](resources/colorpal-deep.png)
*`deep` color palette*

![hls color palette](resources/colorpal-hls.png)
*`hls` color palette*

![husl color palette](resources/colorpal-husl.png)
*`husl` color palette*

![muted color palette](resources/colorpal-muted.png)
*`muted` color palette*

![pastel color palette](resources/colorpal-pastel.png)
*`pastel` color palette*


## For development purpose


If you are interested to modify and playing with this project, you need to install `RazerFX` with `--editable` flag:

```
$ python3 -m pip install --editable .
```

