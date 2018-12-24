from uuid import uuid4
from bottle import post, run, request
import youtube_dl as yt
from core import init_db, add_song, songs_dir

def download_song(url):
    unique_name = str(uuid4())
    filename = f'{songs_dir}/{unique_name}.ogg'
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'vorbis',
        }],
    }
    with yt.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        ydl.download([url])

    title = info_dict['title']
    video_id = info_dict['id']
    tmp_filename = f'{title}-{video_id}.ogg'
    return title, tmp_filename


@post('/add/')
def index():
    # download
    url = request.params.text
    title, filename = download_song(url)
    print(f'Downloaded {url} - {title} - {filename}')

    # add to queue
    conn = init_db()
    add_song(conn, filename)
    conn.close()

    return f'Song "{title}" added to playlist'


run(host='0.0.0.0', port=8080)
