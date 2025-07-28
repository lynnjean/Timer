import streamlit as st
import time

st.set_page_config(
    page_title='위니브 타이머',
    page_icon='⏱️',
    layout = 'centered'
)

# st.title('위니브 타이머')
# st.caption('작업 리듬을 만들어주는 음악 타이머')
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <h1 style="font-size: 3rem; font-weight: bold;">위니브 타이머</h1>
    <p style="color: #888; font-size: 0.8rem;">작업 리듬을 만들어주는 음악 타이머</p>
</div>
""", unsafe_allow_html=True)
