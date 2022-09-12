from utils.db import Database
import pprint


if __name__=="__main__" :
    db = Database()
    db.execute("DROP TABLE IF EXISTS history")
    db.execute("DROP TABLE IF EXISTS ticket")
    db.execute("DROP TABLE IF EXISTS student")
    db.execute("DROP TABLE IF EXISTS department_service_personnel")
    db.execute("DROP TABLE IF EXISTS personnel")
    db.execute("DROP TABLE IF EXISTS department_service")
    db.execute("DROP TABLE IF EXISTS department")
    db.execute("DROP TABLE IF EXISTS service")
    db.execute("DROP TYPE IF EXISTS messtype")
    db.execute('''CREATE TABLE department (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL) ''')
    db.execute('''CREATE TABLE service (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL) ''')
    db.execute('''CREATE TABLE department_service (
        id SERIAL PRIMARY KEY,
        department INTEGER NOT NULL,
        service INTEGER NOT NULL,
        access_level INTEGER NOT NULL,
        CONSTRAINT fk_department
            FOREIGN KEY(department)
                 REFERENCES department(id),
        CONSTRAINT fk_service
            FOREIGN KEY(service)
                REFERENCES service(id) ) ''')
    db.execute('''CREATE TABLE personnel (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        contact VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL) ''')
    db.execute('''CREATE TABLE department_service_personnel (
        id SERIAL PRIMARY KEY,
        department_service INTEGER NOT NULL,
        personnel INTEGER NOT NULL,
        CONSTRAINT fk_department_service
            FOREIGN KEY(department_service)
                REFERENCES department_service(id),
        CONSTRAINT fk_personnel
            FOREIGN KEY(personnel)
                REFERENCES personnel(id) ) ''')
    db.execute('''CREATE TYPE messtype AS ENUM ('non-veg', 'veg', 'special','food_park')''' )
    db.execute('''CREATE TABLE student (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        regno VARCHAR(255) NOT NULL,
        contact VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        hosteller BOOLEAN NOT NULL,
        room INTEGER NOT NULL,
        mess messtype NOT NULL,
        bus INTEGER NOT NULL) ''')
    db.execute('''CREATE TABLE ticket (
        id SERIAL PRIMARY KEY,
        student INTEGER NOT NULL,
        complaint TEXT NOT NULL,
        department_service_personnel INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        resolved BOOLEAN NOT NULL,
        CONSTRAINT fk_student
            FOREIGN KEY(student)
                REFERENCES student(id),
        CONSTRAINT fk_department_service_personnel
            FOREIGN KEY(department_service_personnel)
                REFERENCES department_service_personnel(id) ) ''')
    db.execute('''CREATE TABLE history (
        id SERIAL PRIMARY KEY,
        ticket INTEGER NOT NULL,
        log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        department_service_personnel INTEGER NOT NULL,
        resolved BOOLEAN NOT NULL,
        remarks VARCHAR(255) NOT NULL,
        CONSTRAINT fk_ticket
            FOREIGN KEY(ticket)
                REFERENCES ticket(id),
        CONSTRAINT fk_department_service_personnel
            FOREIGN KEY(department_service_personnel)
                REFERENCES department_service_personnel(id) ) ''')
