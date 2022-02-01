CREATE DATABASE IF NOT EXISTS ipro_db;
USE ipro_db;
DROP TABLE processes;

CREATE TABLE processes(
    ID INT NOT NULL AUTO_INCREMENT,
    PROCESS_ID INT NOT NULL,
    FILE_PATH TEXT,
    MEM_USAGE INT,
    CPU_USAGE INT,
    SESSION_NAME TEXT,
    OPEN_FILES TEXT,
    PROCESS_NAME TEXT,
    TIME_STAMP TEXT,
    UIDS INT,
    USERNAME TEXT,
    PRIMARY KEY (ID)
);

INSERT INTO processes (PROCESS_ID, FILE_PATH, MEM_USAGE, CPU_USAGE, SESSION_NAME, OPEN_FILES, PROCESS_NAME, TIME_STAMP, UIDS, USERNAME) VALUES(
	-- example data, later will need to get data from front-end
    500,
    "C:/Windows/System32/virus.exe",
    75,
    50,
    "virus.exe",
    "C:/Users/Brody/Desktop/secret_information.txt, C:/Users/Administrator/Desktop/enterprise_login_information.txt",
    "virus.exe",
    "07:40:39 1/31/2022",
    3,
    "administrator"
);

SELECT * FROM processes;
