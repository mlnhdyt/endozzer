from django.utils import timezone
import os


def join_img_upload(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"join/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

def campaign_img_upload(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"campaign/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

def get_tx_status(instance):
    from payment.models import Payment
    from payment.utils import tx_status

    pay = Payment.objects.filter(joinCampaign=instance)

    for p in pay:
        order_id = p.order_id
        if(tx_status(str(order_id))):
            return True
    return False

