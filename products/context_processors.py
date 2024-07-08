


import datetime
import  jdatetime
from django.utils import timezone
def public_value(request):
    return {
        'jalali_now': jdatetime.datetime.fromgregorian(datetime=timezone.now()).date().strftime('%Y/%m/%d'),
        'date_now': timezone.now().date()
    }