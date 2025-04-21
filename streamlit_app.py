import requests
import streamlit as st

st.title("Simple FastAPI application")

tab1, tab2, tab3 = st.tabs(['Image', 'Text', 'Table'])

def main():
    with tab1:
        # create input form
        image = st.file_uploader("Classify an image", type=['jpg', 'jpeg'])
        if st.button("Classify!") and image is not None:
            # show image
            st.image(image)
            # format data for input format
            files = {"file": image.getvalue()}
            # send data and get the result
            res = requests.post("http://127.0.0.1:8000/clf_image", files=files).json()
            # print results
            st.write(f'Class name: {res["class_name"]}, class index: {res["class_index"]}')

    with tab2:
        txt = st.text_input('Classify text')
        if st.button('Classify'):
            text = {'text' : txt}
            res = requests.post("http://127.0.0.1:8000/clf_text", json=text)
            st.write(res.json()['label'])
            st.write(res.json()['prob'])
        
    with tab3: 
        st.write("Classify table data")
        with st.form("query_form"):
            # collect feature values
            feature1 = st.text_input("Input value 1", value="0.")
            feature2 = st.text_input("Input value 2", value='0.')
            # query button
            submitted = st.form_submit_button("Classify!")
            if submitted and feature1 and feature2:
                # convert to input format
                vector = {'feature1' : feature1, 'feature2' : feature2}
                # send data and get the result
                res = requests.post("http://127.0.0.1:8000/clf_table", json=vector)
                # print feature values and result
                st.write("feature1", feature1, "feature2", feature2)
                st.write(f"Predicted class is {res.json()['prediction']}")

if __name__ == '__main__':
    main()
