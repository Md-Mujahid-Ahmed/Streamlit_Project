import streamlit as st

st.title("Practicing")

st.header("Practicing Session For WebDeployment")
st.subheader("By Mohammed Mujahid Ahmed")

name = st.text_input("Please Input your name Here:")
st.write(f"Hello,{name} Welcome to the session")

course = st.radio("Select Course",["Data Science","Data Analysis","Full Stack"])
months = st.number_input("Select Months to complete these course:",min_value=3,max_value=9,step=3)
st.write(f"Hello {name} you have opted for {course} for {months} months")
ratings =st.slider(f"Choose ratings for the {course}",min_value=1.0,max_value=5.0,step=0.5)
st.write(f"{name} you have Given {ratings} for {course} course")

if course == "Data Analysis":
    st.write("You have 4 months to complete the course")
elif course == "Data Science":
    st.write("You have 9 months to complete the course")

st.image(r"https://r1.ilikewallpaper.net/ipad-pro-wallpapers/download/91346/sea-sky-clouds-nature-sunset-4k-ipad-pro-wallpaper-ilikewallpaper_com_200.jpg")

st.sidebar.title("Select a page")

st.line_chart(data=[1,3,4,2,5,6,9,8])

st.code("a = input('Enter a name')")

st.latex(r'''
         ar + ar ^ 2 + ar ^ 3 + \cdots + ar ^ n-1 + ar ^ n = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right) )
         ''')




