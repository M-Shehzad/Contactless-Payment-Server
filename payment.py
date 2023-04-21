import razorpay
import os
from dotenv import load_dotenv

load_dotenv()

client = razorpay.Client(auth=(os.environ.get('RAZORPAY_KEY'), os.environ.get('RAZORPAY_SECRET')))

def create_payment_link(amount, description, customer_name, customer_email, customer_contact):
    payment_link = client.payment_link.create({
        # "upi_link": True,
        "amount": amount,
        "currency": "INR",
        "description": description,
        "customer": {
            "name": customer_name,
            "email": customer_email,
            "contact": customer_contact
        },
        "notify": {
            "sms": True,
            "email": False,
            "whatsapp": True,
        },
          "reminder_enable": True,
          "notes": {
            "policy_name": "Hello world"
        },
        "callback_url": "https://tiarasjec.in/success",
        "callback_method": "get"
    })

    return payment_link

def fetch_payment(payment_id):
    try:
        return client.payment.fetch(payment_id)
    except razorpay.errors.RazorpayError as e:
        print(e)
        return False

def get_all_payment_links():
    return client.payment_link.all()

if __name__ == '__main__':
    payment_link = create_payment_link(100, "Test", "Pravin Kumar", "justpk88@gmail.com", "+918618782292")
    print(payment_link)

    # print(fetch_payment("pay_LaoQg8mqXZgUsI"))
    # client.payment_link.notifyBy("pay_LaoQg8mqXZgUsI", "email")
    # print(get_all_payment_links())



