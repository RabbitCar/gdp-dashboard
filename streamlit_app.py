# streamlit_app.py
# 暮光之時：序章 - 光靈戰士的試煉（Streamlit 版）

import streamlit as st

# 試煉選項對應函式
def 試煉_力量():
    st.success("你踏入力量之門，一道光芒注入你的身體。你獲得了短暫的力量提升！")
    st.write("但你也感受到力量背後的沉重與壓力...")

def 試煉_智慧():
    st.success("你進入智慧之門，一位長者出現並出謎題考驗你的思維！")
    riddle = st.text_input("謎題：什麼東西越分享越多？")
    if riddle:
        if "知識" in riddle or "愛" in riddle:
            st.balloons()
            st.write("你答對了！你感受到知識的力量在你心中擴散！")
        else:
            st.warning("這似乎不是正確答案...")

def 試煉_信念():
    st.success("你走入信念之門，一片黑暗中，你只能靠內心前進...")
    st.write("你回想起家園的模樣，那份信念支撐你跨過前方的黑暗。")

def 開場劇情():
    st.markdown("### ✨ 序章：光靈戰士的試煉")
    st.write("你是光靈族的新戰士，被選中參加傳說中的試煉。")
    st.write("試煉中，通過試煉者將獲得光之碎片的祝福，獲得守護世界的力量。")
    st.write("然而，你並不知道，在這與世隔絕的空間外，黑暗正悄悄逼近…")

def 選擇試煉():
    st.markdown("---")
    st.markdown("### 🌀 選擇你的試煉之門")
    st.write("你站在三道光門前，每一道門散發不同的氣息：")
    choice = st.radio("請選擇要踏入哪一道門：", ["1. 力量之門 (挑戰你的體能)", "2. 智慧之門 (解開古老謎題)", "3. 信念之門 (面對內心的黑暗)"])

    if "力量" in choice:
        試煉_力量()
    elif "智慧" in choice:
        試煉_智慧()
    elif "信念" in choice:
        試煉_信念()

# 主程式入口
st.title("🌗 暮光之時 - 光與影的文字冒險")
st.caption("- 由你來決定世界的命運 -")

開場劇情()
選擇試煉()
