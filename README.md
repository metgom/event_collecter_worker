# event_collect_worker

> Python 3.9 환경에서 작성되었습니다.

AWS Lambda에서 작동하는 함수입니다.  
SQLAlchemy 라이브러리를 사용하여 ORM 방식으로 쿼리를 생성하여 RDS에 전달하는 기능을 담당합니다.  
SQS에서 메시지가 수신되면 트리거를 통해 Lambda 함수를 실행하여 RDS에 데이터를 전송합니다.  

![image](https://user-images.githubusercontent.com/39260975/198231796-4f3f8ac0-22c2-4c2b-934e-9b84535bce76.png)
