
from rest_framework import serializers
from .models import Journal

class JournalListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Journal
        fields=['id','cover_image_url','title','slug','date','tags','read_time','excerpt','author','likes','is_featured']

class JournalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Journal
        fields=['cover_image_url','title','content','slug','date','excerpt','read_time','author','department','tags','status','batch','ig_username','li_username']
    

# Serializers are like translators. 
# They take your Django models (Journal objects) and 
# turn them into JSON so React can read them.

# Django by itself is good at serving HTML pages. 
# But your React frontend does not want HTML, it wants JSON data.
# Django REST Framework (DRF) is a tool that makes 
# building JSON APIs in Django simple.

# questiona arises why we didnt use serilaizer 
# in case of books fetching we have also object models there 