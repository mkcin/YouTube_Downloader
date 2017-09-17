import youtube_dl
import re
import json
import subprocess

YT_OPTS = []

def ask_for_flags():
    czy_mp3 = input('video or music (default video):\n1 - video\n2 - music\n')
    if(czy_mp3 == '2'):
        m_format = input('format (default mp3):\n1 - mp3\n2 - m4a\n3 - flac\n4 - wav\n5 - aac\n')
        formats = {
            '1': 'mp3',
            '2': 'm4a',
            '3': 'flac',
            '4': 'wav',
            '5': 'aac'}
        if(re.match(r'^([0-9]+)$', str(m_format)) and int(m_format) >= 1 and int(m_format) <= 5):
            m_format = formats[m_format]
        else:
            # print("default\n")
            m_format = 'mp3'
        YT_OPTS.append('-x')
        YT_OPTS.append('--audio-format')
        YT_OPTS.append(m_format)
        print(YT_OPTS)
    else:
        YT_OPTS.append('-f')
        quality = input('choose quality (default possible best):\n1 - 1080p\n2 - 720p\n3 - 480p\n4 - 360p\n5 - 144p\n')
        if(quality == '5'):
            YT_OPTS.append('bestvideo[height<=144]+bestaudio/best[height<=144]')
        if(quality == '4'):
            YT_OPTS.append('bestvideo[height<=360]+bestaudio/best[height<=360]')
        if(quality == '3'):
            YT_OPTS.append('bestvideo[height<=480]+bestaudio/best[height<=480]')
        if(quality == '2'):
            YT_OPTS.append('bestvideo[height<=720]+bestaudio/best[height<=720]')
        if(quality == '1'):
            YT_OPTS.append('bestvideo[height<=1080]+bestaudio/best[height<=1080]')
        else:
            YT_OPTS.append('bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best')


def download(vids, what):
    if(what == 'video'):
        vid = vids[0]
        print(vid)
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
        with ydl:
            result = ydl.extract_info(
                vid,
                download=False # We just want to extract the info
            )
        video = result
        # print(video)
        # print(json.dumps(video, indent = 2))
        print('---------------------------\n')
        print(video['title'])
        count = 1
        choices={}
        audio = 1000
        for v_format in video['formats']:
            # print(v_format['format'] + " " + v_format['ext'])
            f = v_format['format'].split(' - ')[0]
            first_word = v_format['format'].split()[2]
            if(first_word=='audio'):
                audio = min(audio, int(f))
                continue
            # print(first_word)
            # print(f)
            try :
                print('{}. {} - {} ({}MB)'.format(count, v_format['format'].split(' - ')[1], v_format['ext'], float(v_format['filesize'])/1000000))
            except:
                print('{}. {} - {}'.format(count, v_format['format'].split(' - ')[1], v_format['ext']))
            choices[str(count)] = [f, first_word]
            count += 1
        # print(choices)
        choice = input(':   ')
        if(not re.match(r'^([0-9]+)$', str(choice)) and int(choice) >= 1 and int(choice) <= int(count-1)):
            choice = str(count-1)
        opt = ['-cif', str(choices[choice][0]+'+'+str(audio)), vid]

        youtube_dl.main(opt)
    else:
        # ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
        # with ydl:
        #     result = ydl.extract_info(
        #         vid,
        #             download=False # We just want to extract the info
        #     )
        # video = result
        # # print(video)
        # # print(json.dumps(video, indent = 2))
        # print(video['title'])
        # # print('----------------------')
        # for v_format in video['formats']:
        #     # print(v_format['format'] + " " + v_format['ext'])
        #     f = v_format['format'].split(' - ')[0]
        #     first_word = v_format['format'].split()[2]
        #     if(first_word == 'audio'):
        #         opt = ['-f', f, vid]
        #         youtube_dl.main(opt)
        opt = ['--extract-audio', '--audio-format',  'mp3']
        for v in vids:
            opt.append(v)
        youtube_dl.main(opt)

# ask_for_flags()
# download('https://www.youtube.com/watch?v=fKopy74weus', 'video')
