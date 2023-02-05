from rest_framework import viewsets 
from rest_framework import status
from rest_framework.response import Response
from apps.products.api.serializers.general_serializers import  MeasurenUnitSerializer,IndicatorSerializer,CategoryProductSerializer

class MeasureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurenUnitSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
        
    
class CategoryProductViewSet(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id = self.kwargs['pk'],state=True)
    
    def list(self,request):
        data = self.get_queryset()
        data = self.get_serializer(data,many=True)
        return Response(data.data)
    
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Categoria registrada correctamente'},status=status.HTTP_200_OK)
        return Response({'message':'','erro':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(),data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Categoria actualizada correctamente'},status=status.HTTP_200_OK)
        return Response({'message':'','erro':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        if self.get_object().exists():
            self.get_object().get().delete()
            return Response({'message':'Categoria eliminada correctamente'},status=status.HTTP_200_OK)
        return Response({'message':''},status=status.HTTP_400_BAD_REQUEST)