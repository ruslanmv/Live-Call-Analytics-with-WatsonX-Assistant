# Live Phone Call Analytics with WatsonX.ai

In this project, we will build a dashboard to monitor and analyze Call Center interactions between customers and an AI assistant using WatsonX.ai. Our goal is to enhance the human experience in real-time by creating an advanced virtual assistant powered by LMMs and incorporating human feedback to improve the quality of the virtual assistants.

We will use reinforcement learning for our question and answer models, classify conversations based on quality, and flag unsatisfactory conversations to be handled by a real human. This will ensure the client's needs are met and improve overall customer satisfaction.

## Infrastructure

The infrastructure for this project consists of three main parts:

### Part 1 - LMM Virtual Assistant

1. Create a chatbot powered by WatsonX.ai using a simple vector database to store questions and answers.
2. Utilize the standard RAG (Retriever-Augmented Generation) to retrieve the most accurate answer.
3. Implement reinforcement learning and update the model monthly.

### Part 2 - AI Microservices

1. Enable various microservices provided by IBM, such as Speech-to-Text, Text-to-Speech, and VoIP services to trigger phone calls to our system.

### Part 3 - Monitoring Dashboard

1. Create a custom server in IBM Code Engine to host a monitoring dashboard for real-time call analytics.

## Building the Project


1. Configure your API keys and credentials for IBM Cloud, WatsonX.ai, and other required services in the `config.py` file.

2. Deploy the custom server and dashboard to IBM Code Engine:

- Follow the [official documentation](https://cloud.ibm.com/docs/codeengine?topic=codeengine-getting-started) to create a new project and deploy the application.

5. Navigate to the provided URL to access the monitoring dashboard and start analyzing live phone call interactions.

## How to Improve

1. Continuously update the vector database with new questions and answers to enhance the AI assistant's knowledge base.
2. Regularly review flagged conversations to identify common issues and improve the AI assistant's ability to handle those situations.
3. Refine the reinforcement learning model by incorporating more advanced techniques and adjusting the update frequency based on performance.

## Contributing

We welcome contributions to improve and expand this project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them to your branch.
4. Submit a pull request to the main repository.

We will review your changes and provide feedback before merging.

## License

This project is licensed under the MIT License. See the [MIT](LICENSE) file for details.

## Acknowledgements

- WatsonX.ai for providing the AI services and infrastructure.
- IBM Cloud for hosting the monitoring dashboard and AI microservices.
- The open-source community for their continuous support and inspiration.

Let's start building a powerful live phone call analytics system for an enhanced customer experience!