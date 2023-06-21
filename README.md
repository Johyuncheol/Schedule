### ●프로젝트명:  Team scheudle(가제)



<br/> <br/> 
### ●프로젝트 소개

<br/> 
캠프 남은 기간 동안 여러 번의 팀 프로젝트를 계속 진행 할텐데

서로 할 일들과 진행 상황을 공유하면서 할 일 -진행 중-완료 루트로 시각적으로

한눈에 알아 보기 편한 서비스가 있으면 좋겠다는 생각이 들었고

그러면 '직접 만들어서 사용해보자!' 라는 마음에서 시작했습니다.




<br/> <br/> 
### ●와이어 프레임



<br/> <br/> 
### ●API
<br/> 

|기능|method|URL|request|response|
|---|---|---|---|---|
|할 일 추가|	              |POST|	          |/add|	        |input태그의 id값을 통해 value 전송|	              |'todo': todo_receive, 'location': 0|
|할 일 (앞으로 진행)|	     |POST|	           |/move|	       |클릭된 버튼의 밸류값|	|받은데이터[location]+1|      |저장 상황에 맞는 메시지|
|할 일 (뒤로 진행)|	        |POST|	          |/move_cancel|	|클릭된 버튼의 밸류값|	|받은데이터[location]-1저장|   |상황에 맞는 메시지|
|리스트 출력 (할 일)|	     |GET|	           |/todo|	       |/todo|	                                          |'location':0  데이터의 리스트|
|리스트 출력 (진행중)|	    |GET|	            |/running|	    |/running|	                                       |'location':1  데이터의 리스트|
|리스트 출력 (완료)|	       |GET|	           |/done|	       |/done|	                                          |'location':2  데이터의 리스트|

 
