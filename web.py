import streamlit as st
from LinFun import lineika
import locale
locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')


st.markdown("<h1 style='text-align: center; font-family: Helvetica, sans-serif; font-weight: bold;'>Проект 'П'</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-family: Helvetica, sans-serif; font-weight: bold;'>Найкорисніший застосунок 2024 року!</h2>", unsafe_allow_html=True)
st.write("Просто заповни поля своїми данними, і ти дізнаєшся розмір свого пісюнчика без допомоги лінійки!")

st.text_input(label="Як тебе звати?:", placeholder="Напиши сюди своє прекрасне ім'я!", key="name")

st.text_input(label="Число:", placeholder="Коли в тебе день народження!", key="day")

st.text_input(label="Місяць:", placeholder="Місяць, але не словом, думай довбешкою!", key="month")

st.text_input(label="Рік народження:", placeholder="Теж цифрами, ти ж розумний хлопчина!", key="year")

button_clicked = st.button("**Розрахунок**")

if button_clicked:
    name = st.session_state["name"]
    user = name.capitalize()
    try:
        day = float(st.session_state["day"])
        month = float(st.session_state["month"])
        year = float(st.session_state["year"])
        if day <= 31 and month <= 12 and year <= 2024:
            result = lineika(day, month, year)
            st.write(f"Ого! {user}, в тебе цілих {result} см м'ясної болтяри!")
        else:
            st.write(f"Так, бляха! {user}, ти або тупий, або кого ти збираєшся наїбати?")
    except ValueError:
        st.warning(f"{user} Ти шо плуг? Включай свою довбешку!")


