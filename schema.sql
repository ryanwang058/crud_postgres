-- create table
DROP TABLE IF EXISTS students;
create table students (
  student_id serial primary key,
  first_name varchar(20) not null,
  last_name varchar(20) not null,
  email varchar(50) not null unique,
  enrollment_date date
);

-- initalize data
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');