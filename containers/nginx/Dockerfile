# Nginxのイメージを指定
FROM nginx

RUN rm -f /etc/nginx/conf.d/*
COPY ./containers/nginx/nginx.conf /etc/nginx/conf.d/

CMD /usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf