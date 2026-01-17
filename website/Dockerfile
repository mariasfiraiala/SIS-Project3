FROM node:20-alpine

RUN ["npx", "create-next-app@15.0.3", "--example", "https://github.com/vercel/next.js/tree/d45fc5ad95eeee2218f29c0bfbf1310189ab7781/examples/blog-starter", "app"]

WORKDIR /app

EXPOSE 3000
ENV NEXT_FONT_GOOGLE_DOWNLOAD=false

RUN ["npm", "run", "build"]

CMD ["npm", "start"]
