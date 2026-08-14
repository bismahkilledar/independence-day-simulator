import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# 1. Page Configuration & Aesthetic Dark Theme Styling
st.set_page_config(
    page_title="Independence Day Selfie Experience",
    page_icon="🇮🇳",
    layout="centered"
)

st.markdown("""
    <style>
        /* Global Background & Dark Aesthetic */
        .stApp {
            background-color: #0B0F17;
            color: #E2E8F0;
        }
        
        /* Custom Header Styling */
        .main-header {
            text-align: center;
            padding: 10px 0 20px 0;
        }
        .tricolor-title {
            font-size: 2.2rem;
            font-weight: 800;
            letter-spacing: 0.15em;
            background: linear-gradient(90deg, #FF9933, #FFFFFF, #138808);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 4px;
        }
        .subtitle {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.3em;
            color: #94A3B8;
        }

        /* Glassmorphic Cards */
        div[data-testid="stExpander"], div[data-testid="stVerticalBlock"] > div.element-container {
            border-radius: 16px;
        }

        /* Button Enhancements */
        div.stButton > button {
            background: linear-gradient(135deg, rgba(255,153,51,0.2), rgba(19,136,8,0.2));
            color: #F8FAFC;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            font-weight: 600;
            letter-spacing: 0.05em;
            transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            border-color: #FF9933;
            box-shadow: 0 0 15px rgba(255, 153, 51, 0.3);
            color: #FFFFFF;
        }
        
        /* Download Button */
        div.stDownloadButton > button {
            background-color: #138808;
            color: white;
            border-radius: 12px;
            border: none;
            font-weight: 600;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Header Section
st.markdown("""
    <div class="main-header">
        <p class="subtitle">15th August • Interactive Tribute</p>
        <h1 class="tricolor-title">VANDE MATARAM</h1>
        <p style="color: #64748B; font-size: 0.85rem; font-style: italic;">
            "Pride in our hearts, freedom in our soul."
        </p>
    </div>
""", unsafe_allow_html=True)

# 3. Ambient Background Audio Player (Looping Drone/Harmony)
with st.expander("🎵 Ambient Soundtrack Settings", expanded=False):
    st.write("Enable patriotic ambient sound:")
    # Royalty-free calming ambient track
    audio_url = "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=meditation-flute-111816.mp3"
    st.audio(audio_url, format="audio/mp3", loop=True)

# 4. Image Processing Function: Applies Aesthetic Tricolor Frame & Badges
def apply_aesthetic_frame(image_input):
    # Open image & convert to RGBA
    img = Image.open(image_input).convert("RGBA")
    w, h = img.size
    
    # Create overlay drawing context
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # 1. Outer Tricolor Gradient Frame
    border_thickness = int(min(w, h) * 0.035)
    
    # Top border (Saffron)
    draw.rectangle([(0, 0), (w, border_thickness)], fill=(255, 153, 51, 230))
    # Bottom border (Green)
    draw.rectangle([(0, h - border_thickness), (w, h)], fill=(19, 136, 8, 230))
    # Left border (Gradient simulation: Saffron to Green)
    draw.rectangle([(0, 0), (border_thickness, h // 2)], fill=(255, 153, 51, 230))
    draw.rectangle([(0, h // 2), (border_thickness, h)], fill=(19, 136, 8, 230))
    # Right border
    draw.rectangle([(w - border_thickness, 0), (w, h // 2)], fill=(255, 153, 51, 230))
    draw.rectangle([(w - border_thickness, h // 2), (w, h)], fill=(19, 136, 8, 230))

    # 2. Bottom Glass Badge Container
    badge_height = int(h * 0.13)
    badge_margin = int(w * 0.05)
    badge_box = [
        badge_margin, 
        h - badge_height - border_thickness - 10, 
        w - badge_margin, 
        h - border_thickness - 10
    ]
    
    # Draw rounded glass panel for text
    draw.rounded_rectangle(badge_box, radius=16, fill=(10, 15, 23, 200), outline=(255, 255, 255, 40), width=1)

    # 3. Typography
    try:
        # Fallback to default if specific ttf not installed
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    except Exception:
        font_large = None
        font_small = None

    # Text Placement
    text_x = badge_margin + 20
    text_y_top = badge_box[1] + int(badge_height * 0.2)
    text_y_sub = text_y_top + int(badge_height * 0.38)

    draw.text((text_x, text_y_top), "VANDE MATARAM", fill=(255, 255, 255, 255), font=font_large)
    draw.text((text_x, text_y_sub), "🇮🇳 15 AUGUST • INDEPENDENCE DAY", fill=(255, 153, 51, 255), font=font_small)

    # Combine Base Image with Overlay
    final_image = Image.alpha_composite(img, overlay).convert("RGB")
    return final_image

# 5. Camera Input Section
st.write("")
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    camera_photo = st.camera_input("📸 Capture Your Selfie")

if camera_photo is not None:
    # Process the selfie with aesthetic frame
    with st.spinner("Applying aesthetic tricolor frame & badges..."):
        styled_image = apply_aesthetic_frame(camera_photo)

    st.write("")
    st.markdown("### 🇮🇳 Your Styled Tribute Selfie")
    st.image(styled_image, use_container_width=True)

    # Convert to bytes for download
    buf = io.BytesIO()
    styled_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Instant Download Button
    st.download_button(
        label="📥 Download Selfie",
        data=byte_im,
        file_name="independence_day_selfie.png",
        mime="image/png"
    )
    
    st.balloons()
    
