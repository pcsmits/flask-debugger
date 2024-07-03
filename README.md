docker build -t demo-pg-app .
docker run -it -p 8080:8080 -e PGUSER= -e PGPASS= -e PGDATABASE=postgres -e PGHOST demo-pg-app
