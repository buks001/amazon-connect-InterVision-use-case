# Amazon Connect Contact Center
This repo contains a demo intervision use case for a helpdesk system Contact Center using Amazon connect and integrating with AWS services. it is designed to provide a personalized user experience interactions with Amazon Lex, AWS Lambda functions and database integration.
It guides users through different options and directs them to a specific support queues based on thier input. The lambda function is designed to interact with Amazon Connect and a DynamoDB database. It is part of the system that looks up and updates customer information based on their phone number when they call into Amazon Connect. The function performs database queries and updates to maintain a record of customer interactions.
 

# Prerequisites
It is assumed that you understand the use of the services below and you have the following prerequisites:

An AWS account with both management console and programmatic administrator access.
An existing Amazon Connect instance.
Amazon Connect Customer Profiles enabled on Connect Instance.
Amazon Connect Cases enabled on Connect Instanc
