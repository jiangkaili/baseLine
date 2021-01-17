import pymysql
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from checkinfo.models import CheckInfo
from checkinfo.serializers import CheckInfoSerializer
from BaseLine.common.core.setting import Settings


def Index(request):
    return render(request, 'index.html')


class FindAll(APIView):
    """
    数据脱敏
    """

    def post(self, request):
        checkinfo = CheckInfo.objects.all()
        serializer = CheckInfoSerializer(checkinfo, many=True)
        for item in serializer.data:
            print(item)
        return Response({"data": serializer.data})


def GetAllData(request):
    connect = pymysql.Connect(
        host=Settings.DefaultMySQL.host,
        port=Settings.DefaultMySQL.port,
        user=Settings.DefaultMySQL.user,
        passwd=Settings.DefaultMySQL.password,
        db=Settings.DefaultMySQL.name,
        charset='utf8mb4'
    )
    cursor = connect.cursor()
    get_all_tables_sql = "select table_name from information_schema.tables where table_schema='attack';"
    cursor.execute(get_all_tables_sql)
    result = []
    for table_name in cursor.fetchall():
        get_table_data_sql = "select * from {}".format(table_name[0])
        cursor.execute(get_table_data_sql)
        data = []
        for row in cursor.fetchall():
            data.append(row)
        result.append(data)

    return JsonResponse({"data": result})
