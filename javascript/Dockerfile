FROM node:14-slim

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm ci

COPY . .

EXPOSE 8080

CMD [ "node", "index.js" ]