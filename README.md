

##PROCESSOS PARA UPLOAD DE API FLASK NO EC2 AWS##

- Acesso via ssh da sua instância EC2

- Git clone (url projeto)

- Criar ambiente virtual do projeto e instalar as dependências

- sudo nano /etc/systemd/system/flaskapp.service:

        [Unit]
        Description=Gunicorn instance for a simple hello world app
        After=network.target

        [Service]
        User=ubuntu
        Group=www-data
        WorkingDirectory=/home/ubuntu/api-teste-flask/app
        ExecStart=/home/ubuntu/api-teste-flask/venv/bin/gunicorn -b localhost:8000 main:app
        Restart=always

        [Install]
        WantedBy=multi-user.target

- sudo systemctl daemon-reload
- sudo systemctl start flaskapp
- sudo systemctl enable flaskapp
- sudo systemctl status flaskapp – aparece resultado no terminal:
- Exemplo:

        flaskapp.service - Gunicorn instance for a simple hello world app
            Loaded: loaded (/etc/systemd/system/flaskapp.service; enabled; vendor pres>
            Active: active (running) since Wed 2024-03-13 21:21:19 UTC; 4s ago
        Main PID: 13608 (gunicorn)
            Tasks: 2 (limit: 1121)
            Memory: 43.8M
                CPU: 442ms
            CGroup: /system.slice/flaskapp.service
                    ├─13608 /home/ubuntu/api-teste-flask/venv/bin/python3 /home/ubuntu>
                    └─13609 /home/ubuntu/api-teste-flask/venv/bin/python3 /home/ubuntu>

        Mar 13 21:21:19 ip-172-31-24-149 systemd[1]: Started Gunicorn instance for a si>
        Mar 13 21:21:19 ip-172-31-24-149 gunicorn[13608]: [2024-03-13 21:21:19 +0000] [>
        Mar 13 21:21:19 ip-172-31-24-149 gunicorn[13608]: [2024-03-13 21:21:19 +0000] [>
        Mar 13 21:21:19 ip-172-31-24-149 gunicorn[13608]: [2024-03-13 21:21:19 +0000] [>
        Mar 13 21:21:19 ip-172-31-24-149 gunicorn[13609]: [2024-03-13 21:21:19 +0000] [>

- Teste para ver se está ok
curl localhost:8000

- sudo apt-get install nginx
- sudo systemctl start nginx
- sudo systemctl enable nginx
- sudo nano /etc/nginx/sites-available/default   (edicao do arquivo)


- Adicionar no arquivo antes de server:

        upstream flaskapp {
                server 127.0.0.1:8000;
        }

- trocar location:

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                proxy_pass http://flaskapp;
        }

- salvar.

- sudo systemctl restart nginx