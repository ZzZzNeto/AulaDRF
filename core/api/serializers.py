from rest_framework import serializers

from core.models import Turma, Aluno

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'


from datetime import date

class AlunoSerializer(serializers.ModelSerializer):
    turma = TurmaSerializer(read_only=True)
    idade = serializers.SerializerMethodField('calcular_idade')

    class Meta:
        model = Aluno
        fields = ["nome", "matricula", "idade", "turma"]         

    def calcular_idade(self, instance):
        today = date.today()
        idade = today.year - instance.data_de_nascimento.year - (
            (today.month, today.day) < (instance.data_de_nascimento.month, instance.data_de_nascimento.day))
        return f"{idade} anos"










