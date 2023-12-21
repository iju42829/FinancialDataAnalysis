from get_stock_data import *
from draw_graph import *

def main():
    # 주식 정보 가져오기
    sec = get_stock_data()

    # 주식 차트 및 예측 하기
    draw_graph(sec)
    
if __name__ == "__main__":
    main()
    