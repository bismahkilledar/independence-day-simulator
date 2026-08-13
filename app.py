# Independence Day Simulator – `app.py`

```python
import streamlit as st
import time

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Independence Day Simulator 🇮🇳",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        180deg,
        #FF9933 0%,
        #FFF7ED 18%,
        #FFFFFF 45%,
        #F7FFF7 65%,
        #138808 100%
    );
}

/* Hide Streamlit Footer */
footer {
    visibility: hidden;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: 800;
    color: #000080;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #333333;
    margin-bottom: 30px;
}

/* Creator */
.creator {
    text-align: center;
    font-size: 17px;
    color: #000080;
    font-weight: bold;
    margin-top: 40px;
}

/* Cards */
.card {
    background: rgba(255, 255, 255, 0.90);
    padding: 25px;
    border-radius: 20px;
    margin: 15px 0px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.15);
}

/* Flag Animation */
.flag {
    text-align: center;
    font-size: 130px;
    animation: wave 2s infinite alternate;
}

@keyframes wave {

    0% {
        transform: rotate(-3deg);
    }

    100% {
        transform: rotate(3deg);
    }

}

/* Celebration Text */
.celebration {
    text-align: center;
    padding: 30px;
    background: rgba(255,255,255,0.85);
    border-radius: 25px;
    margin-top: 20px;
}

/* Timeline */
.timeline-card {
    background: rgba(255,255,255,0.92);
    padding: 18px;
    border-left: 6px solid #FF9933;
    border-radius: 10px;
    margin: 10px 0px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "flag_hoisted" not in st.session_state:
    st.session_state.flag_hoisted = False

if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "timeline_completed" not in st.session_state:
    st.session_state.timeline_completed = False


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="main-title">
        🇮🇳 Independence Day Simulator 🇮🇳
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        An Interactive Digital Experience Celebrating
        Freedom • Unity • Pride
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🇮🇳 Explore India")

page = st.sidebar.radio(
    "Choose your experience",
    [
        "🏠 Home",
        "🚩 Flag Hoisting",
        "📜 Freedom Journey",
        "🧠 Independence Quiz",
        "🎉 Grand Celebration"
    ]
)

st.sidebar.divider()

# Progress Calculation

completed_steps = 0

if st.session_state.flag_hoisted:
    completed_steps += 1

if st.session_state.timeline_completed:
    completed_steps += 1

if st.session_state.quiz_completed:
    completed_steps += 1

progress = completed_steps / 3

st.sidebar.write("### Your Progress")

st.sidebar.progress(progress)

st.sidebar.write(
    f"Completed: {completed_steps}/3 Activities"
)


# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Home":

    st.markdown(
        """
        <div class="card">

        <h2>🇮🇳 Welcome to the Independence Day Simulator</h2>

        <p>
        Step into an interactive journey celebrating India's
        freedom, history, unity and pride.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="card">
            <h3>🚩 Flag Hoisting</h3>
            <p>
            Experience a virtual Independence Day
            flag hoisting ceremony.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="card">
            <h3>📜 Freedom Journey</h3>
            <p>
            Explore important events that shaped
            India's journey to independence.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="card">
            <h3>🧠 Independence Quiz</h3>
            <p>
            Test your knowledge about India's
            freedom struggle.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="flag">
            🇮🇳
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(
        "🇮🇳 Begin your journey and celebrate the spirit of India!"
    )


# =========================================================
# FLAG HOISTING PAGE
# =========================================================

elif page == "🚩 Flag Hoisting":

    st.title("🚩 Virtual Flag Hoisting Ceremony")

    st.write(
        "Click the button below to begin the ceremony."
    )

    if not st.session_state.flag_hoisted:

        if st.button(
            "🚩 Start Flag Hoisting",
            use_container_width=True
        ):

            st.write("### Preparing the ceremony...")

            progress_bar = st.progress(0)

            flag_area = st.empty()

            for i in range(101):

                progress_bar.progress(i)

                height = 12 - int(i / 10)

                empty_space = "<br>" * max(height, 0)

                flag_area.markdown(
                    f"""
                    <div style="
                        text-align:center;
                        font-size:100px;
                    ">
                        {empty_space}
                        🇮🇳
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                time.sleep(0.02)

            st.session_state.flag_hoisted = True

            st.balloons()

            st.success(
                "🇮🇳 The National Flag has been proudly hoisted!"
            )

            st.markdown(
                """
                <div class="celebration">

                <h1>🇮🇳 JAI HIND! 🇮🇳</h1>

                <h2>Happy Independence Day!</h2>

                <p>
                Freedom in our minds.<br>
                Pride in our hearts.<br>
                Strength in our unity.
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.markdown(
            """
            <div class="flag">
                🇮🇳
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success(
            "🚩 The flag is proudly flying high!"
        )

        st.info(
            "🇮🇳 Freedom is not just a gift — it is a responsibility."
        )


# =========================================================
# FREEDOM JOURNEY
# =========================================================

elif page == "📜 Freedom Journey":

    st.title("📜 India's Journey to Independence")

    st.write(
        "Explore some important milestones in India's freedom movement."
    )

    events = [

        (
            "1857",
            "First War of Independence",
            "A major uprising against British rule that became an important early chapter in India's struggle for freedom."
        ),

        (
            "1885",
            "Indian National Congress",
            "The Indian National Congress was established and later played a major role in India's freedom movement."
        ),

        (
            "1919",
            "Jallianwala Bagh",
            "The Jallianwala Bagh massacre became a major turning point in India's struggle against British rule."
        ),

        (
            "1930",
            "Dandi March",
            "Mahatma Gandhi led the Salt March as part of the Civil Disobedience Movement."
        ),

        (
            "1942",
            "Quit India Movement",
            "The Quit India Movement called for the end of British rule in India."
        ),

        (
            "1947 🇮🇳",
            "India Becomes Independent",
            "On 15 August 1947, India achieved independence and began a new chapter in its history."
        )

    ]

    for year, title, description in events:

        with st.expander(f"🇮🇳 {year} — {title}"):

            st.markdown(
                f"""
                <div class="timeline-card">

                <h3>{year}</h3>

                <h4>{title}</h4>

                <p>{description}</p>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()

    if st.button(
        "✅ I Explored the Freedom Journey",
        use_container_width=True
    ):

        st.session_state.timeline_completed = True

        st.success(
            "📜 Freedom Journey Completed!"
        )

        st.balloons()


# =========================================================
# QUIZ PAGE
# =========================================================

elif page == "🧠 Independence Quiz":

    st.title("🧠 Independence Day Quiz")

    st.write(
        "Test your knowledge about India's history and independence."
    )

    questions = [

        {
            "question":
            "1. On which date did India gain independence?",

            "options":
            [
                "26 January 1950",
                "15 August 1947",
                "2 October 1947",
                "15 August 1950"
            ],

            "answer":
            "15 August 1947"
        },

        {
            "question":
            "2. Who led the Dandi March in 1930?",

            "options":
            [
                "Jawaharlal Nehru",
                "Mahatma Gandhi",
                "Sardar Patel",
                "Subhas Chandra Bose"
            ],

            "answer":
            "Mahatma Gandhi"
        },

        {
            "question":
            "3. Who was India's first Prime Minister?",

            "options":
            [
                "Dr. B. R. Ambedkar",
                "Sardar Vallabhbhai Patel",
                "Jawaharlal Nehru",
                "Rajendra Prasad"
            ],

            "answer":
            "Jawaharlal Nehru"
        },

        {
            "question":
            "4. Which movement was launched in 1942?",

            "options":
            [
                "Swadeshi Movement",
                "Quit India Movement",
                "Non-Cooperation Movement",
                "Civil Disobedience Movement"
            ],

            "answer":
            "Quit India Movement"
        },

        {
            "question":
            "5. What is the national emblem of India adapted from?",

            "options":
            [
                "Gateway of India",
                "Ashoka Lion Capital",
                "India Gate",
                "Taj Mahal"
            ],

            "answer":
            "Ashoka Lion Capital"
        }

    ]

    answers = []

    for i, q in enumerate(questions):

        st.markdown(f"### {q['question']}")

        selected_answer = st.radio(
            "Choose your answer:",
            q["options"],
            key=f"question_{i}"
        )

        answers.append(selected_answer)

        st.divider()

    if st.button(
        "🏆 Submit Quiz",
        use_container_width=True
    ):

        score = 0

        for i, q in enumerate(questions):

            if answers[i] == q["answer"]:
                score += 1

        st.session_state.quiz_score = score
        st.session_state.quiz_completed = True

        st.subheader(
            f"🏆 Your Score: {score} / {len(questions)}"
        )

        percentage = (score / len(questions)) * 100

        st.progress(int(percentage))

        if score == 5:

            st.balloons()

            st.success(
                "🇮🇳 Outstanding! Excellent knowledge of India's independence!"
            )

        elif score >= 3:

            st.info(
                "👏 Great job! Keep exploring India's inspiring history."
            )

        else:

            st.warning(
                "Keep learning and try the quiz again!"
            )


# =========================================================
# GRAND CELEBRATION
# =========================================================

elif page == "🎉 Grand Celebration":

    st.title("🎉 Grand Independence Day Celebration")

    if not st.session_state.flag_hoisted:

        st.warning(
            "🚩 Please complete the Flag Hoisting Ceremony first."
        )

    elif not st.session_state.timeline_completed:

        st.warning(
            "📜 Please explore India's Freedom Journey first."
        )

    elif not st.session_state.quiz_completed:

        st.warning(
            "🧠 Please complete the Independence Quiz first."
        )

    else:

        st.markdown(
            """
            <div class="flag">
                🇮🇳
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="celebration">

            <h1>🎆 HAPPY INDEPENDENCE DAY! 🎆</h1>

            <h2>🇮🇳 Freedom • Unity • Pride 🇮🇳</h2>

            <p>
            Let us remember the sacrifices of those who fought
            for India's freedom and continue working together
            for a stronger and brighter future.
            </p>

            <h2>🇮🇳 JAI HIND! 🇮🇳</h2>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🚩 Flag Hoisting",
                "Completed"
            )

        with col2:

            st.metric(
                "🧠 Quiz Score",
                f"{st.session_state.quiz_score}/5"
            )

        with col3:

            st.metric(
                "🎉 Celebration",
                "Unlocked"
            )

        st.divider()

        if st.button(
            "🎊 Celebrate India!",
            use_container_width=True
        ):

            st.balloons()

            st.success(
                "🇮🇳 वंदे मातरम्! जय हिंद! 🇮🇳"
            )

            st.markdown(
                """
                # 🇮🇳 Proud To Be Indian 🇮🇳

                ### Unity in Diversity

                ### Strength in Freedom

                ### Pride in India
                """
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="creator">
        🇮🇳 Created by Bismah Killedar 🇮🇳
        <br>
        Celebrating Freedom • Unity • Pride
    </div>
    """,
    unsafe_allow_html=True
)
```
    
