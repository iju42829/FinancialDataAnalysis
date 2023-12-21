# 주식 분석 및 주식 가격 예측 프로젝트

이 프로젝트는 정보검색 과제를 위해 만들었습니다. Python 및 라이브러리를 사용하여 주식 분석 및 주식 가격 예측 프로젝트를 진행하였습니다.

## 개발 환경
- python 3.x
- visual studio code

## 사용한 라이브러리
- Okt
- prophet
- yfinance
- matplotlib

## 프로젝트 구조
- main.py : 주식 예측 프로젝트를 실행하는 주요 함수입니다.

        main() -> None

- convert_date.py : 입력 날짜를 형태소 분석을 통하여 유효한 날짜 형식으로 변경합니다. 

        convert_to_date(input_str : str)

- get_stock_data.py : Yahoo Finance API를 사용하여 주식 데이터를 가져옵니다.

        get_stock_data()

- draw_graph.py : 주식 차트 및 Prophet를 사용하여 주식 가격을 예측 한 뒤 그래프를 그립니다.

        draw_graph(sec) -> None

