from rest_framework.viewsets import ModelViewSet, generics

from core.models import Turma, Aluno
from core.api.serializers import TurmaSerializer, AlunoSerializer

from rest_framework import permissions, status
from rest_framework.response import Response
from datetime import datetime

class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework.viewsets import ModelViewSet, generics

class TesteViewSet(generics.ListAPIView):
    serializer_class = TurmaSerializer
    queryset = Turma.objects.all()
    permission_classes = [permissions.AllowAny]

from rest_framework.decorators import action

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    @action(methods=['get'],detail=False,url_path='bom_dia')
    def bom_dia(self, request, *args,**kwargs):
        return Response({"Bom dia meu bb!"}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        
        turma = Turma.objects.get(id=request.data.get("turma"))
        alunos = Aluno.objects.filter(turma__id=turma.id).count()

        try: 
            serializer = self.get_serializer(data=request.data)
            print(request.data['data_de_nascimento'])
            serializer.is_valid(raise_exception=True)

            serializer.validated_data['turma'] = turma
            data = request.data['data_de_nascimento']
            serializer.save(data_de_nascimento=datetime.strptime(data, f'%m/%d/%Y'))
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        except: 
            if alunos == turma.max_alunos:
                return Response(
                    {"Error": "Quantidade maxima de alunos nessa turma atingida"}, status=status.HTTP_400_BAD_REQUEST
            )
    


