from pathlib import Path 
from fractions import Fraction
import subprocess, shutil, json

# Funções
def detect_fps(fps):
    candidates = [
        Fraction(24000, 1001),
        Fraction(25, 1),
        Fraction(30000, 1001),
        Fraction(50, 1),
        Fraction(60000, 1001),
        Fraction(120000, 1001)
    ]
    return min(candidates,key=lambda x: abs(float(x) - fps))

# Criação de diretórios
dirs = [
    Path("./videos/"),
    Path("./es/ffprobe-json/"),
    Path("./es/raw-stream/"),
    Path("./final-v/")
]

for cdirs in dirs:
    cdirs.mkdir(parents=True, exist_ok=True)

# Verificar se existe arquivos
vd = Path("./videos")
if not any(file.is_file() for file in vd.iterdir()):
    print("Nenhum arquivo encontrado")
    print("Coloque os vídeos em './videos/'")
else:
    for videos in vd.iterdir():
        if not videos.is_file():
            continue    

# Leitura do FFprobe
        save = Path("./es/ffprobe-json/") / f"{videos.stem}.json"

        with open(save, "w") as f:
            log = subprocess.run(
                [
                    "ffprobe",
                    "-v",
                    "error",
                    "-print_format",
                    "json",
                    "-show_entries",
                    "stream=index,bit_rate,codec_type,codec_name,profile,level,width,height,pix_fmt,sample_aspect_ratio,display_aspect_ratio,field_order,color_range,color_space,color_transfer,color_primaries,chroma_location,r_frame_rate,avg_frame_rate,time_base,start_pts,start_time,duration_ts,duration,nb_frames,sample_rate,channels,channel_layout,sample_fmt,bits_per_sample,extradata",
                    "-show_entries",
                    "stream_side_data",
                    str(videos)
                ],
                stdout=f,text=True
            )

        # Leitura e armazenamento do Python
        with open(save, "r") as f:
            metadata = json.load(f)

        for stream in metadata["streams"]:
           if stream["codec_type"] == "video":
               vdin = stream
               break
            
        video_info = {
               "ratio" : vdin.get("display_aspect_ratio"),
               "fps" : vdin.get("r_frame_rate"),
               "clock" : vdin.get("time_base"),
               "duration" : vdin.get("duration"),
               "bitrate" : vdin.get("bit_rate"),
               "codec" : vdin.get("codec_type")
            }
    
        # Conversões e cálculos dos dados obtidos
        bitrate_raw = int(video_info["bitrate"] or 10000000)
        bitrate = int(bitrate_raw * 0.65)
        fps = video_info["fps"]
        num, den = fps.split("/")
        fps = float(num) / float(den)
        fps = detect_fps(fps)
        gop = round(float(fps)) * 2
        
        # Execução do FFmpeg
        rawvideo = Path("./es/raw-stream") / f"{videos.stem}.265"
        finalvideo = Path("./final-v") / f"{videos.stem}.mkv"
        raw = subprocess.run(
            [
                "ffmpeg","-i", str(videos), "-map", "0:v:0", "-c:v", "hevc_mediacodec", "-b:v", str(bitrate), "-g", str(gop), "-pix_fmt", "nv12", "-f", "hevc", str(rawvideo)
            ],
            check=True,text=True)

        mux = subprocess.run(
            [
                "ffmpeg", "-fflags", "+genpts", "-r", str(fps), "-i", str(rawvideo), "-i", str(videos), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "libopus", "-b:a", "96k", "-fps_mode", "passthrough", "-avoid_negative_ts", "make_zero", str(finalvideo)
            ],
            check=True,text=True)