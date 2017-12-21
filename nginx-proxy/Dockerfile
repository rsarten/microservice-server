FROM nginx:alpine

RUN rm /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/conf.d/

RUN rm /usr/share/nginx/html/*
COPY index.html /usr/share/nginx/html/
COPY networking-538.png /usr/share/nginx/html/
