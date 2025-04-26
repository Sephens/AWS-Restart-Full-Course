# Amazon Comprehend
---
## What problems does Amazon Comprehend solve?  

Amazon Comprehend is an NLP service that uses machine learning (ML) to uncover valuable insights and relationships in text. With Amazon Comprehend, you do not need ML expertise to build intelligent applications.

Amazon Comprehend has pre-trained models that can do the following:
* Identify entities such as person, organization, quantity, location, or event.
* Analyze text for speciﬁc types of events and their related entities.
* Extract key phrases and determine the language of text.
* Analyze text to understand how positive or negative sentiment is and gain deeper understanding of the sentiments associated with specific entities.
* Parse words from documents to return part of speech or syntactic function for each word in the document.
* Organize a collection of documents by topic automatically.

Amazon Comprehend can also be used to train customized NLP models to meet your specific requirements. You provide the training data, and Amazon Comprehend creates the model on your behalf. The service can be used to create custom NLP models that can do the following:

* Identify values for entity types that you define, which may be specific to your business or domain. This is called custom named-entity recognition (NER). Examples of named entities include product names, department codes, or other entities that are relevant for your specific use case.

* Classify your text using custom labels that you define. For example, you can use this feature to automatically categorize inbound support requests by problem type based on how the customer described the issue.
To further streamline the process, you can use custom models directly on plain-text, but also on scanned or digital semi-structured documents such as PDFs, Microsoft Word documents, and images. This eliminates the need to pre-process documents to extract text before running the models.

---

## What are the benefits of Amazon Comprehend?
### 1. Integrate powerful NLP into applications

Amazon Comprehend provides accurate NLP available as a set of APIs so you can add text analysis capabilities to your applications. You don't need ML or text-mining expertise to make the most of the insights that Amazon Comprehend can extract.

### 2. Simplify document processing workflows

Streamline document processing activities by using Amazon Comprehend for extracting and recognizing key phrases, entities, topics, sentiment, and more. For example, you can use Amazon Comprehend to automate the classification of contracts and legal documents. You can also use it to extract entities from financial service documents such as insurance claims or mortgage packages, or to find relationships between financial events in a financial report. If you use custom classification or entity recognition models, you don’t even need to extract text before running the actual NLP task. In such scenarios, Amazon Comprehend can directly work on documents in their native format.

### 3. Use Amazon Comprehend with other AWS services

Amazon Comprehend integrates seamlessly with other AWS services. For instance, you can ingest real-time streams with Amazon Kinesis Data Firehose, store data in Amazon Simple Storage Service (Amazon S3), and then use Amazon Comprehend to extract insights.

### 4. Gain privacy, security, and compliance

AWS Identity and Access Management (IAM) can be used to securely control access to Amazon Comprehend operations. Using IAM, you can create and manage AWS users and groups to grant the appropriate access to your developers and end users.


You can already use Amazon S3 to encrypt your input documents, and Amazon Comprehend extends this even further. By using your own AWS Key Management Service (AWS KMS) key, you can encrypt the output results of your job. You can also encrypt the data on the storage volume attached to the compute instance that processes the analysis job.


The result is significantly enhanced security. Third-party auditors assess the security and compliance of Amazon Comprehend as part of multiple compliance programs. These include the payment card industry (PCI), Federal Risk and Management Program (FedRAMP), Health Insurance Portability and Accountability Act (HIPAA), and others.

### 5. Pay only for features you use

When using Amazon Comprehend, there are no upfront commitments or minimum fees. Customers are charged for the documents they analyze and the custom models they train. Amazon Comprehend offers a pay-as-you-go approach for pricing. You pay only for the specific features you need for the time you use them and without long-term contracts. After you stop using the service, there are no additional costs or termination fees.

---

## Architecture and Use Cases

---

### What are the basic technical concepts of Amazon Comprehend?

#### 1. Analysis
**Sentiment analysis** - Sentiment analysis determines the dominant sentiment of a document. Sentiment can be positive, neutral, negative, or mixed.

**Targeted sentiment analysis** - Targeted sentiment analysis determines the sentiment of specific entities mentioned in a document. The sentiment of each mention can be positive, neutral, negative, or mixed.

**Syntax analysis** - Syntax analysis is parsing each word in a document and determining the part of speech for the word, such as pronoun, adjective, or verb.

#### 2. Annotations

Annotations are a dataset providing the location and type of entities appearing in a large collection of documents.



#### 3. Classification
**Custom classification** - For this task, one or more documents are classified based on a set of categories (or classes) defined by the user.

**Single-label custom classification** - For this task, each document can have one and only one class assigned to it. The individual classes are mutually exclusive.

**Multi-label custom classification** - For this task, individual classes represent different categories that are not mutually exclusive. As a result, each document has at least one class assigned to it, but can have more if needed.

#### 4. Custom entity recognition

This is the recognition of entities in a document according to a set of entity types defined by the user.

#### 5. Data
**Training data** - This data is used to train an ML model, such as a custom classifier or custom entity recognizer.

**Test data** - This data is used to test and assess the performance of an ML model after it has been trained. Test data should not be a subset of training data. 

#### 6. Document processing modes

**Single-document synchronous analysis (real time)** - In this mode, you provide a single document to Amazon Comprehend and receive a response right away. 

**Multi-document synchronous analysis (real time)** - In this mode, you provide a collection of up to 25 documents to Amazon Comprehend and receive a synchronous response. 

**Asynchronous batch analysis** - In this mode, you can perform an asynchronous analysis job on a large collection of documents. Upload files to an S3 bucket, start the job, and the results of the analysis will be stored in the bucket or folder that you specify in the request.



#### 7. Dominant language

This is the primary language used in the document.

#### 8. Entity

This is a textual reference to the name of a real-world object or concept, such as people, places, commercial items, dates, and quantities.

#### 9. Entity lists

This is the list of entities and their type label.

#### 10. Key phrase

A key phrase is a string consisting of a noun phrase that describes a certain thing.

#### 11. Personally identifiable information (PII)

PII is personal data that identifies an individual, such as an address, bank account number, or phone number.

---

### What are some typical use cases for Amazon Comprehend?

#### 1. Contact center intelligence

Use Amazon Comprehend to build intelligent contact center solutions that can identify customer sentiment and customer interactions to automatically categorize incoming requests. For example, Amazon Comprehend can categorize support requests by problem type, based on how the customer has described the issue. After categorization, you can route requests to the proper support team for immediate help.

#### 2. Intelligent Document Processing

Build intelligent document processing (IDP) solutions to classify and extract entities from documents such as insurance claims or mortgage packages. This can also help companies automate and streamline operational workflows. You can use Amazon Comprehend to detect language, entities, key phrases, topics, sentiment, and PII from structured or unstructured documents. This helps customers save effort and time in manually reviewing documents and performing data entry operations.

#### 3. Consumer insights

Understanding customer sentiment across various products or services is key to understanding the health of a business. Amazon Comprehend can be used to analyze and interpret customer reviews and feedback to improve your processes, product development, and support. You can use the Amazon Comprehend sentiment analysis capability to turn qualitative customer feedback into actionable insights by determining whether feedback is positive, negative, or neutral.


In addition, Amazon Comprehend targeted sentiment provides users with a more granular analysis that links sentiment to specific items. Users can then focus on specific areas of a product or business at scale.

