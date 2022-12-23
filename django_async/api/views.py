from django.http import JsonResponse
from rest_framework.response import Response
from adrf.views import APIView
from django.http import Http404
from rest_framework import status, viewsets, permissions
from api.models import Sources
from api.serializers import SourcesSerializer
import httpx
import json

class AsyncView(APIView):
    
    async def get(self, request, *args, **kwargs):
        sources = Sources.objects.all()
        serializer = SourcesSerializer(sources, many=True)
        return JsonResponse({"data": serializer.data})
    
    async def post(self, request, *args, **kwargs):
        serializer = SourcesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class DetailAsyncView(APIView):
    
    async def get(self, request, id):
        try:
            sources = Sources.objects.get(id=id)
        except:
            raise Http404
        serializer = SourcesSerializer(sources)
        async with httpx.AsyncClient() as client:
            r = await client.post(
                serializer.data["url"], 
                auth=(
                    serializer.data["basic_auth"]["login"], 
                    serializer.data["basic_auth"]["password"]
                ),
                json=serializer.data["request_body"]
            )
        json_data = []
        single_worker = {}
        list_of_workers = json.loads(json.dumps(r.json(), ensure_ascii=False))["Parameters"]
        for i in list_of_workers:
            single_worker.update({
                "id": i["ID"],
                "name": i["Name"],
                "last_name": i["Surname"],
                "phone": i["Phone"],
                "image_url": i["Photo"]
            })
            json_data.append({i: single_worker[i] if single_worker[i] is not None else "" for i in single_worker})
            single_worker = {}
        result = {"workers_list": json_data}
        return JsonResponse(result)
    
    async def put(self, request, id):
        try:
            source = Sources.objects.get(id=id)
        except:
            raise Http404
        serializer = SourcesSerializer(source, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    async def delete(self, request, id):
        try:
            source = Sources.objects.get(id=id)
            source.delete()
        except:
            raise Http404