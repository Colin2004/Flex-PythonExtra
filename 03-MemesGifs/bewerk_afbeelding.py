from PIL import Image

# Afbeelding openen en oplsaan in de variabele met de naam: afbeelding
afbeelding = Image.open("Outer_Worlds_Max.png")

# De afbeelding tonen in de standaard image viewer van jouw systeem
afbeelding.show()

# De breedte en hoogte van de afbeelding lezen en tonen 
breedte = afbeelding.width
hoogte = afbeelding.height
helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

nieuwe_afmeting = (helft_breedte, helft_hoogte)


kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

# Nu de kleinere afbeelding opslaan me save(). Gebruik de originele bestandsnaam met ergens "klein" er in. 
kleinere_afbeelding.save('Outer_Worlds_Max_klein.png')






