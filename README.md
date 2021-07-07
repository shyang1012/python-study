# python-study
파이썬 기초를 공부하기 위한 프로젝트
교재: Do it! 점프 투 파이썬(https://book.naver.com/bookdb/book_detail.nhn?bid=15052904)
## 공부내용
* 파이썬 기본 문법
* 자료형공부
* 유투브 강의를 참고한 로또 회차별 당첨번호
*  flask를 활용한 게시판 구현
*  정규식

## 로또 프로그램 배포파일 만드는 방법
* pyinstaller를 먼저 설치한다.
```
    pip install pyinstaller
```
* pyinstaller를 활용하여 실행파일을 만드는 방법은 다음과 같다.
```
    (chapter3_do_it) C:\dev\devApps\chapter3_do_it>pyinstaller --onefile --noconsole lottery.py
    --onefile: 이 옵션을 주게 되면 하나의 파일로 묶어준다.
    --noconsole: 이 옵션이 없으면 프로그램이 실행될 때 콘솔이 실행된다.
```
    