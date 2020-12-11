FROM node:12.18.1
ENV NODE_ENV=production

WORKDIR /app/JsTest

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install

COPY . .

EXPOSE 8080

CMD node -r ./tracing index.js