from videoConverter import VideoConverter

file = VideoConverter(
    "media/sample.mp4",
    "media/output.flv",
    {"format": "flv", "video": {"codec": "copy"}, "audio": {"codec": "copy"}},
)

file.run()
