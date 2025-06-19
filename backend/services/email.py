import os
import logging
from typing import Optional
import mailtrap as mt
from utils.config import config

logger = logging.getLogger(__name__)

class EmailService:
    def __init__(self):
        self.sender_email = os.getenv('MAILTRAP_SENDER_EMAIL')
        self.sender_name = os.getenv('MAILTRAP_SENDER_NAME', 'Shukra Team')
        self.api_token = os.getenv('MAILTRAP_API_TOKEN')
        
        if not self.api_token:
            logger.warning("MAILTRAP_API_TOKEN not found in environment variables")
            self.client = None
        else:
            self.client = mt.MailtrapClient(token=self.api_token)
    
    def send_welcome_email(self, recipient_email: str, recipient_name: str):
        subject = "🎉 Welcome to Shukra (Beta) — Let's Get Started "
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Kortix Shukra</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #ffffff;
                    color: #000000;
                    margin: 0;
                    padding: 0;
                    line-height: 1.6;
                }}
                .container {{
                    max-width: 600px;
                    margin: 40px auto;
                    padding: 30px;
                    background-color: #ffffff;
                }}
                .logo-container {{
                    text-align: center;
                    margin-bottom: 30px;
                    padding: 10px 0;
                }}
                .logo {{
                    max-width: 100%;
                    height: auto;
                    max-height: 60px;
                    display: inline-block;
                }}
                h1 {{
                    font-size: 24px;
                    color: #000000;
                    margin-bottom: 20px;
                }}
                p {{
                    margin-bottom: 16px;
                }}
                a {{
                    color: #3366cc;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                .button {{
                    display: inline-block;
                    margin-top: 30px;
                    background-color: #3B82F6;
                    color: white !important;
                    padding: 14px 24px;
                    text-align: center;
                    text-decoration: none;
                    font-weight: bold;
                    border-radius: 6px;
                    border: none;
                }}
                .button:hover {{
                    background-color: #2563EB;
                    text-decoration: none;
                }}
                .emoji {{
                    font-size: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <img src="https://i.postimg.cc/WdNtRx5Z/kortix-shukra-logo.png" alt="Kortix Shukra Logo" class="logo">
                
                <h1>Welcome to Kortix Shukra!</h1>
                
                <div class="content">
                    <p><em><strong>Welcome to Kortix Shukra — we're excited to have you in our closed beta!</strong></em></p>
                    
                    <p>You're one of the select few who have been granted early access to our platform. We value your feedback and insights as we continue to improve Shukra.</p>
                    
                    <p>To celebrate your arrival, here's a <strong>15% discount</strong> to try out the best version of Shukra (1 month):</p>
                    
                    <div class="discount-code">
                        <code>WELCOME15</code>
                    </div>
                    
                    <p>Thanks again, and welcome to the Shukra community <span class="emoji">🌞</span></p>
                    
                    <p>— The Shukra Team</p>
                    
                    <a href="https://www.shukra.so/" class="button">Go to the platform</a>
                </div>
            </div>
            
            <div class="footer">
                <p>Welcome to Shukra — we're excited to have you in our closed beta!</p>
                
                <p>You're one of the select few who have been granted early access to our platform. We value your feedback and insights as we continue to improve Shukra.</p>
                
                <p>To celebrate your arrival, here's a 15% discount to try out the best version of Shukra (1 month):</p>
                
                <p>WELCOME15</p>
                
                <p>Thanks again, and welcome to the Shukra community 🌞</p>
                
                <p>— The Shukra Team</p>
                
                <p>Go to the platform: https://www.shukra.so/</p>
                
                <hr>
                
                © 2024 Shukra. All rights reserved.
                You received this email because you signed up for a Shukra account.
            </div>
        </body>
        </html>
        """
    
    def _send_email(
        self, 
        to_email: str, 
        to_name: str, 
        subject: str, 
        html_content: str, 
        text_content: str
    ) -> bool:
        try:
            mail = mt.Mail(
                sender=mt.Address(email=self.sender_email, name=self.sender_name),
                to=[mt.Address(email=to_email, name=to_name)],
                subject=subject,
                text=text_content,
                html=html_content,
                category="welcome"
            )
            
            response = self.client.send(mail)
            
            logger.info(f"Welcome email sent to {to_email}. Response: {response}")
            return True
                
        except Exception as e:
            logger.error(f"Error sending email to {to_email}: {str(e)}")
            return False
    
    def _get_welcome_email_template(self, user_name: str) -> str:
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome to Kortix Suna</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #ffffff;
      color: #000000;
      margin: 0;
      padding: 0;
      line-height: 1.6;
    }}
    .container {{
      max-width: 600px;
      margin: 40px auto;
      padding: 30px;
      background-color: #ffffff;
    }}
    .logo-container {{
      text-align: center;
      margin-bottom: 30px;
      padding: 10px 0;
    }}
    .logo {{
      max-width: 100%;
      height: auto;
      max-height: 60px;
      display: inline-block;
    }}
    h1 {{
      font-size: 24px;
      color: #000000;
      margin-bottom: 20px;
    }}
    p {{
      margin-bottom: 16px;
    }}
    a {{
      color: #3366cc;
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    .button {{
      display: inline-block;
      margin-top: 30px;
      background-color: #3B82F6;
      color: white !important;
      padding: 14px 24px;
      text-align: center;
      text-decoration: none;
      font-weight: bold;
      border-radius: 6px;
      border: none;
    }}
    .button:hover {{
      background-color: #2563EB;
      text-decoration: none;
    }}
    .emoji {{
      font-size: 20px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="logo-container">
      <img src="https://i.postimg.cc/WdNtRx5Z/kortix-suna-logo.png" alt="Kortix Suna Logo" class="logo">
    </div>
    <h1>Welcome to Kortix Suna!</h1>

    <p>Hi {user_name},</p>

    <p><em><strong>Welcome to Kortix Suna — we're excited to have you on board!</strong></em></p>

    <p>To get started, we'd like to get to know you better: fill out this short <a href="https://docs.google.com/forms/d/e/1FAIpQLSef1EHuqmIh_iQz-kwhjnzSC3Ml-V_5wIySDpMoMU9W_j24JQ/viewform">form</a>!</p>

    <p>To celebrate your arrival, here's a <strong>15% discount</strong> to try out the best version of Suna (1 month):</p>

    <p>🎁 Use code <strong>WELCOME15</strong> at checkout.</p>

    <p>Let us know if you need help getting started or have questions — we're always here, and join our <a href="https://discord.com/invite/FjD644cfcs">Discord community</a>.</p>

    <p>Thanks again, and welcome to the Suna community <span class="emoji">🌞</span></p>

    <p>— The Suna Team</p>

    <a href="https://www.suna.so/" class="button">Go to the platform</a>
  </div>
</body>
</html>"""
    
    def _get_welcome_email_text(self, user_name: str) -> str:
        return f"""Hi {user_name},

Welcome to Suna — we're excited to have you on board!

To get started, we'd like to get to know you better: fill out this short form!
https://docs.google.com/forms/d/e/1FAIpQLSef1EHuqmIh_iQz-kwhjnzSC3Ml-V_5wIySDpMoMU9W_j24JQ/viewform

To celebrate your arrival, here's a 15% discount to try out the best version of Suna (1 month):
🎁 Use code WELCOME15 at checkout.

Let us know if you need help getting started or have questions — we're always here, and join our Discord community: https://discord.com/invite/FjD644cfcs

Thanks again, and welcome to the Suna community 🌞

— The Suna Team

Go to the platform: https://www.suna.so/

---
© 2024 Suna. All rights reserved.
You received this email because you signed up for a Suna account."""

email_service = EmailService() 
