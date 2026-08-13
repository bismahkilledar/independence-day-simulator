import io
from PIL import Image, ImageOps, ImageDraw, ImageFont
import streamlit as st

st.set_page_config(page_title="Independence Day Tricolor Generator", page_icon="🇮🇳", layout="centered")

st.title("🇮🇳 Independence Day Digital Selfie & Greeting Creator")
st.write("Create your custom patriotic selfie card and celebrate Freedom Day in style!")

# Sidebar Controls
st.sidebar.header("Customization Panel")
user_name = st.sidebar.text_input("Enter Your Name / Handle", value="Alfaz-e-Bismah")
quote_choice = st.sidebar.selectbox(
    "Choose a Quote",
    [
        "Freedom in our minds, faith in our words, pride in our souls. Happy Independence Day!",
        "Let's honor the sacrifices of our brave heroes. Jai Hind!",
        "May the tricolor always fly high. Happy 79th Independence Day!"
    ]
)

# Main Upload Section
uploaded_file = st.file_uploader("Upload your selfie or photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file).convert("RGB")
    
    # Resize image for uniformity
    image = ImageOps.fit(image, (500, 500), Image.Resampling.LANCZOS)
    
    # Create a canvas for the final card (500 width, 700 height to leave room for text/frames)
    card_height = 700
    card = Image.new("RGB", (500, card_height), (255, 255, 255))
    
    # Draw Tricolor Header Bar
    draw = ImageDraw.Draw(card)
    draw.rectangle([0, 0, 500, 20], fill="#FF9933") # Saffron
    draw.rectangle([0, 20, 500, 40], fill="#FFFFFF") # White
    draw.rectangle([0, 40, 500, 60], fill="#138808") # Green
    
    # Paste user selfie onto the card
    card.paste(image, (0, 70))
    
    # Draw Tricolor Footer Bar / Banner Area
    draw.rectangle([0, 570, 500, 700], fill="#000080") # Navy Blue background for text
    
    # Add text details
    try:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    except Exception:
        font_title = None
        font_sub = None

    # Draw Text
    draw.text((20, 590), f"✨ {quote_choice}", fill="#FFFFFF", font=font_title)
    draw.text((20, 650), f"— {user_name}", fill="#FF9933", font=font_sub)
    
    # Display the Result
    st.subheader("Your Independence Day Card Preview:")
    st.image(card, use_container_width=True)
    
    # Download Button
    buf = io.BytesIO()
    card.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="📥 Download Your Independence Day Selfie Card",
        data=byte_im,
        file_name="independence_day_card.jpg",
        mime="image/jpeg"
    )
else:
    st.info("👆 Please upload a photo using the uploader above to generate your customized creator tool card.")
    
