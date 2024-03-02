# How to build a Live Phone Call Analytics in WatsonX.ai

We are going to build a dashboard to monitor the Call Center between a customer and the AI assitant by using WatsonX.ai

We are intested to monitor the incomming phone calls to the virtual assitant and analize the human experience in real time.

We will create an advanced Virtual Assitant powered by LMMs in WatsonX.ai.

Including the human feedback to improve the quality the virtual assistants by integrating reinforcement learning to our models of question and answering.

Moreover each coversation is classified by the quality and when the converstaion does not satisfy the customer satisfaction. It is flagged and it is passed the conversation to a real human to satisfy te needs of the client.



# Infrastructure

## Part 1 - LLM Virtual Assisntat
First we need to create our chatbot powered poweed by Watsonx.ai 
We will use a simple vector database where we store questions and answers.  We will use the standard RAG to retrieve the most accurate answer.

For the reinformment learning , it is updated monthly the model.


## Part 2 - AI Microservices.

It is requiered enable some microserviced provided by IBM like 
speech to text,  text to speech and also VoIP servcies. To trigger the phone calls to our systems.

## Part 3 - Monitoring Dashboard

It is needed create a Custom server in Code Engine 





