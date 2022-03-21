from django.contrib import admin
from .models import Company
from .models import Asrusagereport
from .models import Shifts
from .models import Employee
from .models import Toleranceweight
from .models import Pallet
from .models import Qstatus
from .models import Materialinward
from .models import Materialoutward
from .models import Materialreload
from .models import Adjustmentreprocess
from .models import Changepassword

# Register your models here.

admin.site.register(Company)
admin.site.register(Asrusagereport)
admin.site.register(Shifts)
admin.site.register(Employee)
admin.site.register(Toleranceweight)
admin.site.register(Pallet)
admin.site.register(Qstatus)
admin.site.register(Materialinward)
admin.site.register(Materialoutward)
admin.site.register(Materialreload)
admin.site.register(Adjustmentreprocess)
admin.site.register(Changepassword)
