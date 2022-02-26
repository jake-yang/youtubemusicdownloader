# youtubemusicdownloader
I was tired of free youtube to mp3 converter type of websites.. so I made one!

## How To Use
1. Download ffmpeg from website and make a folder on the right path ( link : https://ffmpeg.org/download.html )
2. On your IDE, make output folder, music folder, url.csv.
3. Spend some time to scrap url from any youtube videos that you want to get only audio file.
4. Paste each urls to url.csv one line by one url.
5. install required installments through your own terminal.
6. run main.py and it'll automatically get all urls from url.csv and search it on youtube, download music as webm file, and turn it into mp3 file. 
7. Moreover, through eyed3 library, it automatically adds title and artist info.

## Caution !!
1. it works best for Youtube Title of ' artist - song ' type or ' artist - song (HQ Audio or some description)' type
2. For example, if a Youtube Title is ' Santa Tell Me - Ariana Grande ' , it'll download the artist as 'Santa Tell Me'!
