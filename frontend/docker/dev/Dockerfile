# Stage 1: Build frontend code
FROM node:19-alpine as build

ARG APP_DIR=/app
WORKDIR ${APP_DIR}

COPY package*.json ./

RUN npm ci && \
    npm cache clean --force

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
