from PIL import Image
from PIL.ExifTags import TAGS
    
def extract_all_exif(image_path):
    try:
        # Ouvrir l'image
        img = Image.open(image_path)


        # Vérifier si l'image a des données EXIF
        exif_data = img._getexif()
        if exif_data:
            print("\nToutes les balises EXIF de l'image:")
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")
        else:
            print("L'image ne contient pas de données EXIF.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Chemin vers l'image
image_path = "C:\\Users\\RYU.LAPTOP-N6A90JDT\\Desktop\\Metapic\\images\\IMG_2860.jpg"

# Extraire toutes les données EXIF
extract_all_exif(image_path)
