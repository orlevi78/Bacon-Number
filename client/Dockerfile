# First stage is to build the app.
# Meaning to compile it into .js .css .html
FROM node:alpine AS builder
WORKDIR /client
COPY . .
RUN npm install
RUN npm run build

# Second stage is to create the server running from these files.
FROM nginx:alpine AS runner

# Now I want to copy the files not from my computer(which is default) but rather from the container I just created.
COPY --from=builder /client/dist /usr/share/nginx/html