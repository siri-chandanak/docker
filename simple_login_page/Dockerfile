FROM ubuntu:25.10

RUN apt update

RUN apt install apache2 -y

WORKDIR /var/www/html

COPY index.html /var/www/html/index.html

COPY style.css /var/www/html/style.css

RUN chmod 644 /var/www/html/index.html
RUN chmod 644 /var/www/html/style.css

EXPOSE 5000

CMD ["apache2ctl", "-D", "FOREGROUND"]