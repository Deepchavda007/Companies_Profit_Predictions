import pickle
import streamlit as st


profit_model = pickle.load(open(
    'profit_model.sav', 'rb'))

st.title('Companies Profit Predictions')


rdspend = st.number_input('Research and Development (R&D) Spend',
                          min_value=10000., step=1000.)
st.write('The current Value is ', rdspend)

administration = st.number_input(
    'Administration', min_value=10000., step=1000.)
st.write('The current Value is ', administration)


marketingspend = st.number_input(
    'Marketing Spend', min_value=10000., step=1000.)
st.write('The current Value is ', marketingspend)


profit_prediction = profit_model.predict(
    [[rdspend, administration, marketingspend]])


st.button('Companies Profit Result')


st.info(profit_prediction)
