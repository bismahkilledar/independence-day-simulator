import io
from PIL import Image, ImageOps, ImageDraw, ImageFont
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="🇮🇳 Independence Day Greeting Creator",
    page_icon="🇮🇳",
    layout="centered"
)

# --- Custom UI Styling ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #FF9933 0%, #FFFFFF 50%, #138808 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #8b949e;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    .stDownloadButton button {
        background: linear-gradient(45deg, #FF9933, #138808);
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Header ---
st.markdown('<p class="main-title">Independence Day Creator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">✨ Crafted by Bismah Killedar ✨</p>', unsafe_allow_html=True)

# --- Sidebar Options ---
st.sidebar.markdown("### 🎨 Design Controls")
user_name = st.sidebar.text_input("Your Name", value="Bismah Killedar")

quote_options = {
    "Pride in our souls": "Freedom in our minds, faith in our words, pride in our souls. Happy Independence Day!",
    "Honor our heroes": "Let's honor the sacrifices of our brave heroes. Jai Hind!",
    "Tricolor fly high": "May the tricolor always fly high. Happy 79th Independence Day!"
}
selected_key = st.sidebar.selectbox("Choose Quote", list(quote_options.keys()))
quote_choice = quote_options[selected_key]

# --- Photo Upload ---
st.markdown("### 📸 Upload Your Photo")
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load user image
    user_img = Image.open(uploaded_file).convert("RGB")
    
    # --- Card Layout Configuration ---
    card_width = 600
    card_height = 850
    
    # Create clean white background card
    card = Image.new("RGB", (card_width, card_height), color="#FFFFFF")
    draw = ImageDraw.Draw(card)
    
    # 1. Elegant Top Tricolor Accent Bar (Thick & Clean)
    bar_height = 15
    draw.rectangle([0, 0, card_width, bar_height], fill="#FF9933")       # Saffron
    draw.rectangle([0, bar_height, card_width, bar_height*2], fill="#FFFFFF") # White separator line
    draw.rectangle([0, bar_height*2, card_width, bar_height*3], fill="#138808") # Green
    
    # 2. Add Title Header inside Card
    try:
        font_header = ImageFont.truetype("arial.ttf", 24)
        font_quote = ImageFont.truetype("arial.ttf", 18)
        font_name = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font_header = ImageFont.load_default()
        font_quote = ImageFont.load_default()
        font_name = ImageFont.load_default()

    # Draw Card Header Text
    header_text = "🇮🇳 HAPPY INDEPENDENCE DAY 🇮🇳"
    # Fallback positioning for text width
    draw.text((60, 50), header_text, fill="#000080", font=font_header)
    
    # 3. Process & Frame the User Photo
    photo_size = 420
    user_img = ImageOps.fit(user_img, (photo_size, photo_size), method=Image.Resampling.LANCZOS)
    
    photo_x = (card_width - photo_size) // 2
    photo_y = 100
    
    # Draw a stylish border box around the photo
    draw.rectangle([photo_x - 4, photo_y - 4, photo_x + photo_size + 4, photo_y + photo_size + 4], outline="#FF9933", width=4)
    card.paste(user_img, (photo_x, photo_y))
    
    # 4. Bottom Footer Banner for Quotes & Name (Navy Blue Background)
    footer_y = 550
    draw.rectangle([0, footer_y, card_width, card_height], fill="#000080")
    
    # Word wrapping for quote
    words = quote_choice.split(" ")
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if len(test_line) < 45: # Character length control per line
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())
    
    # Draw Quote Lines
    start_text_y = footer_y + 30
    for i, line in enumerate(lines):
        draw.text((40, start_text_y + (i * 26)), line, fill="#FFFFFF", font=font_quote)
    
    # Draw Creator Name
    name_display = f"— {user_name}"
    draw.text((40, start_text_y + (len(lines) * 26) + 20), name_display, fill="#FF9933", font=font_name)
    
    # --- Display Preview ---
    st.markdown("---")
    st.markdown("### 🌟 Preview")
    st.image(card, use_container_width=True)
    
    # --- Download ---
    st.markdown("### 📥 Save Your Card")
    buf = io.BytesIO()
    card.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="🚀 Download HD Card",
        data=byte_im,
        file_name="independence_day_card.png",
        mime="image/png"
    )
else:
    st.info("👆 Upload an image in the sidebar or above to see your newly styled greeting card.")
    
