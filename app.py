import io
from PIL import Image, ImageOps, ImageDraw, ImageFont
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Independence Day Selfie & Greeting Creator", 
    page_icon="🇮🇳", 
    layout="centered"
)

# Custom CSS Styling to make the app visually striking and engaging
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #FF9933;
        text-align: center;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .sub-text {
        text-align: center;
        color: #555555;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    .creator-tag {
        text-align: center;
        color: #138808;
        font-weight: 600;
        font-size: 0.95rem;
        margin-top: -15px;
        margin-bottom: 25px;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF9933;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #e0852b;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<p class="main-header">🇮🇳 Independence Day Creator 🇮🇳</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Transform your photos into vibrant patriotic greeting cards instantly!</p>', unsafe_allow_html=True)
st.markdown('<p class="creator-tag">✨ Created by Bismah Killedar ✨</p>', unsafe_allow_html=True)

# Sidebar Design
st.sidebar.markdown("### 🎨 Customization Panel")
st.sidebar.markdown("Make your greeting card unique:")

user_name = st.sidebar.text_input("Your Name / Handle", value="Bismah Killedar")
quote_choice = st.sidebar.selectbox(
    "Select Your Favorite Quote",
    [
        "Freedom in our minds, faith in our words, pride in our souls. Happy Independence Day!",
        "Let's honor the sacrifices of our brave heroes. Jai Hind!",
        "May the tricolor always fly high. Happy 79th Independence Day!"
    ]
)

# Main Upload Section in an attractive container
with st.container():
    st.markdown("### 📸 Step 1: Upload Your Photo")
    uploaded_file = st.file_uploader("Choose a selfie or picture (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and process image
    image = Image.open(uploaded_file).convert("RGB")
    image = ImageOps.fit(image, (500, 500), Image.Resampling.LANCZOS)
    
    # Create Canvas (500 width, 700 height)
    card_height = 700
    card = Image.new("RGB", (500, card_height), (255, 255, 255))
    
    # Draw Tricolor Header Bar
    draw = ImageDraw.Draw(card)
    draw.rectangle([0, 0, 500, 20], fill="#FF9933") # Saffron
    draw.rectangle([0, 20, 500, 40], fill="#FFFFFF") # White
    draw.rectangle([0, 40, 500, 60], fill="#138808") # Green
    
    # Paste user image onto the card
    card.paste(image, (0, 70))
    
    # Draw Navy Blue Footer Banner for Text
    draw.rectangle([0, 570, 500, 700], fill="#000080") 
    
    # Load fonts
    try:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    except Exception:
        font_title = None
        font_sub = None

    # Draw Text onto the banner
    draw.text((20, 590), f"✨ {quote_choice}", fill="#FFFFFF", font=font_title)
    draw.text((20, 645), f"— {user_name}", fill="#FF9933", font=font_sub)
    
    # Display the Result
    st.markdown("---")
    st.markdown("### 🌟 Step 2: Preview Your Masterpiece")
    st.image(card, use_container_width=True)
    
    # Download Button Section
    st.markdown("### 📥 Step 3: Download & Share")
    buf = io.BytesIO()
    card.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="🚀 Download Your Greeting Card",
        data=byte_im,
        file_name="independence_day_card.jpg",
        mime="image/jpeg"
    )
else:
    st.info("👆 Upload a picture above to kick off your custom design creation!")
