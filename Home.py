import streamlit as st

st.set_page_config(
    page_title="AI Playground",
    page_icon="👋",
)

st.write("# AI Playground! 👋")

st.sidebar.success("데모 기능을 선택해주세요")

st.markdown(
    """
    신한투자증권 AI Playground 입니다.\n
    AI솔루션부에서 개발한 다양한 데모 기능을 활용해보실 수 있어요!\n
    **👈 좌측에서 데모를 선택해주세요**
    """
)
st.markdown("\n")
st.markdown("\n")

st.markdown(
    """
    ##### 참고 용어\n
    a. 컴포넌트 ('C'로 시작하는 데모 기능) ex.CQ008\n
        - API로 구현된 기능으로 화면 구성에 직접적으로 활용\n
    b. 모듈 ('M'으로 시작하는 데모 기능)  ex.MN102\n
        - 컴포넌트를 구성하기 위해 구현된 내부 API 혹은 함수 (컴포넌트화 되어서 활용됨)\n
    """
)