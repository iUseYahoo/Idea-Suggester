from flask import Flask, request
from flask_cors import CORS
import json, requests, sys, sqlite3, hashlib

conn = sqlite3.connect('./Database/main.db', check_same_thread=False)
cursor = conn.cursor()

###########################################
# Using the config file's set variables   #
###########################################
config_file = open('./config.json', 'r')
config = json.load(config_file)
config_port = config['port']
config_debug_mode = config['useDebugMode']
config_webhook_url = config['discordWebhook']

api_port = config_port
api_use_debug = config_debug_mode
api_webhook_url = config_webhook_url

config_file.close()


###########################################
# Testing if the webhook is valid         #
###########################################

if api_webhook_url == "":
    print("Webhook is not valid. Please check the config file.")
    sys.exit()

testwebhook = requests.get(api_webhook_url, allow_redirects=False)

if testwebhook.status_code != 200:
    print("This webhook didn't return with status code 200, This webhook may be dead.")
    sys.exit()
elif testwebhook.status_code == 200:
    pass
else:
    print(f"Status Code: {testwebhook.status_code}")
    sys.exit()
    

###########################################
# Main API code                           #
###########################################
app = Flask(__name__)
CORS(app)

###########################################
# Send a suggestion page                  #
###########################################
@app.route("/suggestion/", methods=['POST'])
def send_suggestion():

    hash_ip = hashlib.md5(request.remote_addr.encode('utf-8')).hexdigest()
    cursor.execute(f"SELECT ip FROM logged_ips WHERE ip == '{str(hash_ip)}'")
    ip_check = cursor.fetchone()
    if ip_check is None:
        hashed_ip = hashlib.md5(request.remote_addr.encode('utf-8')).hexdigest()
        cursor.execute(f"INSERT INTO logged_ips (ip) VALUES ('{str(hashed_ip)}')")
        conn.commit()

        if request.method == 'POST':
            user_suggestion = request.args.get("suggestion")

            if user_suggestion is None:
                return "No suggestion"
            else:

                cursor.execute(f"INSERT INTO Suggestions (suggestion, ip) VALUES ('{str(user_suggestion)}', '{str(hashed_ip)}')")
                conn.commit()

                send_data = {
                    "content": f'**New Suggestion**\n{str(user_suggestion)}\n*This person\'s IP was also added to the database.*'
                }
                send_req = requests.post(api_webhook_url, data=send_data)
            
                if send_req.status_code == 200:
                    return "Suggestion sent. Note: Your IP was logged into a database but hashed to prevent abuse. To have your Hashed IP removed please contact the developer."
                else:
                    return f"Error sending, Status Code: {send_req.status_code}"
        else:
            return "You cannot access this page. This is for posting suggestions."
    else:
        return "You have already used the API. Please contact the developer to be allowed to use it again. Note: Your IP was logged into a database but hashed to prevent abuse. To have your Hashed IP removed please contact the developer."


if __name__ == '__main__':
    app.run(port=api_port, debug=api_use_debug)