import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import vobject

# Authenticate
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

# UI
st.title("📇 Smart Contact Collector")

sheet_name = st.text_input("Enter Sheet Name:", "Data sheet (Responses)")

if st.button("Generate Contacts VCF"):
    try:
        sheet = client.open(sheet_name).sheet1
        data = pd.DataFrame(sheet.get_all_records())

        vcf = ''
        for index, row in data.iterrows():
            name = row['Full Name']
            email = row['Email Address']
            phone = str(row['Phone Number'])

            vcard = vobject.vCard()
            vcard.add('fn').value = name
            vcard.add('email').value = email
            tel = vcard.add('tel')
            tel.value = phone
            tel.type_param = 'CELL'

            vcf += vcard.serialize()

        with open("class_contacts.vcf", "w") as f:
            f.write(vcf)

        st.success("✅ VCF file generated successfully!")
        with open("class_contacts.vcf", "rb") as file:
            st.download_button("📥 Download VCF", file, file_name="class_contacts.vcf")

    except Exception as e:
        st.error(f"❌ Error: {e}")
