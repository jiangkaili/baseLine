# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/12/25 10:44 上午
# @File    : serializers.py


from rest_framework import serializers

from .models import CheckInfo


class CheckInfoSerializer(serializers.ModelSerializer):
    """用户个人中心详细信息序列化器"""

    class Meta:
        model = CheckInfo
        fields = ('id', 'username', 'mobile', 'id_card')
