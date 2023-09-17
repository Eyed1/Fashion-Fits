import replicate
print("A")
output = replicate.run(
    "naklecha/clothing-segmentation:501aa8488496fffc6bbee9544729dc28654649f2e3c80de0bf08fb9fe71898f8",
    input={"image": open("images/green_shirt.jpg", "rb")}
)
print("HI")

with open("segment_link.txt", "w") as f:
    for x in output:
        f.write(x)
        f.write("\n")
