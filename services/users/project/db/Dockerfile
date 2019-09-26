#Base image
FROM postgres:10.4-alpine

#run create SQL on init
ADD create.sql /docker-entrypoint-initdb.d
