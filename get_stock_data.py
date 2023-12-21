import yfinance as yf
from convert_date import *

def get_stock_data():
    while True:
        print("날짜를 자유롭게 입력해주세요(자연어, 단 2000년 이전의 날짜는 4자리 모두 입력해주세요)")
        day = convert_to_date(input())

        # stock_symbol에 분석하기 원하는 회사 이름 입력
        stock_symbol = "005930.KS"
        start = day[0]
        end = day[1]

    
        result = yf.download(stock_symbol, start=start, end=end)
            
        if not result.empty:
            return result
        else:
            print("날짜 입력이 잘못되었습니다. 인덱스가 비어있습니다.")