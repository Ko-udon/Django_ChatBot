# CHAT PLAYING


오르미 미니프로젝트2 - chatGPT활용 채팅 서비스 



## 1. 목표와 기능

### 1.1 목표
- Django DRF를 이용하여 서버를 구현하기
- 마이크로서비스 아키텍처로 개발하기
- 로그인/로그아웃을 JWT토큰을 이용해 처리하기
- OpenAI의 GPT-3.5 모델을 이용하여 서버에서 응답을 처리해서 전달하기
- [ChatGPT영어 상황극 채팅 서비스 만들기 - 이진석 강사님](https://www.inflearn.com/course/chatgpt-%EC%98%81%EC%96%B4-%EC%B1%84%ED%8C%85%EC%84%9C%EB%B9%84%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0?inst=4f76c676&utm_source=instructor&utm_medium=referral&utm_campaign=inflearn_%ED%8A%B8%EB%9E%98%ED%94%BD_promotion-link)- 유사한 서비스로 구현


### 1.2 기능
- 사이트 회원가입/로그인/로그아웃
- 채팅방 생성하기
	- 채팅방은 사용언어(한국어, 영어, 일본어), 상황, 역할을 정해서 생성
 	- 채팅방은 수정 가능
  	- 생성한 채팅방은 삭제 가능 	 
- 챗봇과 채팅하기
	- 생성한 채팅방은 로그인한 유저가 본인의 채팅방만 조회 가능
 	- 채팅방에 입장 후, 텍스트 입력 시 GPT의 답변이 전달되고 채팅방에 메세지로 표기 	

### 1.3 팀 구성
<table>
	<tr>
		<th>고동우</th>
	</tr>
</table>

## 2. 개발 환경 및 배포 URL
### 2.1 개발 환경
- Web Framework
  - Django 4.0.3 (Python 3.11.6)
- 서비스 배포 환경
  - BackEnd: Amazon Lightsail 
  - FrontEnd: Amazon Lightsail 
### 2.2 배포 URL
- http://15.164.74.72/

### 2.3 URL 구조
- accounts

| App       | URL                                        | Views Function    | HTML File Name      | 요청            | Note           |
|-----------|--------------------------------------------|-------------------|---------------------|----------------|----------------|
| accounts      | 'account/signup/'                              | signUpView        | register.html       |Post            | 회원가입       |
| accounts      | 'account/auth/'                                | UserAuthAPIView   | login.html          |Post            | 로그인         |
| accounts      | 'account/auth/'                                | UserAuthAPIView   | -          |Get             | 유저확인       |
| accounts      | 'account/auth/'                                | UserAuthAPIView   | -          |Delete          | 로그아웃       |

- chat
  
| App       | URL                                        | Views Function    | HTML File Name      | 요청            | Note           |
|-----------|--------------------------------------------|-------------------|---------------------|----------------|----------------|
| chat      | 'chat/'                                | RolePlayingRoomAPIView         | chat_list.html  | Get     | 채팅방 조회    |
| chat      | 'chat/create/'                         | CreateRolePlayingRoomAPIView   | create_chat.html | Post   | 채팅방 생성    |
| chat      | 'chat/<int:pk>/'                       | DetailRolePlayingRoomAPIView   | chat_activate.html   | Get | 채팅방 입장    |
| chat      | 'chat/<int:pk>/activate/'              | chatGPT                        | chat_activate.html  | Post | GPT 메세지 요청 |
| chat      | 'chat/<int:pk>/update/'                | UpdateRolePlayingRoomAPIView   | update_chat.html  | Post   | 채팅방 수정    |
| chat      | 'chat/<int:pk>/delete/'                | DeleteRolePlayingRoomAPIView   | chat_list.html  | Delete   | 채팅방 삭제    |




## 3. 요구사항 명세와 기능 명세

![image](https://github.com/Ko-udon/Django_ChatBot/assets/79897135/07e4cc4e-691b-4e9d-a4d5-0f9de81060d5)



## 4. 프로젝트 구조와 개발 일정
### 4.1 프로젝트 구조
```
📦project
 ┣ 📂backEnd
 ┃ ┣ 📂accounts
 ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┣ 📜managers.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜serializers.py
 ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂chat
 ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┣ 📜forms.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜serializers.py
 ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂chatProject
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜asgi.py
 ┃ ┃ ┣ 📜settings.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜wsgi.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂venv
 ┃ ┣ 📜.env
 ┃ ┣ 📜db.sqlite3
 ┃ ┣ 📜manage.py
 ┃ ┗ 📜requirements.txt
 ┗ 📂frontEnd
 ┃ ┣ 📂css
 ┃ ┣ 📂img
 ┃ ┣ 📂js
 ┃ ┣ 📜chat_activate.html
 ┃ ┣ 📜chat_list.html
 ┃ ┣ 📜create_chat.html
 ┃ ┣ 📜index.html
 ┃ ┣ 📜login.html
 ┃ ┣ 📜PlayGrounds.html
 ┃ ┣ 📜register.html
 ┃ ┗ 📜update_chat.html
```

### 4.1 개발 일정(WBS)

``` mermaid
gantt
    title Django_ChatBot
    dateFormat YY-MM-DD
    section 기획
        리포지토리 생성 :2023-11-21, 1d
        요구사항 분석 :2023-11-21, 1d
        oven 목업 제작 :2023-11-21, 1d
        발표자료 제작 : 2023-11-29, 2d
    section FE
	HTML/CSS 페이지 구현 :2023-11-21, 2d
	페이지 연동 :2023-11-26, 4d
	BE 연결 및 배포 :2023-11-29, 1d
    section BE
	JWT토큰 테스트 :2023-11-22, 1d
	회원가입/로그인/로그아웃 :2023-11-22, 2d
	채팅방 생성 :2023-11-24, 1d
	채팅방 삭제 :2023-11-26, 1d
	채팅방 수정 :2023-11-25, 2d
	gpt와 채팅 :2023-11-28, 2d
	FE 연결 및 배포 :2023-11-29, 1d
    section 발표자료 제작

```

## 5. 역할 분담
- FE/BE : 고동우

## 6. 와이어프레임 / UI / BM

### 6.1 와이어프레임

https://ovenapp.io/view/qLV1Sb2auwmPikx0rBvP7I9le9V22ByD/

<table>
    <tbody>
        <tr>
            <td>메인</td>
            <td>로그인</td>
        </tr>
        <tr>
            <td>
		<img src="readme_resource/wf/wf-main.png" width="100%">
            </td>
            <td>
                <img src="readme_resource/wf/wf-login.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>채팅방 수정</td>
            <td>채팅방 목록</td>
        </tr>
        <tr>
            <td>
                <img src="readme_resource/wf/wf-chat_create.png" width="100%">
            </td>
            <td>
                <img src="readme_resource/wf/wf-chat_list.png" width="100%">
            </td>
        </tr>
        <tr>
            <td>채팅 활성화</td>
        </tr>
        <tr>
            <td>
                <img src="readme_resource/wf/wf-chat_activate.png" width="100%">
            </td>
        </tr>
    </tbody>
</table>

### 6.2 화면 설계
- 화면은 gif파일로 업로드해주세요.
 
<table>
    <tbody>
        <tr>
            <td>메인</td>
            <td>로그인</td>
        </tr>
        <tr>
            <td>
		<img src="readme_resource/gif-main.gif" >
            </td>
            <td>
                <img src="readme_resource/monitor/gif-login.gif" >
            </td>
        </tr>
        <tr>
            <td>채팅방 생성</td>
            <td>채팅방 수정</td>
        </tr>
        <tr>
            <td>
                <img src="readme_resource/monitor/gif-create_chat.gif" width="100%">
            </td>
            <td>
                <img src="readme_resource/monitor/gif-update_chat.gif" width="100%">
            </td>
        </tr>
        <tr>
            <td>채팅방 삭제</td>
            <td>채팅 활성화</td>
        </tr>
        <tr>
            <td>
                <img src="readme_resource/monitor/gif-delete_chat.gif" width="100%">
            </td>
            <td>
                <img src="readme_resource/monitor/gif-chat_activate.gif" width="100%">
            </td>
        </tr>
    </tbody>
</table>


## 7. 데이터베이스 모델링(ERD)
![image](https://github.com/Ko-udon/Django_ChatBot/assets/79897135/c72096d8-5981-4698-b1bd-ffc14991dc43)


## 8. Architecture
![image](https://github.com/Ko-udon/Django_ChatBot/assets/79897135/6b59183b-1723-4a68-8d14-c572fdc60286)



## 9. 메인 기능
1. 회원가입 및 로그인
   - 회원가입 요청 -> 사용자 정보 등록
   - 로그인 -> JWT 토큰(access token)을 웹 페이지 Cookie에 저장
   - 사용자 정보 조회 -> cookie에 access token으로 접속한 사용자 정보 조회
2. 채팅방 생성/조회/수정/삭제
   - 언어, 상황, 역할을 지정하여 채팅방 생성 -> 챗봇 기본 설정으로 입력됨
   - 토큰을 통해 사용자 정보를 확인하여 본인이 생성한 채팅방만 조회
   - 채팅방 수정 가능
   - 채팅방 삭제 가능
3. 채팅 / 채팅 기록 저장
   - 챗봇에 메세지 전송 -> 서버에서 해당 채팅방의 설정에 맞춰 chatGPT에 메세지 전송 -> 응답온 메세지를 프론트에 전달 -> 프론트에서 응답 처리
   - 해당 채팅방에서 대화했던 내용은 저장하여 페이지를 벗어나고 다시 접속해도 유지됨

<table>
    <tbody>
        <tr>
            <td>
		<img src="readme_resource/gif-save_chat.gif" width="100%">
            </td>
        </tr>
    </tbody>
</table>


## 10. 문제 및 에러 해결

1. JS array객체인줄 알았는데 아니여서 값을 조회 못했던 점
- 채팅방 데이터 조회 시 데이터 응답 형태가 일반 배열(array)라고 생각
- 관련 에러를 찾아보니 유사 배열 객체로 반복 가능한 객체를 복사해 새로운 Array 객체로 반환하여 해결
![image](https://github.com/Ko-udon/Django_ChatBot/assets/79897135/da8fdbc5-535f-4a14-b465-0f7fdad96ae2)

<table>
    <tbody>
        <tr>
            <td>기존 코드</td>
            <td>수정 후</td>
        </tr>
        <tr>
            <td>
                <img src="readme_resource/ts/before_1.png" width="100%">
            </td>
            <td>
                <img src="readme_resource/ts/sol_1.png" width="100%">
            </td>
        </tr>
    </tbody>
</table>

2. 채팅 데이터 저장 방식
- 채팅방에 메세지를 어떤식으로 저장할지 고민이 많았다
- 좋은 방법이 생각나지 않아 메세지를 저장시, <tap>(user or system)텍스트를 앞에 붙여서 전달하여 데이터를 split('<tap>')으로 나눠서 구분하여 저장

<table>
    <tbody>
        <tr>
            <td>저장 방식</td>
            <td>메세지 전달</td>
        </tr>
        <tr>
            <td>
                <img src="readme_resource/ts/before_2.png" width="100%">
            </td>
            <td>
                <img src="readme_resource/ts/sol_2.png" width="100%">
            </td>
        </tr>
    </tbody>
</table>

3.채팅방 조회 및 전달 
- 채팅방 입장을 위해 채팅방의 id값이 필요
<table>
    <tbody>
        <tr>
            <td>코드</td>
        </tr>
        <tr>
            <td>
                <img src="readme_resource/ts/before_3.png" width="100%">
            </td>
        </tr>
    </tbody>
</table>

```
'<td>'+'<a class="enter_btn" href='+"chat_activate.html?id="+item['pk']+'>'+'입장'+'</td>'
```

- 위 스크립트에서 `chat_activate.html?id="+item['pk']`으로 pk값을 url로 같이 전달
  
url에 id값을 넣어 다음 페이지로 이동하고, 해당 페이지에서 요청하여 해결



4.API 키값을 포함한 .env파일
- 깃허브에 키값을 포함한 .env파일같은 경우 올릴수 없다
- lighsail linux OS에서 git 프로젝트를 clone
- .env 파일은 구글 드라이브에 공유 링크를 생성 후, 아래 코드로 해결
  
```
wget --load-cookies ~/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies ~/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=[아이디]' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=[아이디]" -O [파일 이름] && rm -rf ~/cookies.txt
```

___

