# Final project for 2023's 219114/115 Programming I
database.py
  - in the database i've created def insert and update to make it easier when you want to use the function

project_manage.py
  - in this part I'm gonna tell you how to run the program to create the project
  - first you have to enter username and password of the student who wants to create a project
  - when you've done the program gonna show you three ways
  - if you a want to create a project enter 1
  - then the program gonna change your role from student to lead
  - and the program gonna ask you want to continue or exit
  - enter exit to make the program done
  - then login again with the same student but the program gonna change output
    - because your role has been changed from student to lead
  - then program will ask you to invite studen/faculty or update the status
  - if you enter invite(member<=2,faculty<=1)
    - the program will show you student table and ask you to enter the ID
      - the program will send the invite to the student you entered the ID
      - then you exit the program and login the student you just send the invite
      - then you should enter 3 to accept or deny the invite
      - then done
    - to invite the faculty is same as student process
    - if you login the faculty you can check the student project before send to the evaluator
    - if you login the admin you can fix everything in the table and you can give new role to faculty to be evaluator
  done

  persons.csv
    -this file you can check the type of the student
