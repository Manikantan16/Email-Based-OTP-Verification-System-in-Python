## 📧 🔢 Email Based OTP Verification System in Python
- This project implements a One-Time Password (OTP) verification system that sends an OTP to the user’s email for secure authentication.
## 🔧 Key Features:
- **OTP Generation:** Securely generates a 5 digit random numeric OTP.
- **Email Integration:** Sends the OTP to a specified email address using Gmail SMTP.
- **OTP Validation:** Accepts user input and verifies the entered OTP against the generated one.
## 🛠️ Tech Stack:
- **Language:** Python
- **Editor:** VSCode
- **Libraries:**
  - smtplib – to send emails
  - random – for OTP generation
  - dotenv - Keep your Gmail SMTP credentials hidden by storing them outside your main VS Code project, such as in a .env file.
  - Commands:
      -  pip install python-dotenv
## 📌 Note:
 - To securely use Gmail SMTP, you need to generate and use an App Password if 2-Step Verification is enabled on your Google account.
 - Without it, emails will fail to send.
## 🧩 Workflow:
- Key in the Senders Name
- Key in the Senders Email
- System generates an OTP and OTP is sent to the senders email
- User enters OTP
- System verifies OTP
- If Valid then ✅ OTP verified successfully! 🔐 If not, you'll see: ❌ Incorrect OTP.
## 📷 O/P Screenshots:
- *Wrong OTP*
  ![Incorrect_OTP](https://github.com/user-attachments/assets/543f9153-ffc8-43ec-95f1-6bdfadce69d1)

- *Valid OTP*
  ![Correct_OTP](https://github.com/user-attachments/assets/4257e620-4e6c-4ce8-8c7b-c711145acde1)

## ✍️ Conclusion:
Implementing an OTP (One-Time Password) verification system enhances the security and reliability of user authentication. By generating and validating time-sensitive OTPs—especially when combined with secure email delivery and environment variable management—developers can protect sensitive actions and user data. 

A special thanks to my dear friend Sunitha 👫🙏 for inspiring me throughout this journey.
  
  

 
