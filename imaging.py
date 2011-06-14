import Image,ImageEnhance
import os
import random
import math
import simplejson

class umelaborize:
    def __init__(self,x = 640,y = 480,json_file = ''):
        self.workspace = Image.new('RGB',(x,y))

        jfile = open(json_file,"r").read()
        self.config_json = simplejson.loads(jfile)

        self.make_mask_x = self.config_json[0][0]
        self.make_mask_y = self.config_json[0][1]

    def __init__(self, x = 640, y = 480, confimagefile = '', hoge = 0):
        self.workspace = Image.new('RGB', (x, y))
        confImage = Image.open(confimagefile)
        self.config_json = [[confImage.size[0]-1, confImage.size[1]-1]]
        self.make_mask_x = confImage.size[0]-1
        self.make_mask_y = confImage.size[1]-1
        pixelArray = []
        for y in xrange(confImage.size[1]):
            yArray = []
            for x in xrange(confImage.size[0]):
                yArray.append(1 if confImage.getpixel((x,y)) == 0 else 0)
            self.config_json.append(yArray)

    def load_image(self,image,debug = False):
        self.im = Image.open(image)
        if debug == True:
            self.im.show()

    def rotate_image(self,image,flag):
        if flag:
            r = pow((image.size[0] / 2),2) + pow((image.size[1] / 2),2)
            r = math.sqrt(r)
            r = int(r)
            
            base = Image.new("RGB",(r*2,r*2),(0,0,0))
            base.putalpha(Image.new("L",(r*2,r*2),0))
            base.paste(image,((base.size[0] - image.size[0]) / 2,(base.size[1] - image.size[1])/2))
            base = base.rotate(random.randint(0,360))
            return base
        else:
            return image

    def kill_paste(self,times,rotate_flag = False,debug = False):
        image_x,image_y = self.im.size
        
        for i in range(times):
            image_smaller_flag = times / (times / 10)
            box_x_size = random.randint(1,image_x) / image_smaller_flag
            box_y_size = random.randint(1,image_y) / image_smaller_flag
            box_x = random.randint(1,image_x) - box_x_size
            box_y = random.randint(1,image_y) - box_y_size

            if box_x < 0:
                box_x = 0
            if box_y < 0:
                box_y = 0

            if debug == True:
                print("Paste =>",box_x,box_y,box_x_size,box_y_size)

            box = (box_x,box_y,box_x + box_x_size,box_y + box_y_size)
            work_x,work_y = self.workspace.size

            mask_check = True
            mask_koma_x = work_x / self.make_mask_x
            mask_koma_y = work_y / self.make_mask_y
            max_work_x = work_x
            max_work_y = work_y

            if debug == True:
                print(mask_koma_x,mask_koma_y)

            while mask_check:
                work_x = random.randint(1,max_work_x - 1)
                work_y = random.randint(1,max_work_y - 1)

                if debug == True:
                    print(work_x,work_y,(work_y / mask_koma_y) + 1,(work_x / mask_koma_x),self.config_json[work_y / mask_koma_y + 1][work_y / mask_koma_y])
                
                fix_x = random.randint(0,max_work_x / 10)
                fix_y = random.randint(0,max_work_y / 10)

                if (work_x - fix_x) / mask_koma_x < 1 or work_x - fix_x < 0:
                    fix_x = 0
                if (work_y - fix_y) / mask_koma_y < 1 or work_y - fix_y < 0:
                    fix_y = 0
                if debug == True:
                    print(work_x - fix_x,work_y - fix_y)
                if self.config_json[((work_y - fix_y) / mask_koma_y) + 1][(work_x - fix_x) / mask_koma_x] == 1:
                    mask_check = False

            if debug == True:
                print("mask check ok")

            #if debug == True:
            #    self.im.crop(box).show()

            temp_image = self.im.crop(box)

            if random.randint(0,1) == 1:
                merge_list = temp_image.split() 
                r = merge_list[random.randint(0,2)]
                g = merge_list[random.randint(0,2)]
                b = merge_list[random.randint(0,2)]
                temp_image = Image.merge("RGB",(b,g,r))

            base = self.rotate_image(temp_image,rotate_flag)
            if rotate_flag:
                self.workspace.paste(base,(work_x,work_y),base)
            else:
                self.workspace.paste(base,(work_x,work_y))

        print("Image Paste Done.")

    def stamp_image(self,size,times):
        work_x,work_y = self.im.size
        work_x = work_x / size
        work_y = work_y / size
        self.im.thumbnail((work_x,work_y))

        temp_x,temp_y = self.workspace.size
        temp_x = random.randint(0,temp_x)
        temp_y = random.randint(0,temp_y)

        for i in range(times):
            box = ((temp_x,temp_y))
            self.workspace.paste(self.im,box)
            temp_x = temp_x - (random.randint(0,30) - 15)
            temp_y = temp_y - (random.randint(0,30) - 15)
        
    def test_show(self):
        self.workspace.show()

    def save_image(self,file_name):
        self.workspace.save(file_name,"png")

def main():
    ume = umelaborize(2000,1000,'config.json')
    ume.load_image("test.jpg")
    ume.kill_paste(5000,False)
    ume.load_image("test2.jpg")
    ume.stamp_image(2,20)
    ume.test_show()
    ume.save_image("koiso.png")

if __name__ == '__main__':
<<<<<<< HEAD
    ume = umelaborize(2000, 1000, 'hoge.bmp', 0)
    print ume.config_json
    ume.load_image('20110501_215111.jpg')
    ume.kill_paste(5000,False)
    ume.load_image("IMG_4925.JPG")
    ume.kill_paste(5000,False)
    ume.test_show()
    ume.save_image("koiso.png")

    #main()
=======
    main()

>>>>>>> python3
