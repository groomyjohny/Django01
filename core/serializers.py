from rest_framework import serializers

import core.models


class ProcessRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = core.models.ProcessRecord
        fields = ['id', 'imageName', 'imagePath', 'osPid', 'osParentPid', 'timestampBegin', 'timestampEnd', 'cpuTimeNs']