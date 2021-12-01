import midtransclient, uuid
from django.conf import settings

# Create Snap API instance
snap = midtransclient.Snap(
    # Set to true if you want Production Environment (accept real transaction).
    is_production=settings.MIDTRANS_IS_PRODUCTION,
    server_key=settings.MIDTRANS_SERVER_KEY
)

def generate_tx(user, fee):
    # Build API parameter

    order_id = str(uuid.uuid4())
    param = {
        "transaction_details": {
            "order_id": order_id,
            "gross_amount": fee
        }, "credit_card":{
            "secure" : True
        }, "customer_details":{
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.no_telepon
        }
    }
    transaction = snap.create_transaction(param)

    return order_id, transaction['token']

def tx_status(order_id):
    try:
        response = snap.transactions.status(order_id)
        status = response['transaction_status']
    except:
        return False
    if(status == 'capture' or status == 'settlement'):
        return True
    else:
        return False

