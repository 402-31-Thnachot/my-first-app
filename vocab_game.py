import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# กำหนดค่าเริ่มต้นใน session_state
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# ฟังก์ชันเริ่มเกมใหม่
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# Dialog แสดงผลลัพธ์
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog():
    st.balloons()

    score = 0

    user_answers = [
        st.session_state.ans1_val.strip().casefold(),
        st.session_state.ans2_val.strip().casefold(),
        st.session_state.ans3_val.strip().casefold(),
        st.session_state.ans4_val.strip().casefold(),
    ]

    correct_answers = [
        "apple",
        "fish",
        "green apple",
        "cherry",
    ]

    for index, (user_answer, correct_answer) in enumerate(
        zip(user_answers, correct_answers), start=1
    ):
        if user_answer == correct_answer:
            st.success(f"✅ ข้อ {index}: ถูกต้อง")
            score += 1
        else:
            st.error(
                f"❌ ข้อ {index}: ยังไม่ถูกต้อง "
                f"(คุณตอบ '{user_answer}')"
            )

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ปุ่มเริ่มเกม
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)


# แสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.is_ended:
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ช่องรับคำตอบ
st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    key="ans1_val",
)

st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    key="ans2_val",
)

st.text_input(
    "ข้อ 3: I like to eat a `g _ e e n  a p p l e`. 🍏",
    key="ans3_val",
)

st.text_input(
    "ข้อ 4: A `c _ e r r y` is a small red fruit. 🍒",
    key="ans4_val",
)


# ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.is_ended:
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    # อัปเดตหน้าจอทุก 1 วินาที
    time.sleep(1)
    st.rerun()


# แสดงผลลัพธ์
if st.session_state.is_ended:
    show_result_dialog()


st.divider()
st.write("นายธนโชติ ศรีคำ เลขที่ 31 ม.4/2")
