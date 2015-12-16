"""
Masuk ke admnistrator {default user untuk administrator adalah postgres}
===============================================
sudo -u postgres psql
===============================================

Lihat user yang ada
===============================================
\du
===============================================

Membuat User
===============================================
CREATE USER iniuser;
ALTER USER iniuser WITH PASSWORD 'inipass';
===============================================

Ubah previllage menjadi superuser
===============================================
Alter role <username> superuser;
Ex: Alter role iniuser superuser;
===============================================

Ubah previllage menjadi readonly
===============================================
GRANT USAGE ON SCHEMA public to iniuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO iniuser;

-- repeat code below for each database:

GRANT CONNECT ON DATABASE foo to iniuser;
\c foo
GRANT USAGE ON SCHEMA public to iniuser; 
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO iniuser;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO iniuser;
===============================================
"""