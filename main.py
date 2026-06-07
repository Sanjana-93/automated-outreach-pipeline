from utils.logger import log
from rich import print
from services.ocean_service import get_similar_companies
from services.prospeo_service import get_contacts
from services.eazyreach_service import get_email
from services.brevo_service import send_email

print("[bold green]\nAUTOMATED OUTREACH PIPELINE STARTED\n[/bold green]")

log("Pipeline Started")

domain = input("Enter company domain: ")

try:
    companies = get_similar_companies(domain)

except Exception as e:

    print(f"[red]Error while fetching companies: {e}[/red]")

    exit()

all_contacts = []

unique_emails = set()

for company in companies:

    try:

        contacts = get_contacts(company)

    except Exception as e:

        print(f"[red]Failed for {company}[/red]")

        continue

    for contact in contacts:

        email = get_email(contact["linkedin"])

        if email and email not in unique_emails:

            unique_emails.add(email)

            contact["email"] = email

            all_contacts.append(contact)

print("[bold yellow]\nREADY TO SEND EMAILS\n[/bold yellow]")

for contact in all_contacts:

    print(contact["name"], "-", contact["email"])

confirm = input("\nSend Emails? (y/n): ")

if confirm.lower() == "y":

    for contact in all_contacts:

        send_email(contact["email"], contact["name"])

        print(f"[green]✓ Email sent to {contact['name']}[/green]")
        log(f"Email sent to {contact['email']}")

else:

    print("\nEmail sending cancelled.")



























# from rich import print
# from dotenv import load_dotenv
# import os

# load_dotenv()

# brevo_key = os.getenv("BREVO_API_KEY")

# print("[green]Project Started Successfully[/green]")

# print("Brevo Key:", brevo_key)


# from services.brevo_service import send_email

# send_email(
#     "singhsanjana931981@gmail.com",
#     "Sanjana"
# )