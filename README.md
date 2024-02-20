# Amazon Connect Contact Center
This repo contains a demo interVision use case for a helpdesk system Contact Center using Amazon connect and integrating with AWS services. also another use case for personalized user experience interactions with Amazon Lex, AWS Lambda functions and database integration.
It guides users through different options and directs them to a specific support queues based on thier input. The lambda function is designed to interact with Amazon Connect and a DynamoDB database,it is part of the system that looks up and updates customer information based on their phone number when they call into Amazon Connect. The function performs database queries and updates to maintain a record of customer interactions.
 

# Prerequisites
It is assumed that you understand the use of the services below and you have the following prerequisites:

1. An AWS account with management console.
2. An existing Amazon Connect instance.
3. Amazon Connect Customer Profiles enabled on Connect Instance.

# First use case 
# Helpdesk system contact center 
This flow creates a Help Desk Interactive Voice Response (IVR) application that uses natural language to identify phrases spoken by a caller and perform the correct action.
e.g for intervision use case, to direct your call appropraitely, simply say "talk to a consultant after pressing 1".

# Steps
1. Import the Lex bot zip file in the folder
2. Add the Amazon Lex bot to an Amazon Connect instance
3. Import the contact flow named "intervison demo flow use case"
4. Test your Lex IVR

[Intervisionbot-DRAFT-POII7PBLFK-LexJson.zip](https://github.com/buks001/amazon-connect-InterVision-use-case/files/14339580/Intervisionbot-DRAFT-POII7PBLFK-LexJson.zip)

 # How to test
Use case 1: 
To direct your call appropriately, "simply say talk to a consultant after pressing 1 on your keypad"
   



# Second use case
# Personalized contact center
This use case uses serverless architecture with lambda and dynamodb integration with Amazon connect.
It performs database queries and updates to maintain a record of customer interactions to give a personlized experience to the caller.
e.g for interVision use-case, to direct your call agent confirms your last call Date and time, and if its your first call, agent recognizes its your first call and input your information so that when you call again it is already registered in the system. 

# Steps
1. Create serverless application with AWS Lambda and Amazon DynamoDB "lamda function.py code in the repo"
3. Add the Lambda function to an Amazon Connect instance
4. Create new users, new queues, and modify a routing profile
5. Import the contact flow named "lambda db personalized flow intervision"
6. Place a test call, update the records database, and place a second test call

   

 [Screen Shot 2024-02-19 at 9 23 08 PM](https://github.com/buks001/amazon-connect-InterVision-use-case/assets/63078734/08f4e9a4-f4a8-4d6f-a7a8-f741551cb17e)

 [Screen Shot 2024-02-19 at 9 20 32 PM](https://github.com/buks001/amazon-connect-InterVision-use-case/assets/63078734/978d2c2d-c765-4692-8745-daf999ec66b9)



# How to test
Use case 2: 
when you press 2, for a new caller it will automatically update the record in the database and give information on the date and directs you to an agent
when you place a second call, it already updates your information on when last you call and directs you to an agent.
 
Simply dial this number and follow each play prompts to confirm the usage. # 866-573-2012

 
