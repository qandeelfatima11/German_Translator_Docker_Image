FROM node:18

WORKDIR /app

COPY package.json .

RUN npm yarn

COPY . .

CMD ["npm", "start"]

