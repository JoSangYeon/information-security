# TestModel
정보보안수준 TEST 모델입니다.

## UseCase 다이어그램

![TestModel_Usecase](img\0. TestModel_Usecase.jpg)

## Class 다이어그램

![TestModel_Class](img\0. TestModel_Class.PNG)

## Activity 다이어그램

![ActivityDiagram1](img\0. TestModel_Activity.jpg)

## 코드 스켈레톤

### 파일구성

1. main.py

   + Project의 main 파일입니다.
   + 해당 파일을 실행합니다.

2. Solution.py

   + Project 전체를 관장하는 class와 첫 시작화면 class를 담고있는 python 파일입니다.

3. Survey.py

   + 화면 2(설문)를 구성하는 class들을 담고 있는 python 파일입니다.
   + Survey1 class는 화면2-1(개인특성측정)
   + Survey2 class는 화면2-2(조직특성측정)
   + Survey3 class는 화면2-3(정보보안수준측정)

4. Result.py

   + 화면 3(결과산출)를 구성하는 class들을 담고 있는 python 파일입니다.
   + Result1 class는 화면 3-1(적합도산출)
   + Result2 class는 화면 3-2(IPA산출)

5. CSV files

   + 설문데이터를 저장하는 csv파일입니다.

   1. individual_attribute.csv
      + 개인특성 설문 데이터
   2. cultural_attribute.csv
      + 조직특성 설문 데이터
   3. Information_Security_Level.csv
      + 정보보안수준 설문 데이터

### Solution.py
#### class Project

```python
class Project(tk.Tk):
    """
    전체 소스코드를 관장하는 Project class
    tkinter 패키지의 TK() 객체를 상속하여 만든 클래스
    """
    def __init__(self):
        # 제목 설정
        # 창 크기 변경 (너비, 높이)

    def switch_frame(self, frame_class):
        """
        frame간 전환을 구현한 메소드
        :param frame_class: 스위치할 frame class명을 입력
        """
        # 매개변수로 받은 frame 객체를 생성
        # 기존에 있던 frame 삭제
        # 새로운 프레임 적용
        # pack()을 통한 배치
```

#### class Main_Frame

```python
class Main_Frame(tk.Frame):
    """
    화면 1-1를 구성하는 Frame class
    버튼은 총 3개로
    시작하기,
    결과확인,
    종료하기 이다.
    """
    def __init__(self, app):
        """
        frame 생성자
        각종 위젯들이 생성자에서 생성된다.
        :param app: 해당 frame을 호출한 Project 객체
        """

    def start_app(self):
        """
        버튼을 클릭하면, 다음화면(Frame(화면 2-1))으로 switching하는 메소드
        :return:
        """

    def start_result(self):
        """
        버튼을 클릭하면, 결과화면(Frame(화면 3-1))으로 switching하는 메소드
        :return:
        """
```

### Survey.py

#### Script

```python
"""
사용되는 설문 스크립트 각 화면에 맞게 dictionary형태로 구성함 
"""
SCRIPT = {
    'Survey1': [['나는 성과중심의 가치를 추구한다.',
                  '나는 일을 할 때, 성취 결과를 중요시한다.',
                  '나는 높은 성과를 이루는 것을 선호한다.'],
                 ['나는 인간관계중심의 가치를 추구한다.',
                  '나는 일을 할 때, 대인관계를 중요시한다.',
                  '나는 좋은 인간관계를 이루는 것을 선호한다.'],
                 ['나는 위험이 발생할 경우 안전한 선택을 우선시하는 편이다.',
                  '나는 손해가 발생하는 것을 경계한다.',
                  '나는 피해가 발생하지 않도록 우선적으로 노력한다.'],
                 ['나는 위험이 발생하더라도 이익을 높일 수 있는 선택을 우선시 하는 편이다.',
                  '나는 이익을 발생하는 것을 추구한다.',
                  '나는 성과가 발생하도록 우선적으로 노력한다.']],
    'Survey2': [['우리 조직은 성과중심의 가치를 추구한다.',
                 '우리 조직은 일을 할 때, 성취 결과를 중요시한다.',
                 '우리 조직은 높은 성과를 이루는 것을 선호한다.'],
                ['우리 조직은 인간관계중심의 가치를 추구한다.',
                 '우리 조직은 일을 할 때, 대인관계를 중요시한다.',
                 '우리 조직은 좋은 인간관계를 이루는 것을 선호한다.'],
                ['우리 조직은 위험이 발생할 경우 안전한 선택을 우선시하는 편이다.',
                 '우리 조직은 손해가 발생하는 것을 경계한다.',
                 '우리 조직은 피해가 발생하지 않도록 우선적으로 노력한다.'],
                ['우리 조직은 위험이 발생하더라도 이익을 높일 수 있는 선택을 우선시 하는 편이다.',
                 '우리 조직은 이익을 발생하는 것을 추구한다.',
                 '우리 조직은 성과가 발생하도록 우선적으로 노력한다.']],
    'Survey3': ['최고경영층 지원',
                '보안 규정(보상, 처벌 등)',
                '정보보안 목표 및 가치',
                '정보보안 시스템',
                '교육/훈련',
                '홍보 캠페인',
                '커뮤니케이션',
                '보안 문화',
                '위기 관리',
                '기술 지원(헬프데스크 등)'],
}
```

#### class Survey1

```python
class Survey1(tk.Frame):
    """
    화면 2-1을 구성하는 Frame class
    개인 특성 측정을 구현
    """
    def __init__(self, app):
        """
        frame 생성자
        각종 위젯들이 생성자에서 생성된다.
        :param app: 해당 frame을 호출한 Project 객체
        """
        # 크기/위치 설정 (가로*세로+x좌표+y좌료)
        
        # checkBox의 check여부를 저장하는 변수를 담는 list
        # 스크립트에서 설문1에 대한 내용을 받아옴
        # 각 설문요인을 담는 frame
        # 각각의 설문 내용을 담는 frame
        # 각 설문에 대한 checkbox를 담는 frame
        
        ### 설문에 대한 내용과 check박스를 화면에 배치하는 반복문 ###

    def check(self):
        """
        체크박스의 check여부를 판단하는 메소드
        중복여부도 판단하며 옳게 체크되어있다고 판단되면 CSV 파일에 해당 설문 내용을 저장함
        """
        # 파일을 읽어옴

        ### 생성했던 check박스들의 내용을 확인하면서 csv파일에 쓸 내용을 구성하는 반복문 ###
        # 이후 다음 설문문항으로 넘김(switch_frame)
```

self.checkvar는 아래와 같은 4x3x6 형태의 리스트
![1. checkvar](img\1. checkvar_1.jpg)

#### class Survey2

매커니즘은 Survey1와 동일

```python
class Survey2(tk.Frame):
    """
    화면 2-2을 구성하는 Frame class
    조직 특성 측정을 구현
    """
    def __init__(self, app):
        """
        frame 생성자
        각종 위젯들이 생성자에서 생성된다.
        :param app: 해당 frame을 호출한 Project 객체
        """
        # 크기/위치 설정 (가로*세로+x좌표+y좌료)
        
        # checkBox의 check여부를 저장하는 변수를 담는 list
        # 스크립트에서 설문2에 대한 내용을 받아옴
        # 각 설문요인을 담는 frame
        # 각각의 설문 내용을 담는 frame
        # 각 설문에 대한 checkbox를 담는 frame
        
        ### 설문에 대한 내용과 check박스를 화면에 배치하는 반복문 ###

    def check(self):
        """
        체크박스의 check여부를 판단하는 메소드
        중복여부도 판단하며 옳게 체크되어있다고 판단되면 CSV 파일에 해당 설문 내용을 저장함
        """
        # 파일을 읽어옴

        ### 생성했던 check박스들의 내용을 확인하면서 csv파일에 쓸 내용을 구성하는 반복문 ###
        # 이후 다음 설문문항으로 넘김(switch_frame)
```

#### class Survey3

매커니즘 자체는 Survey1,2와 동일 하지만, 위젯의 배치가 조금 다름

```python
class Survey3(tk.Frame):
    """
    화면 2-3을 구성하는 Frame class
    정보보안 수준 측정을 구현
    """
    def __init__(self, app):
        """
        frame 생성자
        각종 위젯들이 생성자에서 생성된다.
        :param app: 해당 frame을 호출한 Project 객체
        """
        # 크기/위치 설정 (가로*세로+x좌표+y좌료)

        # checkBox의 check여부를 저장하는 변수를 담는 list
        # 스크립트에서 설문3에 대한 내용을 받아옴
        # 각 설문요인을 담는 frame
        # 각각의 설문 내용을 담는 frame
        # 각 설문에 대한 checkbox를 담는 frame

        ### 설문에 대한 내용과 check박스를 화면에 배치하는 반복문 ###

    def check(self):
        """
        체크박스의 check여부를 판단하는 메소드
        중복여부도 판단하며 옳게 체크되어있다고 판단되면 CSV 파일에 해당 설문 내용을 저장함
        """
        # 파일을 읽어옴

        ### 생성했던 check박스들의 내용을 확인하면서 csv파일에 쓸 내용을 구성하는 반복문 ###
        # 이후 다음 설문문항으로 넘김(switch_frame)
```

Survey3의 self.checkvar는 10x2x5 형태의 리스트
![1. checkvar_2](img\1. checkvar_2.jpg)

### Result.py

#### Script

```python
"""
결과에 따른 스크립트를 각 경우 따라 맞게 dictionary형태로 구성함 
"""
SCRIPT = {
    "result1" : ["\'상\'은 조직과 조직원 간의 목표, 가치 등이 우수한 수준으로 일치한다는 의미입니다."+
                 "\n따라서, 우리 조직은 현재 추진하고 있는 조직 활동을 유지함으로써,"+
                 "\n조직원들이 조직의 방향을 이해하도록 돕는 것이 필요합니다.",
                 "\'중\'은 조직과 조직원 간의 목표, 가치 등이 양호한 수준에서 일치한다는 의미입니다."+
                 "\n따라서, 우리 조직은 현재 추진하고 있는 조직 활동에서 구성원의 가치를 이해하고"+
                 "\n지속적인 변화활동을 추진함으로써, 적합성을 추가 보완하는 것이 필요합니다.",
                 "\'하\'는 조직과 개인간의 목표, 가치 등의 일치성이 미흡한 수준임을 의미합니다."+
                 "\n따라서, 우리 조직은 구성원 들이 추구하는 가치, 목표 등을 검토하여,"+
                 "\n혁신적으로 조직문화를 개편함으로써, 일치성을 확보할 수 있도록 지원하는 것이 필요합니다. "
                 ],
    "result2": {"s1" : ["1. 최고경영층지원", "2. 보안규정(보상, 처벌 등)", "3. 정보보안 목표 및 가치", "4. 정보보안 시스템",
                        "5. 교육/훈련", "6. 홍보/캠페인", "7. 커뮤니케이션", "8. 보안문화", "9. 위기관리", "10. 기술지원(헬프데스크 등)"],
                "s2" : ["우리 회사 직원들이 고려하는 정보보안 활동은 다음과 같습니다.",
                        "첫째, 현수준 유지영역(A). 해당 영역은 정보보안 활동의 중요도는 낮으나, 만족도는 높은 영역으로서, "
                        +"\n{} 요인들의 \n지원을 유지하는 것이 필요합니다.",
                        "둘째, 유지/관리 지속영역(B). 해당 영역은 정보보안 활동의 중요도와 만족도를 높게 판단하는 영역으로서, "
                        +"\n{} 요인들의 \n높은 수준의 지원을 지속적으로 유지시키는 것이 필요합니다.",
                        "셋째, 만족도 제공영역(C). 해당 영역은 정보보안 활동의 중요돠 만족도 모두 낮은 영역으로서, "
                        +"\n{} 요인들의 \n지원에 대한 만족도를 개선할 수 있는 활동이 필요합니다.",
                        "넷째, 중점 개선영역(D). 해당 영역은 정보보안 활동의 중요도는 높으나, 만족도는 낮은 영역으로서,"
                        +"\n{} 요인들의 \n지원을 중점적으로 향상시키는 것이 필요합니다."]}
}

### 각 영역에 대한 Label 위치 ###
POINT = [(0.25,3.15, "A. 현수준 유지영역"), (3.9,4.5, "B. 유지/관리 지속영역"),
         (0.25,0.5, "C. 만족도 제공영역"), (4,0.5, "D. 중점 개선영역")]

### 각 영역의 범위(순서대로 A,B,C,D) ###
AREA = [([0, 0, 2.5, 2.5], [2.5, 5, 5, 2.5]), ([2.5, 2.5, 5, 5], [2.5, 5, 5, 2.5]),
        ([0, 0, 2.5, 2.5], [0, 2.5, 2.5, 0]), ([2.5, 2.5, 5, 5], [0, 2.5, 2.5, 0])]
```

#### class Result1

```python
class Result1(tk.Frame):
    """
    화면 3-1을 구성하는 Frame class
    적합도 산출 화면을 구현
    """
    def __init__(self, app):
        """
        frame 생성자
        각종 위젯들이 생성자에서 생성된다.
        :param app: 해당 frame을 호출한 Project 객체
        """
        # """설문 데이터 import""" #
        ind_att = pd.read_csv('individual_attribute.csv')
        cul_att = pd.read_csv('cultural_attribute.csv')

        self.ind_r = self.calc_mean(ind_att)
        self.cul_r = self.calc_mean(cul_att)

        self.result = self.calc_PO_fit(self.ind_r, self.cul_r)

        # """데이터 시각화""" #
        tk.Frame.__init__(self, app)
        self.app = app
        self.app.geometry("1150x500+420+200")

        # 설문 결과를 보여주는 Frame
        # 설문 결과에 대한 설명을 보여주는 Frame

        fig = self.draw(self.result)                			  # 적합도 산출 (시각화 데이터)결과를 fig변수에 대입
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)  # tk canvas에 대입 
        canvas.get_tk_widget().pack()                              # pack()을 통해 시각화

        # 구간(상중하)을 나누기 위한 리스트
        # 구간 리스트에 대한 Label
        # """pandas의 구간 나누는 cut() 메소드를 통해 구간을 나누고 데이터가 해당하는 구간을 슬라이싱""" #
        
        # """ 적합도에 대한 Text 출력 """ #
        
        # """ 각 구간에 따른 설명 TEXT 출력 """ #

    def calc_mean(self, data):
        """
        12개 문항을 3개씩 4개의 요인으로 나누고
        각 요인에 대한 설문 값의 평균을 구하는 함수
        :param data: pandas를 통해 추출한 설문 데이터 값
        :return: 각 요인에 대한 설문데이터 값의 평균(list)
        """

    def calc_PO_fit(self, ind, cul):
        """
        조직과 개인의 점수차이를 계산하는 메소드
        :param ind: 개인특성 측정값 평균 
        :param cul: 조직특성 측정값 평균
        :return:
            P0_sub : 각 요인별 점수 차이(제곱근)
            dict_r : 각 요인과 Score값이 매칭된 dict(제곱값)
            score  : 적합도 Score
        """

    def draw(self, data):
        """
        설문 데이터를 방사형데이터로 표현하는 Figure를 생성하는 메소드 
        :param data: self.calc_PO_fit()메소드의 return 값
        :return: 4개의 요인의 점수를 방사형으로 표현한 figure 객체
        """

    def next(self):
        """
        다음 화면으로 넘어가는 메소드(Result2)
        생성자에서 생성한 button이 해당 메소드를 command로 가진다.
        """
```

#### class Result2

```python
class Result2(tk.Frame):
    """
    화면 3-2를 구성하는 Frame class
    IPA(중요도-만족도) 산출화면을 구현
    """
    def __init__(self, app):
        """
        frame 생성자
        각종 위젯들이 생성자에서 생성된다.
        :param app: 해당 frame을 호출한 Project 객체
        """
        # """데이터 import""" #
        df = pd.read_csv("Information_Security_Level.csv")
        self.data, self.result = self.calc_mean_and_zip(df)
        self.factors = self.quaternary(self.data)

        # """데이터 시각화""" #
        self.idx = -1 # Script 출력의 번호를 저장하는 변수

        # 설문 결과를 보여주는 Frame
        # 설문 결과에 대한 설명을 보여주는 Frame

        fig = self.draw(self.data)                      # 산점도 데이터를 fig변수에 대입
        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame) # fig변수를 canvas에 대입
        self.canvas.get_tk_widget().grid(row=0, column=0)              # grid(0,0)를 통해 시각화

        self.display_script()                           # 각 구간(A,B,C,D)에 대한 설명 Text 출력 메소드 
            
        # """ 각 구간 설명을 강조하는 Button 생성 및 출력 """ #

    def calc_mean_and_zip(self, data):
        """
        Infomation_Security_Level.csv 파일에서 값을 가져온 뒤, 각각의 열에 대한 평균을 구하고
        산점도로 표현하기 위한 전처리 메소드
        :param data: "Infomation_Security_Level.csv"에서 가져온 DataFrame
        :return:
            data : 산점도 X(중요도), Y(만족도) 좌표 값
            result : console창에 출력하기위한 DataFrame
        """

    def quaternary(self, data):
        """
        중요도,만족도 산점도의 좌표가 어느 영역인지(A,B,C,D) 판별하는 메소드
        :param data: calc_mean_and_zip() 메소드의 return값중에서 "data"
        :return: 각 영역에 대한 요인과 그 요인의 산점도 좌표를 dict형태로 반환
        """

    def draw(self, data):
        """
        전처리가 끝난 데이터를 통해 시각화하는 메소드
        각 영역별로 확인 할 수 있도록 if-else문을 통해 fig를 갱신하는 plot updating 알고리즘으로 구현
        :param data: calc_mean_and_zip()메소드 반환값 중에 "data"
        :return: 시각화 데이터를 가지고 있는 figure 객체
        """

    def display_script(self):
        """
        각 구간(A,B,C,D)에 대한 설명 Text 출력 메소드
        """

    def on_next(self):
        """
        각 영역에 대해 하이라이트되어 볼 수 있도록 하는 메소드(다음 버튼)
        선택된 영역의 요인들만 강조되어 출력된다.
        """

    def on_previous(self):
        """
        각 영역에 대해 하이라이트되어 볼 수 있도록 하는 메소드(이전 버튼)
        선택된 영역의 요인들만 강조되어 출력된다.
        """

    def on_return(self):
        """
        처음 화면으로 넘어가는 메소드(Main_Frame)
        생성자에서 생성한 button이 해당 메소드를 command로 가진다.
        """
```

## 실행화면

#### 화면 1

![3. screen1](img\3. screen1.PNG)

#### 화면 2

![3. screen2-1](img\3. screen2-1.PNG)

![3. screen2-2](img\3. screen2-2.PNG)

![3. screen2-3](img\3. screen2-3.PNG)

#### 화면 3

![3. screen3-1](img\3. screen3-1.PNG)

![3. screen3-2-1](img\3. screen3-2-1.PNG)

![3. screen3-2-2](img\3. screen3-2-2.PNG)

![3. screen3-2-3](img\3. screen3-2-3.PNG)
