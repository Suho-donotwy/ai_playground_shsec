#stremlit packages
import streamlit as st

#basic packages
import pandas as pd
import numpy as np
import plotly.express as px

#Page Title
st.set_page_config(page_title="[CQ009] 이벤트 영향도 분석", page_icon="📈")

#Page Overview
st.markdown("# 이벤트 영향도 분석 #CQ009")
st.sidebar.header("이벤트 영향도 분석")
st.write(
    "이벤트에 따른 종목(한국 종목, 미국 종목)의 주가 등락에 대한 질문에 답변해요."
)

#Page Content 1
st.markdown("\n")
st.markdown("### 이벤트 상승/하락 영향도 분석")

#조회 질의 입력
st.markdown("\n")
st.markdown(
    "<p style='margin-bottom:0;'>질문을 입력해주세요. (ex. 현대글로비스가 선박 신규 계약 따면 어케될까..?)</p>",
    unsafe_allow_html=True
)
user_input = st.text_input("")

#결과 - 답변 요약
# 텍스트
summary_text = """
현대글로비스가 신규 선박 계약을 수주했을 때 과거 이력을 보면 19번 중 15번은 평균 8% 올랐고, 4번은 평균 0.6% 떨어졌어요. 최근 계약을 보면 LNG 및 자동차 운반 분야에서의 경쟁력을 강화하고, 해상 운송 사업의 포트폴리오를 다각화하고 있어요.
"""

# HTML 블록에 변수 삽입
st.markdown(f"""
    <div style="background-color:#F8FFCD; border-radius:5px;">
    <h4>결과</h4>
    """, unsafe_allow_html=True)

st.markdown("\n")

st.markdown(f"""
    <h6>요약</h6>
    {summary_text}
    """, unsafe_allow_html=True)

st.markdown("\n")

#결과 - 테이블
# CSV 파일을 읽어와 DataFrame으로 저장
df = pd.read_csv(".\contents\hyundai_glovis_contracts_sorted.csv", encoding='utf-8-sig')

# DataFrame을 Streamlit에 표로 출력
st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)

#결과 - 차트
# CSV 파일을 읽어와 DataFrame으로 저장
df = pd.read_csv(".\contents\hyundai_glovis_stock_trend.csv", encoding='utf-8-sig')

# Plotly를 사용한 선 그래프 생성
fig = px.line(df, x=df.date, y='value', title='시계열 데이터 시각화')

# 그래프 표시
st.plotly_chart(fig)