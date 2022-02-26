import ssl
from pytube import YouTube
import subprocess
import os
import eyed3
import csv


save_dir = './music'
output = '.wav'


def convert_and_split(file, out):  # file extension should be included
    command = ['ffmpeg', '-i', file, out]
    subprocess.run(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                   executable='/Users/anwhae/audio-orchestrator-ffmpeg/bin/ffmpeg')


def change_filename(filename):  # Assume ' singer - song ( HQ Audio ... ).webm '
    singer_loc = filename.find('-')  # Find location of -
    desc_loc = filename.find('(')  # Find location of (
    singer_txt = filename[:singer_loc-1]  # Get singer text part
    if desc_loc < 0:
        desc_loc = len(filename)+1
    else:
        pass
    song_txt = filename[singer_loc+1:desc_loc-1]  # Get song text part
    full_name = singer_txt+' - '+song_txt
    return song_txt, singer_txt

data = []
with open('url.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
print(data)
for i in range(len(data)):
    url = data[i][0]
    ssl._create_default_https_context = ssl._create_unverified_context  # Block url error

    # Get webm file from url
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True, file_extension='webm')[-1]
    downloaded = video.download(output_path=save_dir)  # Download file
    original_title = os.path.splitext(downloaded)[0].split('/')[-1]  # Get title without extension
    title, artist = change_filename(original_title)

    # Add tags to mp3 file
    convert_and_split('./music/' + original_title + '.webm', './output/' + title + '.mp3')  # Convert webm to mp3
    audio_file = eyed3.load('./output/' + title + '.mp3')  # Open mp3 file
    audio_file.tag.artist = artist.strip() # Add artist
    audio_file.tag.title = title.strip()  # Add title
    audio_file.tag.save()
    print(f"Congrats! Song saved as \n Artist : {artist}, Title : {title}")

