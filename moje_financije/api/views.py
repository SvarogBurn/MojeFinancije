from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.serializer import AccountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Account

class AccountList(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        accounts = Account.objects.all()
        data = AccountSerializer(accounts, many=True).data
        return Response(data, status=status.HTTP_200_OK)

#stvaranje novog accounta
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetailView(APIView):
    
    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        account = self.get_object(pk)
        data = AccountSerializer(account).data
        return Response(data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        account = self.get_object(pk)
        serializer = AccountSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        account = self.get_object(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)