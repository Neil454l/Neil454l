
import json
import os

import streamlit as st

state = 'state.json'
if not os.path.isfile(state):
    with open(state, 'w') as f:
        json.dump({'clicks': 0}, f)

with open(state) as f:
    counter = json.load(f)['clicks']

if st.button('Click me'):
    counter += 1

st.write(f'The button was clicked {counter} times')

with open(state, 'w') as f:
    json.dump({'clicks': counter}, f)
