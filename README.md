# igaworks_event_collect_worker

AWS Lambda에서 작동하는 Event Collect Worker 입니다.  
SQS의 이벤트 수신 트리거를 통해 작동합니다.  
SQLAlchemy 라이브러리를 사용하여 ORM 방식으로 RDS에 데이터를 전송합니다.  
