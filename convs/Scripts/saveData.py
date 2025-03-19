import json
import matplotlib as plt
def generateJson(trends):
    with open('.\convs\dataset\x.json','w') as x:
        json.dump(trends,x,indent=4, ensure_ascii=False)
def saveImage(image_resized,name):
    plt.imshow(image_resized, cmap='gray')
    plt.axis('off')
    plt.save(f'.\convs\dataset\{str(name)}.jpg')