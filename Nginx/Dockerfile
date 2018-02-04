FROM nginx:1.13.7-alpine

RUN rm /etc/nginx/nginx.conf

COPY ./Nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./static/index.html /usr/share/nginx/html/index.html
COPY ./static/dist /usr/share/nginx/html/dist

EXPOSE 80