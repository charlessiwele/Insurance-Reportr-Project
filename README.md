# INITIAL SETUP INSTRUCTIONS
- Create a venv instance inside "Insurance Reportr Project" parent folder
- Activate venv

# SETUP IN WINDOWS
✅ Navigate to "Setup/Windows" folder
✅ Run bat "pip install requirements"
✅ Run bat "makemigrations"
✅ Run bat "migrate"
✅ Run bat "populateconfigdata"
✅ Run bat "generatesuperuser"
✅ Look inside "reportr/user_credentials/super_users" directory for newly generated superuser for logins
✅ Run bat "runtests" to run unit tests 
✅ Run bat "runserver" to start the test/local server

# SETUP IN LINUX
✅ Activate virtual environment
✅ Run "python pip install -r requirements.txt" to install dependent libraries from requirements.txt
✅ Navigate to Insurance Reportr Project/reportr (presumably this is where your "manage.py" will be)
✅ Run python manage.py makemigrations
✅ Run python manage.py migrate
✅ Run python manage.py to configure some custom default config: "python manage.py populateconfigdata"
✅ Run "python manage.py generatesuperuser" to generate a default super user to access the admin panel
✅ Look inside "reportr/user_credentials/super_users" directory for newly generated superuser for logins
✅ Run unit tests "python manage.py test"
✅ Run "python manage.py runserver 127.0.0.1:8000" to start the test/local server
 

# GENERAL USAGE INSTRUCTIONS
- Confirm you have the server up running (python manage.py runserver 127.0.0.1:8000), 
- Open browser and navigate to http://127.0.0.1:8000/admin
- In the django admin panel login, you can login using the user and password generated in "generatesuperuser"
- Navigate to PaymentDocument model
- Add new model instance/record and attach the test file (Insurance Reportr Project\Test Files\2018_12_11_payments.csv) to the file field
- Select option to "Save and continue editing"
- Top right hand corner select "Sync Document Payments" this will populate the Payments table/model
- Navigate to the "Payment" model to see all the new records added
- Navigate to "Report" model
- Select to add new Report instance. note: Report name will already be populated
- Select the previously added PaymentDocument instance in the payments_document field
- Select a report_type option from the drop-down "report_type" field
- Save and continue editing
- In the top right hand corner, select the "Generate Reports" button. 
  -- This will generate reports based on the "report_type" option selected
- Refresh current "Report" page
- Reports will be generated and listed below the standard Report fields.
- Select the file link on any of the generated files to download and view the file contents
