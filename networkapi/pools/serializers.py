from rest_framework import serializers
from networkapi.requisicaovips.models import ServerPool, ServerPoolMember
from networkapi.healthcheckexpect.models import Healthcheck
from networkapi.equipamento.models import Equipamento


class ServerPoolDatatableSerializer(serializers.ModelSerializer):

    healthcheck = serializers.RelatedField(
        source='healthcheck.healthcheck_type'
    )

    environment = serializers.RelatedField(
        source='environment.name'
    )

    class Meta:
        model = ServerPool
        fields = (
            'id',
            'identifier',
            'default_port',
            'healthcheck',
            'environment',
            'pool_created'
        )


class ServerPoolMemberSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = ServerPoolMember
        fields = ('id',
                  'server_pool',
                  'identifier',
                  'ipv6', 'ip',
                  'priority',
                  'weight',
                  'limit',
                  'port_real',
                  'healthcheck'
                  )


class ServerPoolSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = ServerPool
        fields = (
            'id',
            'identifier',
            'default_port',
            'healthcheck',
            'environment',
            'pool_created'
        )


class HealthcheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Healthcheck
        fields = ('id',
                  'identifier',
                  'healthcheck_type',
                  'healthcheck_request',
                  'healthcheck_expect',
                  'destination'
                  )

class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = ('id',
                  'tipo_equipamento',
                  'modelo',
                  'nome',
                  'grupos'
                 )