def create_youtube_video(title, description):
    youtube_video = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {}  
    }
    return youtube_video

def like(youtube_video):
    youtube_video["likes"] += 1
    return youtube_video

def dislike(youtube_video):
    youtube_video["dislikes"] += 1
    return youtube_video

def add_comment(youtube_video, username, comment):
    youtube_video["comments"][username] = comment
    return youtube_video

title = input("What is the title of your video? ")
description = input("What is the description of your video? ")
youtube_video = create_youtube_video(title, description)

youtube_video = like(youtube_video)

youtube_video = dislike(youtube_video)

username = input("What is your name? ")
comment = input("What is your comment? ")
youtube_video = add_comment(youtube_video, username, comment)

print("\nFinal State of the Video:")
print(youtube_video)

    