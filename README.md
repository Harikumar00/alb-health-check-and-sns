┌──────────────────────────┐
│      CloudWatch Rule     │
│   (Every 10 Minutes)     │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│        AWS Lambda        │
│  ELB Health Checker     │
│  (Boto3 + Python)       │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│ Application Load Balancer│
│        (ALB)             │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│        Target Group      │
│  Registered EC2 Instances│
│                          │
│  - Instance 1 (Healthy)  │
│  - Instance 2 (Unhealthy)│
└─────────────┬────────────┘
              │
     If Unhealthy Found
              │
              ▼
┌──────────────────────────┐
│        Amazon SNS        │
│   (Email Notification)  │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│      Email Subscriber    │
│  Health Alert Received   │
└──────────────────────────┘


##Screenshots 
Health checker:
<img width="1440" height="900" alt="Screenshot 2025-12-26 at 14 43 14" src="https://github.com/user-attachments/assets/257b1a3e-ca90-43a3-b02f-592f8af187c0" />
![Uploading Screenshot 2025-12-26 at 14.43.14.png…]()

Terminal output:
<img width="1440" height="900" alt="Screenshot 2025-12-26 at 14 44 16" src="https://github.com/user-attachments/assets/8545259b-2115-4b32-8521-29acdeea9a5d" />

SNS subscription:
<img width="1440" height="900" alt="Screenshot 2025-12-26 at 14 45 23" src="https://github.com/user-attachments/assets/1c07603b-a846-4030-889c-f3625a85ed1d" />

SNS triggered mail:
<img width="1440" height="900" alt="Screenshot 2025-12-26 at 14 46 00" src="https://github.com/user-attachments/assets/63cd98e8-2c35-4602-9fbd-adf687673201" />

TARGET group used:
<img width="1440" height="900" alt="Screenshot 2025-12-26 at 14 48 59" src="https://github.com/user-attachments/assets/7da8efa2-faf2-48a8-9ac3-a79ef5357cfa" />





