from transformers import SegformerImageProcessor, AutoModelForSemanticSegmentation
from PIL import Image
import requests
import matplotlib.pyplot as plt
import torch.nn as nn
import urllib.request

processor = SegformerImageProcessor.from_pretrained("mattmdjaga/segformer_b2_clothes")
model = AutoModelForSemanticSegmentation.from_pretrained("mattmdjaga/segformer_b2_clothes")

#url = "https://plus.unsplash.com/premium_photo-1673210886161-bfcc40f54d1f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8cGVyc29uJTIwc3RhbmRpbmd8ZW58MHx8MHx8&w=1000&q=80"
#url = "https://kidteachkid.org/wp-content/uploads/2020/05/Rich-School-picture-new-2018-reduced-full-size-cropped.jpg"
#url = "https://www.bu.edu/careers/files/2022/08/resources-pcc-600x500.jpg"
#url= "https://media.cnn.com/api/v1/images/stellar/prod/140402222212-big-bang-theory-cast-0402.jpg?q=w_800,h_534,x_0,y_0,c_fill"
url = "https://imgs.michaels.com/MAM/assets/1/5E3C12034D34434F8A9BAAFDDF0F8E1B/img/94E9E2DD89844CEEAC9D3653D2BC2F3E/10388595_11.jpg"
urllib.request.urlretrieve(url, "img.jpg")
#image = Image.open(requests.get(url, stream=True).raw)
image = Image.open("img.jpg")
inputs = processor(images=image, return_tensors="pt")

outputs = model(**inputs)
logits = outputs.logits.cpu()

upsampled_logits = nn.functional.interpolate(
    logits,
    size=image.size[::-1],
    mode="bilinear",
    align_corners=False,
)

pred_seg = upsampled_logits.argmax(dim=1)[0]

plt.imshow(pred_seg)
plt.show()
