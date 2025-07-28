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



if 'timer_running' not in st.session_state:
    st.session_state.timer_running=False
if 'timer_paused' not in st.session_state:
    st.session_state.timer_paused=False
if 'start_time' not in st.session_state:
    st.session_state.start_time=None
if 'total_pause_time' not in st.session_state:
    st.session_state.total_pause_time=0
if 'total_seconds' not in st.session_state:
    st.session_state.total_seconds=25*60
if 'timer_completed' not in st.session_state:
    st.session_state.timer_completed=False
if 'show_celebration' not in st.session_state:
    st.session_state.show_celebration=False
if 'remaining_seconds' not in st.session_state:
    st.session_state.remaining_seconds=25*60

def update_timer():
    if st.session_state.timer_running and not st.session_state.timer_paused: # 타이머가 실행중
        current_time=time.time()
        elapsed = current_time-st.session_state.start_time-st.session_state.total_pause_time
        remaining = st.session_state.total_seconds-int(elapsed)

        if remaining<=0:
            st.session_state.remaining_seconds = 0
            st.session_state.timer_running = False
            st.session_state.timer_completed = True
            st.session_state.show_celebration = True
        else:
            st.session_state.remaining_seconds = remaining

def get_timer_status():
    # 타이머가 완료되었을때
    if st.session_state.timer_completed:
        return "completed"
    # 타이머가 진행중이고 정지 버튼을 누르지 않았을때
    elif st.session_state.timer_running and not st.session_state.timer_paused:
        return "running"
    # 타이머 정지 버튼을 눌렀을때
    elif st.session_state.timer_paused:
        return "paused"
    # 그외
    else:
        return "stopped"

update_timer()
current_status=get_timer_status()

col_left, col_right = st.columns(2)

with col_left:
    if st.session_state.total_seconds>0:
        progress = st.session_state.remaining_seconds/st.session_state.total_seconds
        progress = max(0,min(1,progress)) # 0-1 사이값만 출력되도록 설정
    else:
        progress=0 
    
    st.progress(float(progress))

    status_col1, status_col2, status_col3 = st.columns(3)
    with status_col1:
        if current_status=="running":
            st.markdown('타이머',help="타이머가 실행중입니다!")      
        elif current_status=="paused":
            st.markdown('타이머',help="타이머가 일시 정지 되었습니다!") 
        elif current_status=="completed":
            st.markdown('타이머',help="타이머가 완료되었습니다!") 
        else:
            st.markdown('타이머',help="타이머가 대기중입니다!") 
    with status_col3:
        st.markdown(f'{int(progress*100)}%')

with col_right:
    pass