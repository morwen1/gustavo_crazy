from rest_framework import serializers
from PIL import image

class ImagesTransform (serializers.Serializer):
    #address = serializers.Charfield()
    image = serializer.ImageField()
    

    def create(self , data):
        import pdb; pdb.set_trace()