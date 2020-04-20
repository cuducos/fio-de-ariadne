from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from web.core.models import Kid


class KidResource(DjangoResource):
    preparer = FieldsPreparer(
        fields={field.name: field.name for field in Kid._meta.fields}
    )

    valid_url_params = set(field.name for field in Kid._meta.fields)

    def list(self):
        if not self.request.GET:
            return Kid.objects.all()

        kwargs = {
            key: value
            for key, value in self.request.GET.items()
            if key in self.valid_url_params
        }
        return Kid.objects.filter(**kwargs)
