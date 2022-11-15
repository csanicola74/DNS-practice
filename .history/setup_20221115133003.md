# Setup instructions for hosting a flask application on a virtual machine connected to a custom domain

## Initial setup requirements:
1. Azure/GCP virtual machine setup on the ubontu system
2. Python coded file with operational front/backend visuals hosted on flask
3. Custom domain of your choosing (Ex .tech)

## Hosting Flask on a VM:
1. Initiate your virtual machine 
2. Connect through SSH
3. Upload/Git clone python file
4. Change directories to the .py file location
5. Run the script
> sudo python3 app.py
6. Confirm on the terminal that the flask application is operational

## Hosting VM IP on a Domain:
1. Locate your public ip address for your virtual machine
2. Navigate to your domain service provider
3. Login to your account
4. Locate the DNS management service (or similar)
5. Add a new 'A Record' 
6. Provide a name for the domain (@ is a wildcard and will default to domain.tech or similar)
7. Provide your IPV4 
8. Adjust TTL to the lowest value
9. Save

### When you navigate to your custom domain, you should be able to view your flask application running. This can be confirmed via virtual machine terminal.