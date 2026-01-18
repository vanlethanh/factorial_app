import streamlit as st
from factorial import fact

def main():
    st.title("Chương trình tính giai thừa")
    number=st.number_input("Nhập số: ",min_value=0,max_value=900)
    if st.button("Tính giai thừa"):
        result=fact(number)
        st.write(f"Giai thừa của {number} là {result}")

if __name__=="__main__":
    main()

