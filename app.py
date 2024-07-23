import streamlit as st
import pickle
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import sklearn


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

ps = PorterStemmer()
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)




st.title("E-mail/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

import streamlit as st

def predict_spam(input_sms):
    # Preprocessing
    transformed_sms = transform_text(input_sms)

    # Vectorize
    vector_input = tfidf.transform([transformed_sms])

    # Predict
    result = model.predict(vector_input)[0]
    return result

# Streamlit app logic
if st.button('Predict'):
    # Example input_sms, assuming it's defined somewhere in your code
    input_sms = st.text_area("Enter your SMS message")

    # Call the prediction function
    result = predict_spam(input_sms)

    # Display the result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
