import os
from redmail import EmailSender


#Send the email

email = EmailSender(
    host='smtp.gmail.com',
    port=587,
    username='nombre@email.com',
    password='xxxx yyyy zzzz aaaa'
)

email.send(
    subject="Datos de Sensores del DataCenter",
    sender="nombre@email.com",
    receivers=['nombre@mail.com, nombre2@mail.com, nombre@icloud.com'],  
    text="Valores de los sensores del DataCenter.",
    html="""
        <h1>Datos de los Sensores del DataCenter generados:</h1>
        {{ my_image1 }}
        {{ my_image2 }}
        <h1>@DATA 2024</h1>
    """,
    body_images={
        'my_image1': '/home/sudo/Data/imagen1.png',
        'my_image2': '/home/sudo/Data/imagen2.png',
    }
)
