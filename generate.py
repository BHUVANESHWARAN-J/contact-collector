import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import vobject

# Google Sheets Authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

# User inputs Google Sheet name
sheet_name = input("Enter the Google Sheet name: ")

try:
    sheet = client.open(sheet_name).sheet1
    data = pd.DataFrame(sheet.get_all_records())

    print(f"✅ Successfully fetched data from '{sheet_name}'")

    # User inputs column headers dynamically
    name_field = input("Enter the column header for Name: ")
    email_field = input("Enter the column header for Email: ")
    phone_field = input("Enter the column header for Phone Number: ")

    vcf = ""
    for _, row in data.iterrows():
        name = row[name_field]
        email = row[email_field]
        phone = str(row[phone_field])

        vcard = vobject.vCard()
        vcard.add('fn').value = name
        vcard.add('email').value = email
        tel = vcard.add('tel')
        tel.value = phone
        tel.type_param = 'CELL'
        vcf += vcard.serialize()

    with open("class_contacts.vcf", "w") as f:
        f.write(vcf)

    print("✅ VCF file 'class_contacts.vcf' created successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
