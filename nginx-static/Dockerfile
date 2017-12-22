FROM nginx:alpine

RUN rm /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/conf.d/

RUN rm /usr/share/nginx/html/*
COPY . /usr/share/nginx/html/
