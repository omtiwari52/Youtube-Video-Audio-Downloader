# import pytube

from pytube import YouTube

##link liyaa

link = input("Enter a link :   ")
available = YouTube(link)

print("1. for video")
print("2. for audio")
op = int(input("enter choice : "))


if op == 1:
    video = available.streams.filter(progressive=True)

    for i,v in enumerate(video):
        res = str(v).split(" ")[3]
        # print(i,type(str(v)))
        print(f"{i}. {res[5:-1]}")

    choice = int(input("enter choice :"))
    download = str (video[choice]).split(" ")[1]
    print("downloading started.....")
    print(download[6:1])
    d = available.streams.get_by_itag(download[6:-1])
    print(d.download("./video"))
    print("downloaded....")
## streams ko show kiya sirf resolution 

if op == 2:
    audio = available.streams.filter(only_audio=True)
    for i,v in enumerate (audio):
        res = str(v).split(" ")[3]
        # print(i,type(str(v).split("")[3]))
    # print(i,res[5:-1])
    print(f"{i},{res[5:-1]}")

    choice = int(input("enter choice :"))
    download = str (video[choice]).split(" ")[1]
# print(video[choice])
    print("downloading started.....")
    print(download[6:1])
    d = available.streams.get_by_itag(download[6:-1])
    print(d.download("./audio"))
    print("downloaded....")


