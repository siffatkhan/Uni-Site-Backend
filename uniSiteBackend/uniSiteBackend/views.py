from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import smtplib
from email.mime.text import MIMEText

@csrf_exempt
def contact_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        try:
            email=settings.EMAIL_HOST_USER
            password=settings.EMAIL_HOST_PASSWORD
            port=settings.EMAIL_PORT
            # print(email)
            # print(password)
            # print(type(port))
            # print(port)

            # Email body
            msg = MIMEText(f"From: {name} <{email}>\n\n{message}")
            msg["Subject"] = f"New message from {name}"
            msg["From"] = email
            msg["To"] = email
            

            # Connect to Gmail SMTP
            server = smtplib.SMTP_SSL("smtp.gmail.com", port)
            server.login(email, password)
            server.send_message(msg)
            server.quit()

            return JsonResponse({"success": True, "message": "Email sent successfully!"})

        except Exception as e:
            print("EMAIL ERROR:", e)
            return JsonResponse({
                "success": False,
                "message": "Error sending email",
                "error": str(e)
            })

    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)


