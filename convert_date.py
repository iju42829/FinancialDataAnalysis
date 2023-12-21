from konlpy.tag import Okt
from datetime import datetime

def convert_to_date(input_str : str):
    okt = Okt()
    input_str = input_str.replace('-', ' - ').replace('/', ' ').replace('~', ' ')

    # 형태소 분석을 통해 명사 및 숫자 추출
    pos_tags = okt.pos(input_str)

    # 숫자만 추출
    numbers = [word.lower() if 'A' <= word <= 'Z' else word for word, pos in pos_tags if pos == 'Number']

    # 추출된 숫자가 여섯 개 이상인 경우에만 처리
    if len(numbers) >= 6:
        numbers = [num.replace('년', '').replace('월', '').replace('일', '').replace('year', '').replace('month', '').replace('day', '').replace('-', '') for num in numbers]

        year_first, month_first, day_first = map(int, numbers[:3])
        year_second, month_second, day_second = map(int, numbers[3:6])

        if (year_first < 100):
            year_first += 2000
        
        if (year_second < 100):
            year_second += 2000

        # 날짜 형식으로 변환
        try:
            parsed_date = datetime(year_first, month_first, day_first)
            parsed_date1 = datetime(year_second, month_second, day_second)
           
            return parsed_date.strftime("%Y-%m-%d"), parsed_date1.strftime("%Y-%m-%d")
        
        except ValueError:
            pass  # 올바른 날짜 형식이 아니면 무시

    return None, None  # 추출된 숫자가 부족하거나 형식이 맞지 않는 경우