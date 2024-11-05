#stremlit packages
import streamlit as st
from streamlit_date_picker import date_range_picker, date_picker, PickerType

#basic packages
import time
import numpy as np
import pandas as pd
import datetime
from datetime import datetime, timedelta

#Page Title
st.set_page_config(page_title="등락 사유 및 근거 [CQ004]", page_icon="📈")

#Page Overview
st.markdown("# 등락 사유 및 근거 #CQ004")
st.sidebar.header("등락 사유")
st.write(
    "증시(KOSPI, KOSDAQ, NASDAQ, S&P 등), 종목(한국 종목, 미국 종목)의 일정 기간 동안 등락 사유를 확인할 수 있어요."
)

#Page Content 1
st.markdown("\n")
st.markdown("### 1. 특정 지수/종목의 등락 사유 및 근거")

#조회 대상 코드 입력
st.markdown("\n")
st.markdown(
    "<p style='margin-bottom:0;'>지수나 종목의 코드를 입력해주세요. ex. 코스피(KS11), 삼성전자(005930), SK하이닉스(000660)</p>",
    unsafe_allow_html=True
)
user_input = st.text_input("")

#조회 기간 입력
st.write("기간을 입력해주세요.")
default_start, default_end = datetime.now() - timedelta(days=1), datetime.now()
refresh_value = timedelta(days=1)
date_range_string = date_range_picker(picker_type=PickerType.date,
                                      start=default_start, end=default_end,
                                      key='date_range_picker',
                                      refresh_button={'is_show': True, 'button_name': 'Reset',
                                                      'refresh_value': refresh_value})

#결과 - 등락 사유
# 요약
summary_text = """
3분기 실적 전망과 시장에서의 치열한 경쟁 때문입니다. 삼성은 약 9.1조 원의 영업이익을 기록할 것으로 예측했지만, 이는 시장 기대치인 10조 원을 밑돌며 투자자들의 실망을 샀습니다. 또한 메모리 반도체 시장에서의 비용 증가와 경쟁사인 SK하이닉스의 최신 고대역폭 메모리(HBM) 출시에 밀려, 기술 경쟁에서 어려움을 겪고 있다는 평가를 받고 있습니다.
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

#결과 - 근거
# 뉴스 제목과 링크를 리스트로 준비
news_items = [
    {"title": "삼성전자, AI 반도체 시장서 경쟁력 저하", "link": "https://www.reuters.com/technology/samsungs-profit-recovery-seen-weakening-q3-2024-10-06/"},
    {"title": "메모리 반도체 수요 부진, 실적 악화", "link": "https://www.reuters.com/technology/samsungs-profit-recovery-seen-weakening-q3-2024-10-06/"},
    {"title": "외국인 투자자, 삼성전자 4조 원 순매도", "link": "https://blog.naver.com/PostView.nhn?blogId=youngeung2&logNo=223633138978"},
    {"title": "증권사, 삼성전자 목표 주가 30% 하향 조정", "link": "https://blog.naver.com/PostView.nhn?blogId=youngeung2&logNo=223633138978"}
]

# HTML 시작 태그
html_content = """
<h6>뉴스 출처</h6>
<ul>
"""

# 뉴스 항목을 HTML로 추가
for item in news_items:
    html_content += f"<li><a href='{item['link']}' target='_blank'>{item['title']}</a></li>"

# HTML 종료 태그
html_content += """
</ul>
</div>
"""

# HTML 렌더링
st.markdown(html_content, unsafe_allow_html=True)
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")

#Page Content 2
st.markdown("### 2. 주요 종목의 실시간 등락 사유")

st.markdown(f"""
    <div style="background-color:#F8FFCD; border-radius:5px;">
    <h4>결과</h4>
    """, unsafe_allow_html=True)

st.markdown("\n")

# CSV 파일을 읽어와 DataFrame으로 저장
df = pd.read_csv("stock_price_changes_without_source.csv", encoding='utf-8-sig')

# DataFrame을 Streamlit에 표로 출력
st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)