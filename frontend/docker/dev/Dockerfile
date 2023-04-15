# Stage 1: Build frontend code
FROM node:19-alpine as build

ARG APP_DIR=/app
WORKDIR ${APP_DIR}

COPY package*.json ./

RUN apk add --no-cache make gcc g++ python3 && \
    npm ci && \
    npm cache clean --force && \
    apk del make gcc g++ python3

COPY . .

CMD ["npm", "run", "start"]
