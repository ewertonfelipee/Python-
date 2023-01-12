emails = [
    ",asdasd@gmail.com",
    "dfkodfko@hotmail.com",
    "SF,sdf@outlook.c'om",
    "   gkogko@apple.com    "
]

emails_tratados = [email.strip().replace(",","").replace("'","").lower() for email in emails]
emails_tratados_apple = [email.strip().replace(",","").replace("'","").lower() for email in emails if "@apple" in email]
print(emails_tratados)
print(emails_tratados_apple)