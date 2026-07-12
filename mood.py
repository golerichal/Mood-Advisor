import streamlit as st 

st.title("🤗Mood Advisor")
st.subheader("A Simple Mood - Based Advice System")

mood=st.selectbox("How are you feeling today?",["select your mood","Happy😊","Sad 🥲","Angry 😡","stressed 😟","Tired 😪"])

if mood == "Happy😊":
    st.success( "That's Really Nice to hear 🤗")
    st.info("Advice: Keep doing whatever makes you feel  this way.")

elif mood== "Sad 🥲":
 st.info("I am sorry if you are feeling sad 😕")
 st.write("Advice: Talk to someone you love and feel comfortable")

elif mood== "Angry 😡":
 st.warning("it's totally okay...it's natural to feel angry sometime.")
 st.write("Advise:Take a deep breath and give  yourself some time")

elif mood== "stressed 😟":
   st.error("you're not weak for feeling stressed")
   st.write("Advise:Do Something that you like to do")


elif mood== "Tired 😪": 
   st.warning("You're not lazy,you're human")
   st.write("Advise:Rest without guilt,even a short pause can help you feel stronger again 🤍")

else:
  st.error("please select a mood. ")