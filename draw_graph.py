from prophet import Prophet
from prophet.plot import plot
import matplotlib.pyplot as plt

def draw_graph(sec) -> None:
    # 작년 종가
    last_year_close = sec['Close'].iloc[0]

    # 상승률 계산
    sec['Yearly_Return'] = ((sec['Close'] - last_year_close) / last_year_close) * 100

    # 그래프 그리기
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(18, 18), sharex=True)

    # 첫 번째 서브플롯 (가격)
    color = 'tab:blue'
    ax1.set_ylabel('Price', color=color)
    ax1.plot(sec.index, sec['Close'], color=color, label='Stock Price')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='upper left')

    # 두 번째 서브플롯 (상승률)
    color = 'tab:red'
    ax2.set_ylabel('Yearly Return %', color=color)
    ax2.plot(sec.index, sec['Yearly_Return'], color=color, linestyle='--', label='Yearly Return')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend(loc='upper left')

    plt.suptitle('Stock Price, Yearly Return', y=0.94)
    plt.show()

    df = sec

    # 데이터프레임의 인덱스를 사용하여 Date와 Close를 선택
    df_train = df.reset_index()[['Date', 'Close']]

    # 컬럼 이름 변경
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    # Prophet 모델 생성
    m = Prophet(changepoint_range=1, changepoint_prior_scale=0.5)

    # 모델 학습
    m.fit(df_train)

    # 미래를 예측하기 위한 데이터프레임 생성
    future = m.make_future_dataframe(periods=365)  # 1년치 예측

    # 예측 수행
    forecast = m.predict(future)

    # 상한가 및 하한가 설정
    percentage_range = 10
    forecast['yhat_upper'] = forecast['yhat'] * (1 + percentage_range / 100)
    forecast['yhat_lower'] = forecast['yhat'] * (1 - percentage_range / 100)

    # 예측 결과 시각화
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 원래의 주가 그리기
    ax.plot(df_train['ds'], df_train['y'], label='Actual Price', color='tab:blue')

    # 예상 주가 그리기
    ax.plot(forecast['ds'], forecast['yhat'], label='Predicted Price', color='tab:red')

    # 상한가 및 하한가 그리기
    ax.plot(forecast['ds'], forecast['yhat_upper'], linestyle='--', color='red', label=f'Upper Limit (+{percentage_range}%)')
    ax.plot(forecast['ds'], forecast['yhat_lower'], linestyle='--', color='green', label=f'Lower Limit (-{percentage_range}%)')

    # 변동점에 선 추가
    for changepoint in m.changepoints:
        plt.axvline(changepoint, linestyle='--', color='gray', alpha=0.5)

    # 레이블과 범례 추가
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Price Prediction')
    plt.legend()

    # 그래프 보기
    plt.show()

    fig = m.plot_components(forecast)
    plt.show()