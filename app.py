import io
from PIL import Image, ImageOps, ImageDraw, ImageFont
import streamlit as st
import os
import requests

# --- Page Configuration & Modern Styling ---
st.set_page_config(
    page_title="🇮🇳 Digital Tricolor Card Creator",
    page_icon="🇮🇳",
    layout="centered"
)

# --- MODERN THEME & CSS ---
# Custom CSS to create a premium, dark-mode UI with saffron/green accents
st.markdown("""
    <style>
    /* Overall App Background */
    [data-testid="stAppViewContainer"] {
        background-color: #0E1117;
        color: #E0E0E0;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Main Title */
    .main-title {
        font-size: 3em;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #FF9933 0%, #FFFFFF 50%, #138808 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    /* Subtitle and Creator Tag */
    .sub-title {
        text-align: center;
        color: #A0A0A0;
        font-size: 1.2em;
        margin-bottom: 5px;
    }
    .creator-tag {
        text-align: center;
        color: #FF9933;
        font-weight: 600;
        margin-bottom: 30px;
        font-size: 1em;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161B22;
    }
    .sidebar-header {
        color: #FF9933;
        font-weight: bold;
    }

    /* File Uploader Customization */
    .stFileUpload {
        border: 2px dashed #FF9933;
        border-radius: 10px;
        padding: 10px;
        background-color: #161B22;
    }

    /* Result Card Styling */
    .result-card {
        border: 1px solid #30363D;
        border-radius: 15px;
        padding: 20px;
        background-color: #161B22;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        margin-top: 20px;
    }

    /* Stylish Button */
    .stDownloadButton button {
        background: linear-gradient(45deg, #FF9933, #138808);
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stDownloadButton button:hover {
        background: linear-gradient(45deg, #e68a2e, #117a07);
        transform: translateY(-2px);
    }
    
    /* Information Box */
    .stAlert > div {
        background-color: #161B22 !important;
        border-color: #FF9933 !important;
        color: #FF9933 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Header Section ---
st.markdown('<p class="main-title">Digital Tricolor Card Creator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Turn your photo into a patriotic masterpiece.</p>', unsafe_allow_html=True)
st.markdown('<p class="creator-tag">✨ Crafted by Bismah Killedar ✨</p>', unsafe_allow_html=True)

# --- Sidebar: Customization Panel ---
st.sidebar.markdown('<h2 class="sidebar-header">🎨 Customization</h2>', unsafe_allow_html=True)
user_name = st.sidebar.text_input("Your Name / Handle", value="Bismah Killedar")

quote_options = {
    "Freedom in our minds...": "Freedom in our minds, faith in our words, pride in our souls. Happy Independence Day!",
    "Salute the heroes...": "Let's honor the sacrifices of our brave heroes. Jai Hind!",
    "Tricolor flying high...": "May the tricolor always fly high. Happy 79th Independence Day!"
}
selected_quote_key = st.sidebar.selectbox("Select Your Favorite Quote", list(quote_options.keys()))
quote_choice = quote_options[selected_quote_key]

# --- Main Section: Photo Upload ---
st.markdown("### 📸 Step 1: Upload Your Photo")
uploaded_file = st.file_uploader(" ", type=["jpg", "jpeg", "png"])

# --- Processing Logic (Generates the Card) ---
if uploaded_file is not None:
    # Load user image
    user_img = Image.open(uploaded_file).convert("RGB")
    
    # Define dimensions for the final card (500x800)
    card_width = 500
    card_height = 800
    
    # Create a blank white canvas
    card = Image.new("RGB", (card_width, card_height), color="#FFFFFF")
    draw = ImageDraw.Draw(card)
    
    # 1. Draw the Tricolor Border
    border_height = 25
    draw.rectangle([0, 0, card_width, border_height], fill="#FF9933") # Saffron
    draw.rectangle([0, border_height, card_width, border_height*2], fill="#FFFFFF") # White
    draw.rectangle([0, border_height*2, card_width, border_height*3], fill="#138808") # Green
    
    # Define the area where the main design goes (below the border)
    content_y_start = border_height * 3
    content_height = card_height - content_y_start
    
    # 2. Create the Content Area (Use a dark navy background for premium look)
    content_area = Image.new("RGB", (card_width, content_height), color="#000080")
    
    # 3. Process the User's Photo (Center & Resize)
    # Calculate size to fit (e.g., 400x400 square)
    target_size = 400
    user_img = ImageOps.fit(user_img, (target_size, target_size), method=Image.Resampling.LANCZOS)
    
    # Calculate position to center photo on the content area
    photo_x = (card_width - target_size) // 2
    photo_y = 50 # Space from top of content area
    content_area.paste(user_img, (photo_x, photo_y))
    
    # 4. Add Text Section (Quote & Name)
    text_y_start = photo_y + target_size + 40
    
    try:
        # Try loading a custom font; fallback to default if not available
        # Note: You might need to adjust the path if using a server-hosted font
        font_quote = ImageFont.truetype("arial.ttf", 22)
        font_name = ImageFont.truetype("arial.ttf", 18)
    except IOError:
        font_quote = ImageFont.load_default()
        font_name = ImageFont.load_default()

    # Draw Quote (White, Centered, Multi-line wrap)
    quote_lines = []
    words = quote_choice.split(" ")
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        test_width, _ = draw.textbbox((0, 0), test_line, font=font_quote)[2:]
        if test_width < (card_width - 60):
            current_line = test_line
        else:
            quote_lines.append(current_line.strip())
            current_line = word + " "
    quote_lines.append(current_line.strip())
    
    line_height = 28
    for i, line in enumerate(quote_lines):
        text_width, _ = draw.textbbox((0, 0), line, font=font_quote)[2:]
        text_x = (card_width - text_width) // 2
        text_y = text_y_start + (i * line_height)
        content_area.paste(Image.new("RGB", (1,1), "#FFFFFF"), (0,0)) # dummy paste to get draw object
        draw_content = ImageDraw.Draw(content_area)
        draw_content.text((text_x, text_y), line, fill="#FFFFFF", font=font_quote, align="center")

    # Draw Creator Name (Saffron, Centered)
    name_text = f"— {user_name}"
    name_width, _ = draw.textbbox((0, 0), name_text, font=font_name)[2:]
    name_x = (card_width - name_width) // 2
    name_y = text_y_start + (len(quote_lines) * line_height) + 30
    draw_content.text((name_x, name_y), name_text, fill="#FF9933", font=font_name)
    
    # 5. Composite Final Card
    card.paste(content_area, (0, content_y_start))
    
    # --- Display Result ---
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown("### 🌟 Step 2: Your Final Masterpiece")
    st.image(card, use_container_width=True)
    
    # --- Download Section ---
    st.markdown("### 📥 Step 3: Save & Share")
    
    buf = io.BytesIO()
    card.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="🚀 Download Your HD Greeting Card (PNG)",
        data=byte_im,
        file_name="my_independence_day_card.png",
        mime="image/png"
    )
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # Initial state: Show upload prompt
    st.info("👆 Upload a picture from your device using the box above to start creating your card.")
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
