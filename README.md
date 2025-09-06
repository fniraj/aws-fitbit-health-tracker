The AWS Fitbit Health Tracker is a cloud-based health monitoring system that integrates the Fitbit API, AWS services, and a Flutter-based frontend to securely collect, store, and display user health metrics such as steps and heart rate. The frontend, developed in Flutter, provides a simple interface for user login and data visualization. Authentication is managed through Fitbit OAuth2, which generates secure access tokens. Once logged in, users can view their health data in the app. The backend is built on AWS. API Gateway serves as the entry point for all client requests and triggers AWS Lambda functions, which handle business logic such as calling the Fitbit API, processing data, and managing communication with the database. DynamoDB, a NoSQL database, stores user profiles and Fitbit health data. Postman and Python scripts were used during development to test endpoints and validate integration. The project was developed collaboratively, with both team members contributing equally to backend services, frontend development, design, and testing. One of the main challenges was understanding AWS components like Lambda, DynamoDB, and API Gateway, and integrating them with Fitbit’s OAuth2 authentication flow. These challenges were addressed by following instructor guidance, using reference tutorials, and iterative testing. This project demonstrates how wearable health data can be effectively combined with serverless cloud computing to provide a secure, scalable, and efficient health tracking solution. Potential future improvements include adding real-time data visualization, expanding analytics capabilities, and supporting additional wearable APIs such as Apple Health or Google Fit.








# final_project

A new Flutter project.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.

