select_id = """SELECT id FROM table_001_request_response"""
select_request = """SELECT api_http_request FROM table_001_request_response WHERE id = %s"""
select_response = """SELECT api_http_response FROM table_001_request_response where id = %s"""
insert_request = """INSERT INTO table_001_request_response (id, api_http_request, api_http_response, 
api_http_request_send_time, api_http_response_waiting_time, user_id_id) VALUES (%s, %s, %s, %s, %s, %s)"""