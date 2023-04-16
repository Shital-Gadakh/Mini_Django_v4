



















for database
 python manage.py  shell                                                  
from jobs.models import Portal
 portal1 = Portal(name="naukri.com", description="famaouse job website")
portal1.save()


New terminal
 sqlite3 db.sqlite3
.tables
 select * from job_portal
1.600
==>show new database added