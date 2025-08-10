import yt_dlp

def download_video():
    try:
        video_url = (input(
            "Введите ссылку на видео: ")
                     .strip()
                     )
        save_path = (input(
            "Введите путь для сохранения видео (или Enter для текущей папки): ")
                     .strip() or "."
                     )

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }

        try:
            print(f"Скачиваем видео с {video_url}...")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            print("Видео успешно скачано!")
        except Exception as e:
            print(f"Ошибка при скачивании видео: {e}")
    except KeyboardInterrupt:
        print("\nСкачивание видео отменено.")

if __name__ == "__main__":
    download_video()
