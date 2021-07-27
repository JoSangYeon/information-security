"""
메뉴얼

① 각 해당 문항의 집단(개인차 변인, 집단차 변인으로 구성) 평균 점수
② 3개로 구성된 해당문항의 평균값 산출, 수식 = 각 3개 문항 평균
③ P-O fit sub-score: 각 요인별 점수 차이, 수식 = (5-abs(개인요인평균 – 집단요인평균))^2 : 범위 0~25
④ P-O fit total score : P-O fit sub-score 값들의 총합의 제곱근
⑤ P-O fit total score × 10 = 100 분위 점수 변경
⑥ 상중하 집단 구분: 1/3 씩 동일한 급간으로 구분

1. individual 속성에서 각 요인(총 4개)마다의 평균을 구함
1-1. 4개의 요인중 각각의 질문에 대한 평균 == 그냥 해당 요인의 모든 값의 평균
1-2. 개인은 설문을 한 당사자의 값으로만 판단
```
np.mean([aa,bb,cc])
Out[29]: 4.333333333333333
np.mean([2,5,4,1,6,6,3,5,6,6,5,5,3,5,2,6,4,4])
Out[30]: 4.333333333333333
```
2. 1과 같이 cultural 속성에서도 같이 값을 구함
2-1. 기업요인은 전체의 설문 데이터의 평균을 구함
3. 1(a)과 2(b)의 차이의 절대값(abs(a-b))를 5에서 뺌 즉, 5-abs(a-b)
4. 3에서 얻은 값을 => P-O fit total score
5. sum(P-O fit total score) * 5
5-1. sum(P-O fit total score) / 2 * 10
"""
import pandas as pd
import numpy as np

def calc_mean(data):
    """
    12개 문항을 3개씩 4개의 요인으로 나누고
    각 요인에 대한 설문 값의 평균을 구하는 함수
    :param data: pandas를 통해 추출한 설문 데이터 값
    :return: 각 요인에 대한 설문데이터 값의 평균(list)
    """
    T_data = data.T
    result = []
    for i in range(0, len(T_data), 3):
        tmp = np.mean([T_data[i], T_data[i + 1], T_data[i + 2]]).round(3)
        # print(T_data[i], end=", ")
        # print(T_data[i + 1], end=", ")
        # print(T_data[i + 2], "=>", tmp)
        result.append(tmp)
    return result

def calc_PO_fit(ind, cul):
    ind = np.array(ind)
    cul = np.array(cul)

    print(5-np.abs(ind-cul))
    print((np.sum(5-np.abs(ind-cul))/2*10).round(3))
    return

if __name__ == "__main__":
    ind_att = pd.read_csv('individual_attribute.csv')
    cul_att = pd.read_csv('cultural_attribute.csv')

    cul_data = np.array(cul_att.iloc[:,1:].values.tolist())
    ind_data = np.array(ind_att.iloc[4, 1:].values.tolist())
    result1 = calc_mean(ind_data)
    result2 = calc_mean(cul_data)
    print(result1)
    print(result2)

    calc_PO_fit(result1, result2)