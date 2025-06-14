
import streamlit as st
import datetime

st.set_page_config(page_title="Deine KI-Assistenz", layout="centered")
st.title("🤖 Deine persönliche KI-Assistenz")

gender = st.radio("Wähle deinen Avatar:", ["Weiblich", "Männlich", "Neutral"])

if gender == "Weiblich":
    st.image("avatar_female.png", width=150)
    greeting = "Willkommen, meine Liebe. Wie kann ich dir heute helfen?"
elif gender == "Männlich":
    st.image("avatar_male.png", width=150)
    greeting = "Willkommen, mein Lieber. Was darf ich heute für dich tun?"
else:
    st.image("avatar_neutral.png", width=150)
    greeting = "Willkommen. Wie kann ich dich heute unterstützen?"

st.markdown(f"### {greeting}")

st.subheader("📒 Dein Notizblock")
note = st.text_area("Was möchtest du festhalten?", height=150)
if st.button("Notiz speichern"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("notizen.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {note}\n")
    st.success("✅ Notiz gespeichert!")

with st.expander("📚 Gespeicherte Notizen anzeigen"):
    try:
        with open("notizen.txt", "r", encoding="utf-8") as f:
            content = f.read()
            st.text(content if content else "Noch keine Notizen gespeichert.")
    except FileNotFoundError:
        st.info("Noch keine Notizen vorhanden.")
