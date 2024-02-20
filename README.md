# Amazon Connect Contact Center
This repo contains a demo intervision use case for a helpdesk system Contact Center using Amazon connect and integrating with AWS services. also another use case for personalized user experience interactions with Amazon Lex, AWS Lambda functions and database integration.
It guides users through different options and directs them to a specific support queues based on thier input. The lambda function is designed to interact with Amazon Connect and a DynamoDB database,it is part of the system that looks up and updates customer information based on their phone number when they call into Amazon Connect. The function performs database queries and updates to maintain a record of customer interactions.
 

# Prerequisites
It is assumed that you understand the use of the services below and you have the following prerequisites:

1. An AWS account with management console.
2. An existing Amazon Connect instance.
3. Amazon Connect Customer Profiles enabled on Connect Instance.

# First use case 
# Helpdesk system contact center 
(InterVision Use Case/AWS_Demo_Flow_HD.json)
{InterVision Use Case/AWS_Demo_Flow_Main.json}
(InterVision Use Case/HelpDesk-Lex_v2_Bot.zip) https://github.com/buks001/amazon-connect-InterVision-use-case/blob/main/InterVision%20Use%20Case/Contact%20flow%20use%20case%201/HelpDesk-Lex_v2_Bot.zip
This flow creates a Help Desk Interactive Voice Response (IVR) application that uses natural language to identify phrases spoken by a caller and perform the correct action.
e.g for intervision use case, to direct your call appropraitely, simply say talk to a consultant after pressing 1.

# Second use case
# Personilized contact contact center
(InterVision Use Case/contactflow/Intervision demo flow usecase)
(InterVision Use Case/contactflow/lamda_db_personalized_flow_intervision)
(InterVision Use Case/Intervisionbot-DRAFT-POII7PBLFK-LexJson.zip) https://github.com/buks001/amazon-connect-InterVision-use-case/blob/main/InterVision%20Use%20Case/Contact%20flow%20use%20case%202/Intervisionbot-DRAFT-POII7PBLFK-LexJson.zip
This flow Creates serverless application with AWS Lambda and Amazon DynamoDB
with the Lambda function to an Amazon Connect instance
it Creates new users, new queues, and modify a routing profile.
The function performs database queries and updates to maintain a record of customer interactions.

 # How to test
 # Use case 1: 
 To direct your call appropraitely, "simply say talk to a consultant after pressing 1 on your keypad"
 # Use case 2: 
 when you press 2, it gives information on when last you call and directs you to an agent.
 
 Simply dial this number and follow each play prompts # 866-573-2012

 
