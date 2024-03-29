CREATE DATABASE IF NOT EXISTS ipro_db;
USE ipro_db;
DROP TABLE processes;

CREATE TABLE processes (
  ID int NOT NULL AUTO_INCREMENT,
  TIME text,
  MACHINE_ID text,
  PROCESS_NAME text,
  MEMORY_UTILIZATION TEXT,
  CPU_UTILIZATION TEXT,
  MEMORY_USED text,
  THREADS int DEFAULT NULL,
  USER text,
  PATH text,
  PID int DEFAULT NULL,
  PRIMARY KEY (ID)
);


--example data
INSERT INTO processes (TIME, MACHINE_ID, PROCESS_NAME, MEMORY_UTILIZATION, CPU_UTILIZATION, MEMORY_USED, THREADS, USER, PATH, PID) VALUES (
    "2022-02-14 21:02:50.061406",
    "66351924125566",
    "System",
    "0.0018126485636964706",
    "25.7",
    "0.151552 MB",
    234, 
    "SYSTEM", 
    "C:\Windows\System32\smss.exe", 
    520);

SELECT * FROM processes;
