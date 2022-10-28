from rest_framework import serializers

import core.models


class ProcessRecordSerializer(serializers.ModelSerializer):
    cpuTimeNs = serializers.ReadOnlyField()
    class Meta:
        model = core.models.ProcessRecord
        fields = ['id', 'imageName', 'imagePath', 'osPid', 'osParentPid', 'timestampBegin', 'timestampEnd', 'cpuCycles', 'cpuClockRate', 'cpuTimeNs']