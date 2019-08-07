FROM node:latest
EXPOSE 8080
RUN mkdir /frontend
WORKDIR /frontend
RUN npm i -g npm@3.10.10
RUN npm install -i
# Hopefully you'd never actually do this, just copy everything, including locally installed node_modules
CMD npm run serve