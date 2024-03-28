# Use Alpine Linux as the base image
FROM alpine:latest

# Install Nginx
RUN apk update && \
    apk add --no-cache nginx

# Copy Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Command to start Nginx
CMD ["nginx", "-g", "daemon off;"]
