import qrcode
import os
from PIL import Image, ImageDraw, ImageFont
from django.db import models
from django.contrib.auth.models import User
from menus.models import Menu
from configs.models import Config, Qrcode
from menyu.settings.base import BASE_DIR

def qrcode_location(instance, filename):
    return '%s/qrcode/%s' % (instance.owner.username, filename)

class Seat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()

    qrcode = models.ImageField(upload_to=qrcode_location, null=True, blank=True)

    def qrcode_gerator(self, instance):
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=14,
        border=1,
        ) # create qrcode
        menu = Menu.objects.get(owner=instance.owner) # find the menu
        #fill the qrcode with uuid of the menu and the table number
        qr.add_data('"uuid": "'+ str(menu.uuid)+'", "table": ' + str(self.number))
        #make fit? dont know
        qr.make(fit=True)
        #define the name of the qrcode
        filename = str(self.number)+".png"
        #trasform the qrcode in image
        img = qr.make_image()
        img_w, img_h = img.size
        #find the qrcode config
        qr_object = Config.objects.get(id=1)
        #open the base layout
        background = Image.open(qr_object.qrcode.qrcode).convert('RGBA')
        background = background.copy()
        bg_w, bg_h = background.size
        #offset where the qrcode will be placed
        offset = int(((bg_w - img_w) / 2)), int(((bg_h - img_h) / 2)- 5)
        #paste the qrcode inside the layout
        background.paste(img, offset)
        #create an image for the text
        txt = Image.new('RGBA', background.size, (255,255,255,0))
        #get the font
        fnt = ImageFont.truetype('qrcode/Roboto.ttf', 109)
        #draw contest
        d = ImageDraw.Draw(txt)
        d.text((460, 32), str(self.number).zfill(2), font=fnt, fill=(255,255,255,255))
        out = Image.alpha_composite(background, txt)
        if not(os.path.exists(os.path.dirname(BASE_DIR)+"/media/"+str(instance.owner)+"/qrcode/")):
            os.makedirs(os.path.dirname(BASE_DIR)+"/media/"+str(instance.owner)+"/qrcode/")
        #background.show()
        #save the qrcode

        out.save(os.path.dirname(BASE_DIR)+"/media/" + qrcode_location(self, filename), "PNG")
        return qrcode_location(self, filename)

    def save(self):
        self.qrcode = self.qrcode_gerator(self)

        super(Seat, self).save()

    def __str__(self):
        return str(self.owner)+" Mesa: "+str(self.number)
