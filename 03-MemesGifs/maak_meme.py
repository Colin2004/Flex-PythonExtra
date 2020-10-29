from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("meme_background.jpg")

breedte = achtergrond.width
hoogte = achtergrond.height

achtergrond = achtergrond.resize((breedte *2,hoogte *2))

achtergrond.show()



lettertype = ImageFont.truetype("impact.ttf", 14)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "                                                                 You've worked with python for a couple hours. You forgot to test and got an error when finally done"

# Bereken de breedte en hoogte van de tekst
tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype) 
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

# Tekst positie berekenen
tekst_x = (breedte - tekst_breedte) / 4
tekst_y = (hoogte - tekst_hoogte) / 4

tekengebied.multiline_text((tekst_x-30, tekst_y-4), tekst, font=lettertype, fill=(255,255,255))


achtergrond.show()



#opslaan onder een andere naam
achtergrond.save("meme_met_tekst.jpg")

