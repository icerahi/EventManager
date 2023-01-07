from django.db.models.fields import EmailField
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        
        #add custom claim
        token['username']=user.username
        token['total_done']=user.task_set.filter(is_done=True).count()
        return token
    
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,style={'input_type':'password'})
    password2 = serializers.CharField(write_only=True,style={'input_type':'password'})
    email= serializers.EmailField(required=True)
    message = serializers.SerializerMethodField(read_only=True)
    token  = serializers.SerializerMethodField(read_only=True)
    # token_expires = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User 
        fields =(
            'username',
            'email',
            'password',
            'password2',
            'message',
            'token',
            # 'token_expires',
        )
        # extra_kwargs ={'password':{'write_only':True}}
    def get_message(self,obj):
        return f'Hi{obj.username}! Thanks for Joining!!'
    
    def get_token(self,obj):
        return get_tokens_for_user(obj)
    
    def validate_email(self,value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('User with this email already exists!')
        return value 
    
    def validate_username(self,value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError('User with is username already exists')
        return value 
    
    def validate(self,data):
        pw=data.get('password')
        pw2=data.pop('password2')
        if pw !=pw2:
            raise serializers.ValidationError('Password must be match!!')
        return data
    
    def create(self,validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user_obj = User(username=username,email=email)
        user_obj.set_password(password)
        # user_obj.active = False 
        user_obj.save()
        return user_obj

class ChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)
    class meta:
        model=User