import qrcode
import streamlit as st
from io import BytesIO

def generate_qr(link):
    """Generates a QR code image from the given link."""
    features = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    features.add_data(link)
    features.make(fit=True)
    img = features.make_image(fill_color="black", back_color="white") 
    return img

st.title("📌 QR Code Generator")
st.write("Enter a link below to generate a QR code.")

user_link = st.text_input("🔗 Enter your URL:")

if st.button("🚀 Generate QR Code"):
    if user_link:
        qr_image = generate_qr(user_link)

        buf = BytesIO()
        qr_image.save(buf, format="PNG")
        buf.seek(0) 

        st.image(buf, caption="✅ Your QR Code", use_column_width=True)

        st.download_button(
            label="⬇️ Download QR Code",
            data=buf.getvalue(),
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.warning("⚠️ Please enter a valid link.")
        