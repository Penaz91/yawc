Yet Another Wallpaper Changer
=============================

Multimonitor-aware wallpaper changer
------------------------------------

"I was bored one evening. So I made this."

### Basic Principles

The basic idea behind is having "modules" that take care of 3 steps:

1. Identifying the monitors
2. Downloading the wallpapers
3. Setting the wallpapers

### Configuration

The changer can be configured via its `config.toml` file.

#### General Section

```
[general]
monitor_detector="XlibDetector"
wallpaper_setter="CommandSetter"
wallpaper_downloader="DummyDownloader"
wallpaper_folder="<where to save/load the wallpapers>"
```

This configuration uses Xlib to identify the monitors and uses a command to set the wallpaper and no wallpapers will be downloaded.

Available Monitor Detectors:

- **XlibDetector** Available for Xorg

Available Wallpaper Downloaders:

- **DummyDownloader** Doesn't download any wallpaper, this makes YAWC just a local multimonitor-aware wallpaper setter
- **WallHaven** Downloads a random wallpaper from `wallhaven.cc`

Available Wallpaper Setters:

- **CommandSetter** Uses a shell command to set the wallpaper

### Optional sections

#### `downloader.WallHaven`

```
[downloader.WallHaven]
api_key = ""
purity = 100
sorting = "toplist"
top_range = "3M"
categories = 100
query = ""
max_pages = 5
```

You can configure the WallHaven downloader with the following options:

- **api_key** The WallHaven API key, necessary if you want to download certain types of images;
- **purity** How "pure" images should be, in WallHaven's scale SFW/Sketchy/NSFW (100 is SFW, 110 is SFW+Sketchy, etc...)
- **sorting** How to sort the result page, this affects how the image is randomly selected. Available values are:
    - date_added
    - relevance
    - random
    - views
    - favorites
    - toplist
    - automatically
- **top_range**: Defines the time range to search in (available values: 1d 3d 1w 1M 3M 6M 1y)
- **categories**: Defines the categories to search in: General/Anime/People (100 is General, 110 Is General+Anime, etc...)
- **query**: Keywords you want to use to filter the search
- **max_pages**: The maximum number of pages you want to search in (so you don't always search in the first result page).

One picture per monitor will be downloaded, the monitor's resolution will be automatically be used to filter the results further.

#### `setter.CommandSetter`

```
[setter.CommandSetter]
command = "nitrogen --set-zoom-fill --random {folder} --head={monitor}"
```

This configuration gets a random wallpaper from the folder set in the general section and sets it on the monitor (using Nitrogen).

A different configuration (usually used in conjunction with a downloader) is the following:

```
[setter.CommandSetter]
command = "nitrogen --set-zoom-fill {background} --head={monitor}"
```
