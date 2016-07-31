from PIL import Image
img = Image.open(r"D:pict\1.jpg")
left=50
top=200
width=1700
height=2200
box=(left,top,width,height)
resized_img=img.crop((box))
resized_img.save(r"D:\pict_recize\2.jpg")

res_img=Image.open(r"D:\pict_recize\2.jpg")
watermark=Image.open (r"D:\watermark\watermark.png")
width_w=500
height_w=500
watermark_res=watermark.resize((width_w,height_w))
res_img.paste(watermark_res,(1000,1400),watermark_res)
res_img.save(r"D:\pict_watermark\pict_watermark.jpg")